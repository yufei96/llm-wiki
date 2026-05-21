#!/usr/bin/env python3
"""
Build MkDocs site from Obsidian wiki.
1. Copy wiki/ to site/content/
2. Convert [[wiki-links]] to standard markdown
3. Run mkdocs build
"""
import shutil
import re
import os
import subprocess
import sys
import yaml
from urllib.parse import quote
from pathlib import Path

def quote_path(path: str) -> str:
    """URL-encode non-ASCII characters in a path, preserving / separators."""
    parts = path.split('/')
    return '/'.join(quote(p, safe='') for p in parts)

ROOT = Path(__file__).parent.parent
WIKI_SRC = ROOT / "wiki"
BUILD_DIR = ROOT / "site" / "content"
SITE_OUT = ROOT / "site" / "build"
MKDOCS_YML = ROOT / "mkdocs.yml"
MKDOCS_BUILD_YML = ROOT / "site" / "mkdocs.yml"

def build_page_index(wiki_root: Path) -> dict:
    index = {}
    for md_file in wiki_root.rglob("*.md"):
        rel = md_file.relative_to(wiki_root)
        name = md_file.stem
        index[name] = str(rel)
        parent = rel.parent
        if parent != Path('.'):
            index[f"{parent.name}/{name}"] = str(rel)
    return index

def convert_wiki_links(content: str, current_file: Path, page_index: dict, wiki_root: Path) -> str:
    current_dir = current_file.parent

    def replace_link(match):
        full = match.group(1)
        if '|' in full:
            target, display = full.split('|', 1)
        else:
            target = full
            display = full

        target = target.strip()
        display = display.strip()
        # Strip .md extension for lookup
        lookup_target = target[:-3] if target.endswith('.md') else target
        # Strip wiki/ prefix (Obsidian cross-vault links)
        if lookup_target.startswith('wiki/'):
            lookup_target = lookup_target[5:]

        if target.startswith(('http://', 'https://', '#', '!')):
            return match.group(0)
        resolved_path = page_index.get(lookup_target)
        if not resolved_path:
            # Try partial matches
            for subdir in ['sources', 'concepts', 'entities', 'topics', 'comparisons', 'raw/articles', 'raw/papers', 'raw/archive-2026-05-17', 'raw/repo']:
                key = f"{subdir}/{lookup_target}"
                if key in page_index:
                    resolved_path = page_index[key]
                    break

        if resolved_path:
            # For raw/ assets, use site-root-relative path (will be symlinked into build output)
            if resolved_path.startswith('raw/'):
                rel = f"/{resolved_path}"
            else:
                target_path = wiki_root / resolved_path
                try:
                    rel = os.path.relpath(target_path, current_dir)
                except ValueError:
                    rel = resolved_path
            return f"[{display}]({rel})"
        else:
            return f"[{display}]({target}.md)"

    pattern = r'\[\[([^\]]+)\]\]'
    result = re.sub(pattern, replace_link, content)
    # URL-encode non-ASCII chars in markdown links (for Cloudflare Pages compatibility)
    result = re.sub(
        r'(\[[^\]]*\]\()([^)]*[\u4e00-\u9fff][^)]*)(\))',
        lambda m: m.group(1) + quote_path(m.group(2)) + m.group(3),
        result
    )
    return result

def extract_title(md_file: Path) -> str:
    """Extract title from YAML frontmatter or first heading."""
    try:
        content = md_file.read_text(encoding='utf-8')
    except Exception:
        return md_file.stem

    # Try YAML frontmatter
    fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', fm_match.group(1), re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()

    # Try first heading
    heading_match = re.search(r'^#\s+(.+)', content, re.MULTILINE)
    if heading_match:
        return heading_match.group(1).strip()

    return md_file.stem


def generate_section_indexes(content_dir: Path):
    """Auto-generate index.md for each section directory with tag-based grouping."""
    sections = ['topics', 'concepts', 'comparisons', 'entities', 'sources']
    section_titles = {
        'topics': '主题',
        'concepts': '概念',
        'comparisons': '对比',
        'entities': '实体',
        'sources': '来源',
    }
    section_descs = {
        'topics': '综合多来源的主题深度文章',
        'concepts': '独立概念释义',
        'comparisons': '跨领域对比分析',
        'entities': '人物、组织与政策实体',
        'sources': '原始来源摘要与引用',
    }

    # Tag-to-category mapping for auto-grouping (per-section)
    # Each section has its own semantic domain, so shared mappings don't work.
    category_maps = {
        'topics': {
            'MOSA': 'MOSA核心', 'mosa': 'MOSA核心', '模块化': 'MOSA核心',
            'GRA': '政府参考架构', 'ABMS': '政府参考架构', 'Sentinel': '政府参考架构',
            'PNT': '政府参考架构',
            'MBSE': '系统工程与建模', 'SysML': '系统工程与建模',
            'INCOSE': '系统工程与建模', '系统工程': '系统工程与建模',
            'NASA': '系统工程与建模', 'NIST': '系统工程与建模',
            'CMU': '系统工程与建模', 'SEI': '系统工程与建模',
            'DoD': '采办与政策', '国防采办': '采办与政策', '采办': '采办与政策', '政策': '采办与政策',
            'CCA': '协作作战飞机', 'DEW': '定向能武器',
            'NATO': 'NATO与国际化', '国际化': 'NATO与国际化',
            'FACE': '开放标准', 'SOSA': '开放标准', 'OMS': '开放标准',
            'HOST': '开放标准', 'WOSA': '开放标准', '开放架构': '开放标准', '标准': '开放标准',
            '数字工程': '数字工程', 'Digital Engineering': '数字工程',
            'DEE': '数字工程', '数字化转型': '数字工程',
            '中国': '中国与民用', '智能网联': '中国与民用',
            '智能网联汽车': '中国与民用', '车路云一体化': '中国与民用', 'V2X': '中国与民用',
            '无人机': '中国与民用', '华为': '中国与民用',
            '韧性': '系统特性', '安全': '系统特性', '弹性': '系统特性',
            '赛博弹性': '系统特性', '网络安全': '系统特性',
        },
        'concepts': {
            'MOSA': 'MOSA基础', 'mosa': 'MOSA基础', '模块化': 'MOSA基础',
            'GRA': '政府参考架构', 'ABMS': '政府参考架构', 'Sentinel': '政府参考架构',
            'PNT': '政府参考架构', 'NC3': '政府参考架构',
            'R-EGI': '政府参考架构', 'DEWS': '政府参考架构',
            'FACE': '接口与架构标准', 'SOSA': '接口与架构标准', 'OMS': '接口与架构标准',
            'HOST': '接口与架构标准', 'WOSA': '接口与架构标准', 'UCS': '接口与架构标准',
            'MORA': '接口与架构标准', 'COARPS': '接口与架构标准', 'SCARS': '接口与架构标准',
            'VICTORY': '接口与架构标准', 'CMOSS': '接口与架构标准',
            '开放架构': '接口与架构标准', 'UAI': '接口与架构标准',
            'MBSE': '系统工程', 'SysML': '系统工程', 'INCOSE': '系统工程',
            '系统工程': '系统工程', 'NASA': '系统工程', 'NIST': '系统工程',
            '架构框架': '系统工程', '系统集成': '系统工程',
            '数字工程': '数字工程', 'Digital Engineering': '数字工程',
            '数字孪生': '数字工程', 'DMM': '数字工程', '数字化转型': '数字工程',
            'DoD': '采办与国防', '国防采办': '采办与国防', '采办': '采办与国防',
            'defense-acquisition': '采办与国防', 'cost-overrun': '采办与国防', 'MDAP': '采办与国防',
            'AAF': '采办与国防', 'MTA': '采办与国防', '供应商锁定': '采办与国防',
            '成本超支': '采办与国防', '国防': '采办与国防',
            'CCA': '作战概念', '软件定义能力': '作战概念',
            'modularity': 'MOSA基础', 'architecture': 'MOSA基础', 'patterns': 'MOSA基础',
            'defense': '采办与国防', 'cross-domain': 'MOSA基础',
            '韧性': '系统属性', '安全': '系统属性', '弹性': '系统属性',
            '赛博弹性': '系统属性', '网络安全': '系统属性',
        },
        'entities': {
            # Entity-type based classification — NOT topic-based
            '美国国防部': '国防部及军种',
            'DoD': '国防部及军种', 'OUSD': '国防部及军种',
            'AFMC': '国防部及军种', 'AFLCMC': '国防部及军种', 'AFRL': '国防部及军种',
            'USAF': '国防部及军种', 'AFGSC': '国防部及军种', 'DAF': '国防部及军种', 'SAB': '国防部及军种',
            'NAVAIR': '国防部及军种', '海军': '国防部及军种',
            '太空军': '国防部及军种', 'SDA': '国防部及军种', '太空架构': '国防部及军种',
            '战略司令部': '国防部及军种', '核力量': '国防部及军种',
            '组织': '国防部及军种', 'PMA-209': '国防部及军种',
            '数字装备管理': '国防部及军种', 'DEM&S': '国防部及军种',
            '承包商': '防务承包商', '国防工业': '防务承包商',
            'Lockheed-Martin': '防务承包商', 'Northrop-Grumman': '防务承包商',
            'RTX': '防务承包商',
            'CCA': '防务承包商', '自主系统': '防务承包商',
            '国防科技': '防务承包商', '无人机': '防务承包商',
            '无人系统': '防务承包商',
            'NATO': '国际与标准组织', '联盟': '国际与标准组织', '国际化': '国际与标准组织',
            '专业组织': '国际与标准组织', '标准组织': '国际与标准组织',
            '行业联盟': '国际与标准组织', '互操作': '国际与标准组织',
            'GAO': '政府监察与政策', 'OMB': '政府监察与政策',
            '咨询机构': '政府监察与政策', '联邦机构': '政府监察与政策',
            'DSB': '政府监察与政策', '技术评估': '政府监察与政策',
            '监察': '政府监察与政策', '国会': '政府监察与政策',
            '政策': '政府监察与政策', '预算': '政府监察与政策',
            '采办评估': '政府监察与政策', '成本超支': '政府监察与政策',
            'DAU': '政府监察与政策', '培训（国防）': '政府监察与政策',
            'BBP': '政府监察与政策',
            '人物': '人物',
            'SCARS': '工业与咨询', 'MOATEL': '工业与咨询',
            'PPI': '工业与咨询', 'CAE': '工业与咨询', 'IS4S': '工业与咨询',
            '模拟器': '工业与咨询', '弹药': '工业与咨询', '验证': '工业与咨询', '测试': '工业与咨询',
            '训练': '工业与咨询', '培训': '工业与咨询', '咨询': '工业与咨询',
            'R-EGI': '工业与咨询', 'PNT': '工业与咨询', 'GPS': '工业与咨询',
            'SysML': '人物',
        },
        'comparisons': {
            'MOSA': 'MOSA演化与实施', 'mosa': 'MOSA演化与实施', '模块化': 'MOSA演化与实施',
            'GRA': '标准与架构', 'FACE': '标准与架构', 'SOSA': '标准与架构',
            'C5ISR': '标准与架构', 'CMOSS': '标准与架构', 'VICTORY': '标准与架构',
            '开放架构': '标准与架构', '标准': '标准与架构', '接口': '标准与架构',
            'DoD': '国防采办体系', '国防采办': '国防采办体系', '采办': '国防采办体系',
            '国防': '国防采办体系', '政策': '国防采办体系',
            'MBSE': '系统工程方法', 'SysML': '系统工程方法', 'INCOSE': '系统工程方法',
            '系统工程': '系统工程方法', 'NASA': '系统工程方法', 'NIST': '系统工程方法',
            '数字工程': '数字工程', 'DMM': '数字工程', 'DEE': '数字工程', '平台': '数字工程',
            '中国': '中美对比', '国际化': '中美对比', 'NATO': '中美对比',
            '韧性': '系统特性对比', '赛博弹性': '系统特性对比', '安全性': '系统特性对比',
            '网络安全': '系统特性对比', '弹性': '系统特性对比',
            '对比': '方法论对比',
        },
        'sources': {
            'NDAA': '核心政策与立法', 'USC': '核心政策与立法', '美国法典': '核心政策与立法',
            '法律': '核心政策与立法', '国会': '核心政策与立法', 'HASC': '核心政策与立法',
            'DFARS': '核心政策与立法', '合同': '核心政策与立法', 'OMB': '核心政策与立法',
            '三军': '核心政策与立法', 'BBP': '核心政策与立法',
            'DoDI': '国防部采办条例', 'DODI': '国防部采办条例', 'DoD': '国防部采办条例',
            '采办': '国防部采办条例', '国防采办': '国防部采办条例',
            'AAF': '国防部采办条例', 'MTA': '国防部采办条例', 'MIL-STD': '国防部采办条例',
            'MOSA': 'MOSA实施指南', 'mosa': 'MOSA实施指南', '模块化': 'MOSA实施指南',
            'NAVAIR': 'MOSA实施指南', 'PEO': 'MOSA实施指南', '海军': 'MOSA实施指南',
            'NDIA': 'MOSA实施指南', 'OSJTF': 'MOSA实施指南',
            'FACE': '技术标准与架构', 'SOSA': '技术标准与架构', 'OMS': '技术标准与架构',
            'HOST': '技术标准与架构', 'WOSA': '技术标准与架构', 'VICTORY': '技术标准与架构',
            'CMOSS': '技术标准与架构', 'MORA': '技术标准与架构', 'UAI': '技术标准与架构',
            'STANAG': '技术标准与架构', 'UCS': '技术标准与架构', 'SCARS': '技术标准与架构',
            'SysML': '技术标准与架构', '开放架构': '技术标准与架构', '标准': '技术标准与架构',
            '案例': '实施案例与项目', 'Raider': '实施案例与项目', 'B-21': '实施案例与项目',
            'FLRAA': '实施案例与项目', 'PrSM': '实施案例与项目', 'LTAMDS': '实施案例与项目',
            'SM-6': '实施案例与项目', 'SPY': '实施案例与项目', 'AMDR': '实施案例与项目',
            'SDA': '实施案例与项目', 'PWSA': '实施案例与项目', 'E-Hel': '实施案例与项目',
            'XM30': '实施案例与项目', 'IBCS': '实施案例与项目', '爱国者': '实施案例与项目',
            'GAO': '审查与监督', 'DOT&E': '审查与监督', 'DSB': '审查与监督',
            'CRS': '审查与监督', 'CSIS': '审查与监督', '监察': '审查与监督', '审计': '审查与监督',
            'MBSE': '系统工程与数字工程', 'INCOSE': '系统工程与数字工程',
            '系统工程': '系统工程与数字工程', 'NASA': '系统工程与数字工程',
            '数字工程': '系统工程与数字工程', 'SysML v2': '系统工程与数字工程',
            'NIST': '系统工程与数字工程', 'ISO': '系统工程与数字工程',
            'PPI': '项目管理与需求工程', '需求': '项目管理与需求工程',
            'DID': '项目管理与需求工程', '测试': '项目管理与需求工程',
            '陆军': '产业与市场', '空军': '产业与市场', 'AFMC': '产业与市场',
            'AFRL': '产业与市场', 'AFLCMC': '产业与市场',
            'Defense News': '产业与市场', 'Military': '产业与市场', 'Lockheed': '产业与市场',
            'Northrop': '产业与市场', 'Raytheon': '产业与市场', 'Collins': '产业与市场',
            '学术': '学术与研究', '论文': '学术与研究', 'Purdue': '学术与研究',
            'Shah': '学术与研究', 'IEEE': '学术与研究',
            '中国': '民用与跨域', '华为': '民用与跨域', '大疆': '民用与跨域',
            '鸿蒙': '民用与跨域', '车路云': '民用与跨域', 'WICVC': '民用与跨域',
            '智能网联': '民用与跨域', 'HIMA': '民用与跨域',
        },
    }

    for section in sections:
        section_dir = content_dir / section
        if not section_dir.is_dir():
            continue

        # Collect articles with tags
        articles = []
        for md_file in sorted(section_dir.glob("*.md")):
            if md_file.name == "index.md":
                continue
            title = extract_title(md_file)
            # Extract first tag for grouping
            tags = []
            try:
                content = md_file.read_text(encoding='utf-8')
                fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
                if fm_match:
                    tag_match = re.search(r'^tags:\s*\[(.*?)\]', fm_match.group(1), re.MULTILINE)
                    if tag_match:
                        tags = [t.strip().strip('"').strip("'") for t in tag_match.group(1).split(',')]
            except Exception:
                pass
            articles.append((md_file.stem, title, tags if tags else [md_file.stem]))

        if not articles:
            continue

        # Group by tags
        grouped = {}
        tag_map = category_maps.get(section, {})
        for stem, title, tags in articles:
            category = '其他'
            for tag in tags:
                if tag in tag_map:
                    category = tag_map[tag]
                    break
            if category not in grouped:
                grouped[category] = []
            grouped[category].append((stem, title))

        # Generate index.md
        section_title = section_titles.get(section, section.title())
        desc = section_descs.get(section, '')
        lines = [
            f'---',
            f'title: "{section_title}"',
            f'---',
            f'',
            f'# {section_title}',
            f'',
        ]
        if desc:
            lines.append(f'> {desc}')
            lines.append(f'')
        lines.append(f'共 {len(articles)} 篇文章。')
        lines.append('')

        # Output grouped
        for cat_name in sorted(grouped.keys()):
            if len(grouped) > 1:  # Only show headings if multiple groups
                lines.append(f'## {cat_name}')
                lines.append('')
            for stem, title in sorted(grouped[cat_name], key=lambda x: x[1]):
                lines.append(f'- [{title}]({stem})')
            lines.append('')

        index_path = section_dir / "index.md"
        index_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        grouped_count = len(grouped)
        print(f"  Generated {section}/index.md ({len(articles)} articles, {grouped_count} groups)")


def main():
    # ── YAML integrity pre-check (fail early) ──
    yaml_check = subprocess.run(
        [sys.executable, str(ROOT / "site" / "check-yaml.py")],
        capture_output=True, text=True
    )
    if yaml_check.returncode != 0:
        print("YAML INTEGRITY CHECK FAILED:")
        print(yaml_check.stdout)
        print(yaml_check.stderr)
        sys.exit(1)
    print("YAML integrity check: OK")

    # Clean
    for d in [BUILD_DIR, SITE_OUT]:
        if d.exists():
            shutil.rmtree(d)

    # Copy wiki → content
    shutil.copytree(WIKI_SRC, BUILD_DIR)
    print(f"Copied wiki/ → site/content/")

    # Generate section index pages
    print("Generating section indexes...")
    generate_section_indexes(BUILD_DIR)

    # Use overview.md as homepage
    overview = BUILD_DIR / "概述.md"
    if not overview.exists():
        overview = BUILD_DIR / "overview.md"
    if overview.exists():
        shutil.copy2(overview, BUILD_DIR / "index.md")
        print("Copied overview.md → index.md (homepage)")

    # Build index and convert
    page_index = build_page_index(BUILD_DIR)

    # Also index raw/ files (articles, papers, archive, repo)
    # so [[raw/articles/xxx]] links resolve to the real files
    RAW_SRC = ROOT / "raw"
    if RAW_SRC.exists():
        raw_files = 0
        for md_file in RAW_SRC.rglob("*.md"):
            rel = f"raw/{md_file.relative_to(RAW_SRC)}"
            name = md_file.stem
            page_index[name] = rel
            parent = md_file.relative_to(RAW_SRC).parent
            if parent != Path('.'):
                page_index[f"{parent.as_posix()}/{name}"] = rel
            # raw/articles/xxx → raw/articles/xxx.md
            page_index[f"raw/{md_file.relative_to(RAW_SRC).with_suffix('')}"] = rel
            raw_files += 1
        print(f"Indexed {raw_files} raw/ files")

    print(f"Index: {len(page_index)} pages")

    converted = 0
    total_links = 0
    unresolved = []

    for md_file in sorted(BUILD_DIR.rglob("*.md")):
        content = md_file.read_text(encoding='utf-8')
        if '[[' not in content:
            continue

        link_count = content.count('[[')
        new_content = convert_wiki_links(content, md_file, page_index, BUILD_DIR)

        # Track unresolved links
        remaining = re.findall(r'\[\[([^\]]+)\]\]', new_content)
        for r in remaining:
            unresolved.append((md_file.relative_to(BUILD_DIR), r))

        if new_content != content:
            converted += 1
            total_links += link_count
            md_file.write_text(new_content, encoding='utf-8')

    print(f"Converted {converted} files, {total_links} links")
    if unresolved:
        print(f"Unresolved: {len(unresolved)} links (will be plain links)")

    # Strip .md from regular markdown links to existing pages (MkDocs compatibility)
    md_stripped = 0
    for md_file in BUILD_DIR.rglob("*.md"):
        orig = md_file.read_text(encoding='utf-8')
        new = orig
        for m in re.finditer(r'\[([^\]]+)\]\(([^)]+\.md)\)', orig):
            path = m.group(2)[:-3]  # strip .md
            if (BUILD_DIR / path).with_suffix('.md').exists():
                new = new.replace(m.group(0), f'[{m.group(1)}]({path})')
                md_stripped += 1
        if new != orig:
            md_file.write_text(new, encoding='utf-8')
    if md_stripped:
        print(f"Stripped .md from {md_stripped} regular markdown links")
    # Count before URL-encoding
    encoded_links = 0
    for md_file in BUILD_DIR.rglob("*.md"):
        orig = md_file.read_text(encoding='utf-8')
        new = re.sub(
            r'(\[[^\]]*\]\()([^)]*[\u4e00-\u9fff][^)]*)(\))',
            lambda m: m.group(1) + quote_path(m.group(2)) + m.group(3),
            orig
        )
        if new != orig:
            md_file.write_text(new, encoding='utf-8')
            encoded_links += 1
    if encoded_links:
        print(f"URL-encoded Chinese paths in {encoded_links} files")

    # Create mkdocs.yml for build (paths relative to site/ cwd)
    mkdocs_content = MKDOCS_YML.read_text(encoding='utf-8')
    mkdocs_content = mkdocs_content.replace('docs_dir: site/content', 'docs_dir: content')
    mkdocs_content = mkdocs_content.replace('site_dir: site/build', 'site_dir: build')

    # Filter stale nav entries — remove .md links to pages that don't exist in content/
    config = yaml.safe_load(mkdocs_content)
    skipped_count = 0
    if config and 'nav' in config:
        def filter_nav(items):
            nonlocal skipped_count
            cleaned = []
            for item in items:
                if isinstance(item, dict):
                    filtered = {}
                    for key, val in item.items():
                        if isinstance(val, list):
                            filtered[key] = filter_nav(val)
                        elif isinstance(val, str) and val.endswith('.md'):
                            if (BUILD_DIR / val).exists():
                                filtered[key] = val
                            else:
                                print(f"  - {val}")
                                skipped_count += 1
                        else:
                            filtered[key] = val
                    if filtered:
                        cleaned.append(filtered)
                else:
                    cleaned.append(item)
            return cleaned
        config['nav'] = filter_nav(config['nav'])
        mkdocs_content = yaml.dump(config, allow_unicode=True, default_flow_style=False, sort_keys=False)

    # Write cleaned config to BOTH build dir AND master mkdocs.yml
    if skipped_count:
        print(f"  Removed {skipped_count} stale entries from nav")

        # Update master mkdocs.yml (restore absolute paths)
        master_config = yaml.safe_load(mkdocs_content)
        master_yaml = yaml.dump(master_config, allow_unicode=True, default_flow_style=False, sort_keys=False)
        # Restore original docs_dir/site_dir paths for master
        master_yaml = master_yaml.replace('docs_dir: content', 'docs_dir: site/content')
        master_yaml = master_yaml.replace('site_dir: build', 'site_dir: site/build')
        MKDOCS_YML.write_text(master_yaml, encoding='utf-8')
        print(f"  Updated {MKDOCS_YML}")

    MKDOCS_BUILD_YML.write_text(mkdocs_content, encoding='utf-8')

    # ── Orphan page detection (files in content/ not listed in nav) ──
    # Reverse of stale nav filter — catches pages that exist but have no nav entry
    nav_file_set = set()
    def collect_nav_files(items):
        for item in items:
            if isinstance(item, dict):
                for key, val in item.items():
                    if isinstance(val, list):
                        collect_nav_files(val)
                    elif isinstance(val, str) and val.endswith('.md'):
                        parts = val.rsplit('/', 1)
                        nav_file_set.add(parts[-1] if len(parts) > 1 else val)
            elif isinstance(item, str) and item.endswith('.md'):
                nav_file_set.add(item)
    collect_nav_files(config.get('nav', []))

    orphans = []
    for section in ['topics', 'concepts', 'comparisons', 'entities', 'sources']:
        section_dir = BUILD_DIR / section
        if not section_dir.is_dir():
            continue
        for f in sorted(section_dir.glob('*.md')):
            if f.name == 'index.md':
                continue
            if f.name not in nav_file_set:
                orphans.append(str(f.relative_to(BUILD_DIR)))

    if orphans:
        print(f"  ⚠️  Orphan pages ({len(orphans)}) — exist in content/ but NOT in mkdocs.yml nav:")
        for o in orphans:
            print(f"     - {o}")
        print(f"  Hint: add them to mkdocs.yml or they will 404 on the site")

    # Build
    print("\nBuilding MkDocs site...")
    result = subprocess.run(
        ["mkdocs", "build", "-f", str(MKDOCS_BUILD_YML)],
        capture_output=True, text=True, cwd=str(ROOT / "site")
    )

    if result.returncode != 0:
        print("BUILD FAILED:")
        print(result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr)
        sys.exit(1)

    # Copy static root files (e.g. WeChat verification) to build output
    for f in ROOT.glob("*.txt"):
        if f.name.startswith(".") or f.name == "requirements.txt":
            continue
        shutil.copy2(f, SITE_OUT / f.name)
        print(f"  Copied root file: {f.name}")

    # Symlink individual raw/ .md files that are referenced from wiki pages
    # (avoid symlinking whole raw/ dir which would pull in PDFs >25MB)
    raw_link_root = SITE_OUT / "raw"
    RAW_SRC = ROOT / "raw"
    if RAW_SRC.exists():
        if raw_link_root.exists() or raw_link_root.is_symlink():
            if raw_link_root.is_symlink():
                raw_link_root.unlink()
            else:
                shutil.rmtree(raw_link_root)
        raw_linked = 0
        for md_file in RAW_SRC.rglob("*.md"):
            dst = raw_link_root / md_file.relative_to(RAW_SRC)
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not dst.exists():
                dst.symlink_to(os.path.relpath(md_file, dst.parent))
                raw_linked += 1
        print(f"  Symlinked {raw_linked} raw/*.md files to build output")

    # Count output
    if SITE_OUT.exists():
        file_count = sum(1 for _ in SITE_OUT.rglob("*") if _.is_file())
        size_mb = sum(f.stat().st_size for f in SITE_OUT.rglob("*") if f.is_file()) / 1024 / 1024
        print(f"✓ Site built: {SITE_OUT}")
        print(f"  {file_count} files, {size_mb:.1f} MB")
    else:
        print("ERROR: Build directory not created")
        sys.exit(1)

if __name__ == '__main__':
    main()
