"""Build compact bilingual analysis views from the research dataset."""
import json,html
from pathlib import Path
from collections import Counter
from urllib.parse import urlencode
R=Path(__file__).resolve().parents[1]
def build():
 d=json.loads((R/'data/papers.json').read_text());papers=d['papers'];e=html.escape
 labels={'gaze':'注视','blink':'眨眼','eye-closure':'闭眼','pursuit':'追随','pupil':'瞳孔','action':'动作与状态变化','movement':'移动','selection':'选择与确认','social':'社交与共享视线','adaptation':'自适应','aiming':'瞄准','guidance':'引导'}
 coded=sum(bool(p.get('interaction_roles')) for p in papers)
 statuses=Counter(p.get('evidence_status') for p in papers);full=statuses['full_text_assessed'];provisional=statuses['abstract_html_provisional'];remaining=len(papers)-full-provisional
 for en in (False,True):
  t=lambda zh,eng:eng if en else zh;b='../' if en else '';out=R/'en' if en else R
  def bars(key):
   c=Counter(p[key] for p in papers);maximum=max(c.values());rows=[]
   for label,n in (sorted(c.items(),reverse=True) if key=='year' else c.most_common()):
    name=str(label) if en or key=='year' else d['topics'][label]
    query=urlencode({key:label})
    rows.append(f'<a class="bar" href="research.html?{query}"><span>{e(name)}</span><i style="--fill:{n/maximum*100:.2f}%" aria-hidden="true"></i><b>{n}</b></a>')
   return ''.join(rows)
  def groups(key):
   c=Counter(v for p in papers for v in p.get(key,[]));rows=[]
   for value,n in c.most_common():
    name=value.replace('-',' ').title() if en else labels[value]
    links=''.join(f'<li><a href="research.html#{e(p["id"])}">{e(p["title"])}</a></li>' for p in papers if value in p.get(key,[]))
    rows.append(f'<details class="group"><summary>{e(name)} <b>{n}</b></summary><ul>{links}</ul></details>')
   return ''.join(rows)
  s=f'''<!doctype html><html lang="{'en' if en else 'zh-CN'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Analysis · Gaze Atlas</title><link rel="stylesheet" href="{b}style.css"><link rel="stylesheet" href="{b}analysis.css"></head><body><header><a class="brand" href="./">◉ GAZE ATLAS</a><nav aria-label="{t('主导航','Main navigation')}"><a href="./">{t('游戏库','Games')}</a><a href="research.html">{t('研究论文','Research')}</a><a href="analysis.html" aria-current="page">{t('研究分析','Analysis')}</a></nav></header><main class="analysis"><p class="eyebrow">RESEARCH / ANALYSIS</p><h1>{t('研究一览','Research at a glance.')}</h1><p class="intro">{t('从年份、主题与交互机制探索本库文献。点击图表查看论文。','Explore this collection by year, topic and interaction. Select a chart row to browse its papers.')}</p><div class="stats"><div><strong>{len(papers)}</strong>{t('篇文献','publications')}</div><div><strong>{min(p['year'] for p in papers)}–{max(p['year'] for p in papers)}</strong>{t('发表年份','publication years')}</div><div><strong>{coded}/{len(papers)}</strong>{t('已编码交互机制','interaction-coded records')}</div></div><div class="analysis-grid"><section><h2>{t('研究主题','Topics')}</h2><p>{t('每篇文献归入一个主题。','One primary topic per publication.')}</p>{bars('topic')}</section><section><h2>{t('发表年份','Publication years')}</h2><p>{t('本库各年份的收录数量。','Publications represented in this collection.')}</p>{bars('year')}</section><section><h2>{t('眼部信号','Eye signals')}</h2><p>{t(f'基于 {coded} 篇已编码文献，可多选；展开查看论文。',f'Across {coded} coded records; multiple labels per paper. Expand to explore.')}</p>{groups('eye_signals')}</section><section><h2>{t('交互机制','Interaction roles')}</h2><p>{t(f'基于 {coded} 篇已编码文献，可多选；展开查看论文。',f'Across {coded} coded records; multiple labels per paper. Expand to explore.')}</p>{groups('interaction_roles')}</section></div><aside><h2>{t('数据覆盖','Coverage')}</h2><p>{t(f'统计描述本库的收录分布。交互编码覆盖 {coded} 篇，其余 {len(papers)-coded} 篇待补充。贡献者的证据记录包含 {full} 篇全文评估、{provisional} 篇摘要／HTML 初步收录；其余 {remaining} 篇沿用原有来源核查记录。',f'Counts describe this collection. Interaction coding covers {coded} publications, with {len(papers)-coded} awaiting coding. Contributor evidence records label {full} publications as full-text assessed and {provisional} as abstract/HTML provisional; {remaining} retain their earlier source-verification records.')}</p><a href="{b}data/papers.json">{t('下载开放数据','Download open data')} ↗</a></aside></main><footer>GAZE ATLAS · {e(d['updated_at'])}</footer></body></html>'''
  (out/'analysis.html').write_text(s)
if __name__=='__main__':build()
