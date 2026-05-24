"""Wiki doc config — category maps, section settings, title/tag extraction, index & nav generation.

Single source of truth for tag→category mappings used by both index pages and mkdocs nav.
"""
from __future__ import annotations

import re
from pathlib import Path


_SECTION_CFG = {
    'titles': {
        'topics': '主题',
        'concepts': '概念',
        'comparisons': '对比',
        'entities': '实体',
        'sources': '来源',
    },
    'descs': {
        'topics': '综合多来源的主题深度文章',
        'concepts': '独立概念释义',
        'comparisons': '跨领域对比分析',
        'entities': '人物、组织与政策实体',
        'sources': '原始来源摘要与引用',
    },
    'category_maps': {
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
            'CCF': '采办与国防', '成本超支': '采办与国防', '国防': '采办与国防',
            'CCA': '作战概念', '软件定义能力': '作战概念',
            'modularity': 'MOSA基础', 'architecture': 'MOSA基础', 'patterns': 'MOSA基础',
            'defense': '采办与国防', 'cross-domain': 'MOSA基础',
            '韧性': '系统属性', '安全': '系统属性', '弹性': '系统属性',
            '赛博弹性': '系统属性', '网络安全': '系统属性',
        },
        'entities': {
            '美国国防部': '国防部及军种', 'DoD': '国防部及军种', 'OUSD': '国防部及军种',
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
            '国防科技': '防务承包商', '无人机': '防务承包商', '无人系统': '防务承包商',
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
            '立法': '核心政策与立法', '公法': '核心政策与立法',
            '国防预算': '核心政策与立法', '政策': '核心政策与立法',
            'DoDI': '国防部采办条例', 'DODI': '国防部采办条例', 'DoD': '国防部采办条例',
            '采办': '国防部采办条例', '国防采办': '国防部采办条例',
            'AAF': '国防部采办条例', 'MTA': '国防部采办条例', 'MIL-STD': '国防部采办条例',
            '采办路径': '国防部采办条例', '采办改革': '国防部采办条例', 'MDAP': '国防部采办条例',
            'MOSA': 'MOSA实施指南', 'mosa': 'MOSA实施指南', '模块化': 'MOSA实施指南',
            'NAVAIR': 'MOSA实施指南', 'PEO': 'MOSA实施指南', '海军': 'MOSA实施指南',
            'NDIA': 'MOSA实施指南', 'OSJTF': 'MOSA实施指南',
            'MOSA案例': 'MOSA实施指南', '实施指南': 'MOSA实施指南',
            'FACE': '技术标准与架构', 'SOSA': '技术标准与架构', 'OMS': '技术标准与架构',
            'HOST': '技术标准与架构', 'WOSA': '技术标准与架构', 'VICTORY': '技术标准与架构',
            'CMOSS': '技术标准与架构', 'MORA': '技术标准与架构', 'UAI': '技术标准与架构',
            'STANAG': '技术标准与架构', 'UCS': '技术标准与架构', 'SCARS': '技术标准与架构',
            'SysML': '技术标准与架构', '开放架构': '技术标准与架构', '标准': '技术标准与架构',
            '航电': '技术标准与架构', '开放系统': '技术标准与架构', '互操作性': '技术标准与架构',
            '雷达': '技术标准与架构', '电子战': '技术标准与架构', '标准化': '技术标准与架构',
            '防空反导': '技术标准与架构', '开放标准': '技术标准与架构', '硬件标准': '技术标准与架构',
            '传感器': '技术标准与架构', '控制器': '技术标准与架构', '武器接口': '技术标准与架构',
            'PNT': '技术标准与架构', 'ICBM': '技术标准与架构', 'VITA': '技术标准与架构',
            'OpenVPX': '技术标准与架构', '接口': '技术标准与架构',
            '案例': '实施案例与项目', 'Raider': '实施案例与项目', 'B-21': '实施案例与项目',
            'FLRAA': '实施案例与项目', 'PrSM': '实施案例与项目', 'LTAMDS': '实施案例与项目',
            'SM-6': '实施案例与项目', 'SPY': '实施案例与项目', 'AMDR': '实施案例与项目',
            'SDA': '实施案例与项目', 'PWSA': '实施案例与项目', 'E-Hel': '实施案例与项目',
            'XM30': '实施案例与项目', 'IBCS': '实施案例与项目', '爱国者': '实施案例与项目',
            'IAMD': '实施案例与项目', 'Aegis': '实施案例与项目',
            'SPY-6': '实施案例与项目', 'Sentinel': '实施案例与项目',
            'CCA': '实施案例与项目', 'R-EGI': '实施案例与项目',
            'GAO': '审查与监督', 'DOT&E': '审查与监督', 'DSB': '审查与监督',
            'CRS': '审查与监督', 'CSIS': '审查与监督', '监察': '审查与监督', '审计': '审查与监督',
            '测试评估': '审查与监督', '采办报告': '审查与监督',
            'MBSE': '系统工程与数字工程', 'INCOSE': '系统工程与数字工程',
            '系统工程': '系统工程与数字工程', 'NASA': '系统工程与数字工程',
            '数字工程': '系统工程与数字工程', 'SysML v2': '系统工程与数字工程',
            'NIST': '系统工程与数字工程', 'ISO': '系统工程与数字工程',
            '数字孪生': '系统工程与数字工程', '数字化转型': '系统工程与数字工程',
            '建模与仿真': '系统工程与数字工程', '手册': '系统工程与数字工程',
            '验证': '系统工程与数字工程', 'M&S': '系统工程与数字工程',
            '模型驱动': '系统工程与数字工程', '方法论': '系统工程与数字工程',
            'PPI': '项目管理与需求工程', '需求': '项目管理与需求工程',
            'DID': '项目管理与需求工程', '测试': '项目管理与需求工程',
            '需求工程': '项目管理与需求工程', '武器系统': '项目管理与需求工程',
            '数据权利': '项目管理与需求工程', '数据权': '项目管理与需求工程',
            '项目管理': '项目管理与需求工程', '投资回报': '项目管理与需求工程',
            '陆军': '产业与市场', '空军': '产业与市场', 'AFMC': '产业与市场',
            'AFRL': '产业与市场', 'AFLCMC': '产业与市场',
            'Defense News': '产业与市场', 'Military': '产业与市场', 'Lockheed': '产业与市场',
            'Northrop': '产业与市场', 'Raytheon': '产业与市场', 'Collins': '产业与市场',
            '国防工业': '产业与市场', '模拟器': '产业与市场', '训练': '产业与市场',
            '无人机': '产业与市场', '导弹': '产业与市场', '导航': '产业与市场',
            '军售': '产业与市场',
            '学术': '学术与研究', '论文': '学术与研究', 'Purdue': '学术与研究',
            'Shah': '学术与研究', 'IEEE': '学术与研究',
            'CMU': '学术与研究', 'SEI': '学术与研究',
            '中国': '民用与跨域', '华为': '民用与跨域', '大疆': '民用与跨域',
            '鸿蒙': '民用与跨域', '车路云': '民用与跨域', 'WICVC': '民用与跨域',
            '智能网联': '民用与跨域', 'HIMA': '民用与跨域',
            'NATO': '民用与跨域', '智能座舱': '民用与跨域',
            '智能网联汽车': '民用与跨域', '车辆': '民用与跨域',
        },
    },
}
SECTIONS = ['topics', 'concepts', 'comparisons', 'entities', 'sources']


def extract_title(md_file: Path) -> str:
    """Extract first # heading from a markdown file, falling back to filename."""
    try:
        content = md_file.read_text(encoding='utf-8')
        # Skip YAML frontmatter
        body = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, count=1, flags=re.DOTALL)
        heading = re.search(r'^#\s+(.+)', body, re.MULTILINE)
        if heading:
            return heading.group(1).strip()
    except Exception:
        pass
    return md_file.stem


def extract_tags(md_file: Path) -> list:
    """Extract tags list from YAML frontmatter."""
    try:
        content = md_file.read_text(encoding='utf-8')
        fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if fm_match:
            tag_match = re.search(r'^tags:\s*\[(.*?)\]', fm_match.group(1), re.MULTILINE)
            if tag_match:
                return [t.strip().strip('"').strip("'") for t in tag_match.group(1).split(',')]
    except Exception:
        pass
    return []


def generate_section_indexes(content_dir: Path, section_cfg: dict = None):
    """Auto-generate index.md for each section directory with tag-based grouping."""
    if section_cfg is None:
        section_cfg = _SECTION_CFG
    section_titles = section_cfg['titles']
    section_descs = section_cfg['descs']
    category_maps = section_cfg['category_maps']

    for section in SECTIONS:
        section_dir = content_dir / section
        if not section_dir.is_dir():
            continue

        articles = []
        for md_file in sorted(section_dir.glob("*.md")):
            if md_file.name == "index.md":
                continue
            title = extract_title(md_file)
            tags = extract_tags(md_file)
            articles.append((md_file.stem, title, tags if tags else [md_file.stem]))

        if not articles:
            continue

        tag_map = category_maps.get(section, {})
        grouped = {}
        for stem, title, tags in articles:
            category = '其他'
            for tag in tags:
                if tag in tag_map:
                    category = tag_map[tag]
                    break
            if category not in grouped:
                grouped[category] = []
            grouped[category].append((stem, title))

        section_title = section_titles.get(section, section.title())
        desc = section_descs.get(section, '')
        lines = [
            '---',
            f'title: "{section_title}"',
            '---',
            '',
            f'# {section_title}',
            '',
        ]
        if desc:
            lines.append(f'> {desc}')
            lines.append('')
        lines.append(f'共 {len(articles)} 篇文章。')
        lines.append('')

        for cat_name in sorted(grouped.keys()):
            if len(grouped) > 1:
                lines.append(f'## {cat_name}')
                lines.append('')
            for stem, title in sorted(grouped[cat_name], key=lambda x: x[1]):
                lines.append(f'- [{title}]({stem})')
            lines.append('')

        index_path = section_dir / "index.md"
        index_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
        grouped_count = len(grouped)
        print(f"  Generated {section}/index.md ({len(articles)} articles, {grouped_count} groups)")


def generate_nav(content_dir: Path, section_cfg: dict) -> list:
    """Auto-generate mkdocs nav from filesystem + YAML frontmatter + tag category maps.

    Returns nav list compatible with mkdocs.yml format.
    Replaces the manual 278-line nav section in mkdocs.yml.
    """
    section_titles = section_cfg['titles']
    category_maps = section_cfg['category_maps']

    nav = [{'首页': '概述.md'}]

    for section in SECTIONS:
        section_dir = content_dir / section
        if not section_dir.is_dir():
            continue

        # Collect pages with tags
        articles = []
        for md_file in sorted(section_dir.glob("*.md")):
            if md_file.name == "index.md":
                continue
            title = extract_title(md_file)
            tags = extract_tags(md_file)
            articles.append((md_file.name, title, tags))

        if not articles:
            continue

        # Group by tag category (same maps as generate_section_indexes)
        tag_map = category_maps.get(section, {})
        grouped = {}
        for filename, title, tags in articles:
            category = '其他'
            for tag in tags:
                if tag in tag_map:
                    category = tag_map[tag]
                    break
            grouped.setdefault(category, []).append((title, filename))

        # Build section nav structure
        section_items = [f"{section}/index.md"]
        for cat_name in sorted(grouped.keys()):
            if len(grouped) > 1:
                sub_items = []
                for title, filename in sorted(grouped[cat_name], key=lambda x: x[0]):
                    sub_items.append({title: f"{section}/{filename}"})
                section_items.append({cat_name: sub_items})
            else:
                for title, filename in sorted(grouped[cat_name], key=lambda x: x[0]):
                    section_items.append({title: f"{section}/{filename}"})

        nav.append({section_titles[section]: section_items})

    return nav
