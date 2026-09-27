"""Run with python -B scripts/test_site.py; fixtures stay in a temporary directory."""
import importlib.util
import io
import os
import shutil
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent


def load(relative_path):
    spec = importlib.util.spec_from_file_location(Path(relative_path).stem, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_links(root):
    converter = load('site/link_converter.py')
    health = load('scripts/wiki-health-check.py')
    wiki = root / 'wiki'
    for name in ('concepts/概念V1.0.md', 'concepts/同名.md', 'topics/同名.md', '索引.md'):
        path = wiki / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text('---\ntitle: test\n---\n', encoding='utf-8')
    content = '[[wiki/concepts/概念V1.0.md|概念]] [[wrong/概念V1.0]] [[同名]] [[concepts/同名]]'
    source = wiki / '索引.md'
    source.write_text('---\ntitle: index\n---\n' + content, encoding='utf-8')
    index = converter.build_page_index(wiki)
    missing = []
    converted = converter.convert_wiki_links(content, source, index, wiki, missing)
    assert missing == ['wrong/概念V1.0', '同名'], missing
    assert '[概念](concepts/概念V1.0.md)' in converted, converted
    assert '[concepts/同名](concepts/同名.md)' in converted
    assert '\\' not in converted
    issues = health.check_wiki(root)
    assert [target for _, target in issues['broken_links']] == missing, issues
    assert 'topics/同名.md' in issues['orphan_pages'], issues
    assert 'concepts/同名.md' not in issues['orphan_pages'], issues
    assert 'concepts/概念V1.0.md' not in issues['missing_from_index'], issues
    raw = root / 'raw' / 'articles'
    raw.mkdir(parents=True)
    (raw / '概念V1.0.md').write_text('raw', encoding='utf-8')
    index = converter.build_page_index(wiki, root / 'raw')
    assert converter.resolve_link('概念V1.0', index) == 'concepts/概念V1.0.md'
    assert converter.resolve_link('raw/articles/概念V1.0.md', index) == 'raw/articles/概念V1.0.md'
    assert converter.resolve_link('wrong/概念V1.0', index) is None
    print('PASS: shared link resolution, ambiguity, raw paths and diagnostics')


def test_build(root):
    for relative in ('site/site_builder.py', 'site/link_converter.py', 'site/doc_config.py',
                     'site/check-yaml.py', 'scripts/wiki-health-check.py'):
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / relative, target)
    sources = root / 'wiki' / 'sources'
    sources.mkdir(parents=True)
    original = '---\ntitle: sample\ntype: source\nsource: raw/papers/sample.pdf\n---\n# Sample\n[[missing|display]]\n'
    source = sources / 'sample.md'
    source.write_text(original, encoding='utf-8')
    raw = root / 'raw'
    raw.mkdir()
    (raw / 'release-map.tsv').write_text('local\trelease\nsample.pdf\tsample-download.pdf\n', encoding='utf-8')
    (root / 'mkdocs.yml').write_text('site_name: test\ndocs_dir: site/content\nsite_dir: site/build\n', encoding='utf-8')
    env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
    env['PATH'] = str(Path(sys.executable).parent) + os.pathsep + env.get('PATH', '')
    builder = load(root / 'site/site_builder.py')
    output = io.StringIO()
    # Rendering stays real; the test account cannot create raw-file symlinks on Windows.
    with patch.dict(os.environ, env), patch.object(Path, 'symlink_to'), redirect_stdout(output):
        builder.main()
    html = (root / 'site/build/sources/sample/index.html').read_text(encoding='utf-8')
    assert 'releases/download/raw-v2-aligned/sample-download.pdf' in html
    assert '[[missing]]' in output.getvalue() and 'Unresolved: 1' in output.getvalue(), output.getvalue()
    assert source.read_text(encoding='utf-8') == original
    print('PASS: real MkDocs output contains PDF download; missing target reported; source unchanged')


def test_navigation(root):
    config = load('site/doc_config.py')
    concepts = root / 'concepts'
    concepts.mkdir(parents=True)
    for name, tags in (('MOSA', '[]'), ('未知', '[unknown]'), ('标准', '[FACE, MOSA]')):
        (concepts / f'{name}.md').write_text(
            f'---\ntags: {tags}\n---\n# {name}\n', encoding='utf-8'
        )
    nav = config.generate_navigation(root)
    groups = {name: items for entry in nav[1]['概念'][1:] for name, items in entry.items()}
    assert groups['MOSA基础'] == [{'MOSA': 'concepts/MOSA.md'}], groups
    assert groups['其他'] == [{'未知': 'concepts/未知.md'}], groups
    assert groups['接口与架构标准'] == [{'标准': 'concepts/标准.md'}], groups
    index = (concepts / 'index.md').read_text(encoding='utf-8')
    for name, entries in groups.items():
        text = index.split(f'## {name}\n', 1)[1].split('\n## ', 1)[0]
        for entry in entries:
            for title, filename in entry.items():
                assert f'[{title}]({Path(filename).stem})' in text, text
    print('PASS: index and navigation share fallback, unknown-tag and first-tag grouping')


if __name__ == '__main__':
    with tempfile.TemporaryDirectory(prefix='llm-wiki-test-') as directory:
        test_links(Path(directory))
        test_build(Path(directory) / 'build-case')
        test_navigation(Path(directory) / 'nav-case')
