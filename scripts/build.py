"""Build static pages. Python standard library only; run from any directory."""
import json, html, pathlib, shutil
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
E=lambda value: html.escape(str(value),quote=True)
def shell(title,body,depth=0):
 p='../'*depth
 return f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="可持續擴充的資科複習筆記：觀念、算例、易錯點與自我測驗。"><title>{E(title)} | CS Notes Lab</title><link rel="stylesheet" href="{p}assets/style.css"><script defer src="{p}assets/app.js"></script></head><body><nav aria-label="主要導覽"><a class="brand" href="{p}index.html"><span class="logo">cs/</span> CS Notes Lab</a><div class="navlinks"><a href="{p}index.html#library">筆記書架</a><a href="{p}rules.html">專案規則 ↗</a></div></nav><main>{body}</main><footer><span>CS Notes Lab · 把知識整理成自己的理解。</span><span>原創學習整理 · AI 協作建置 · 2026</span></footer></body></html>'''
def items(values):return '<ul>'+''.join(f'<li>{E(x)}</li>' for x in values)+'</ul>'
def build():
 if OUT.exists():shutil.rmtree(OUT)
 (OUT/'notes').mkdir(parents=True)
 shutil.copytree(ROOT/'assets',OUT/'assets')
 shutil.copy(ROOT/'AGENTS.md',OUT/'AGENTS.md')
 notes=[json.loads(p.read_text()) for p in sorted((ROOT/'content/notes').glob('*.json'))]
 cards=''
 for i,n in enumerate(notes,1):
  slug=n['slug']; search=' '.join([n['title'],n['category'],n['summary']]+[c['term'] for c in n['concepts']])
  cards+=f'''<article class="card" data-slug="{E(slug)}" data-category="{E(n['category'])}" data-search="{E(search)}"><div class="cardtop"><span class="tag">{E(n['category'])}</span><span>NOTE {i:02d} / {n['minutes']} 分鐘</span></div><h3><a href="notes/{E(slug)}.html">{E(n['title'])}</a></h3><p>{E(n['summary'])}</p><div class="cardfoot"><a href="notes/{E(slug)}.html">開始閱讀 <span aria-hidden="true">↗</span></a><span class="reviewed" data-progress="{E(slug)}">尚未標記</span></div></article>'''
  concepts=''.join(f'<div class="concept"><h3>{E(c["term"])}</h3><p>{E(c["explanation"])}</p></div>' for c in n['concepts'])
  quizzes=''
  for j,q in enumerate(n['quiz']):
   options=''.join(f'<label class="option"><input type="radio" name="q{j}" value="{k}">{E(o)}</label>' for k,o in enumerate(q['options']))
   quizzes+=f'''<form class="quiz" data-answer="{q['answer']}" data-explanation="{E(q['explanation'])}"><fieldset><legend>{j+1}. {E(q['question'])}</legend>{options}</fieldset><button type="submit">檢查答案</button><p class="feedback" role="status"></p><details><summary>查看解析</summary><p>正確答案：{E(q['options'][q['answer']])}。{E(q['explanation'])}</p></details></form>'''
  ex=n['example'];sources=''.join(f'<li><a class="source" href="{E(s["url"])}" target="_blank" rel="noopener noreferrer">{E(s["label"])} ↗</a></li>' for s in n['sources'])
  body=f'''<article class="article"><a class="back" href="../index.html#library">← 返回筆記書架</a><p class="eyebrow">{E(n['category'])} / STUDY NOTE</p><h1>{E(n['title'])}</h1><p class="lead">{E(n['summary'])}</p><p class="articlemeta">約 {n['minutes']} 分鐘 · 更新 {E(n['updated'])}</p><section id="objectives"><h2>01 / 學習目標</h2>{items(n['objectives'])}</section><section id="concepts"><h2>02 / 核心觀念</h2>{concepts}</section><section id="example"><h2>03 / 例題與解析</h2><div class="example"><p><strong>{E(ex['question'])}</strong></p><ol>{''.join('<li>'+E(s)+'</li>' for s in ex['steps'])}</ol><p class="answer">{E(ex['answer'])}</p></div></section><section id="mistakes"><h2>04 / 常見錯誤</h2>{items(n['mistakes'])}</section><section id="quiz"><h2>05 / 自我測驗</h2><p>先作答再查看解析；答錯也能立即釐清觀念。</p>{quizzes}</section><section id="sources"><h2>06 / 參考資料</h2><ul>{sources}</ul><p>本頁為原創教學整理，算例為自行設計，並非教材原題。</p></section><button class="mark" data-mark="{E(slug)}" aria-pressed="false">標記這篇已複習</button><p id="storage-status" role="status">複習標記僅儲存在本瀏覽器，不會同步到其他裝置。</p></article>'''
  (OUT/'notes'/f'{slug}.html').write_text(shell(n['title'],body,1))
 filters=''.join(f'<button type="button" data-filter="{x}" aria-pressed="{str(i==0).lower()}">{x}</button>' for i,x in enumerate(['全部','記憶體','計算機組織','作業系統']))
 body=f'''<section class="hero"><div><p class="eyebrow">A SMALL LIBRARY FOR BIG IDEAS</p><h1>把資科觀念，<br>慢慢變成<em>直覺。</em></h1><p class="intro">從「好像懂了」到真正說得清楚。<br>每篇一個觀念，一道算例，再用兩題測驗確認理解。</p><a class="cta" href="#library">翻開筆記書架 ↓</a></div><div class="board" aria-label="學習流程示意"><div class="boardhead"><span>THE LEARNING STACK</span><span>01 → 03</span></div><div class="stack"><div>理解觀念 <span>understand</span></div><div>動手算一次 <span>practice</span></div><div>說明為什麼 <span>explain ✓</span></div></div><p>不只是收集答案，也把推理過程留下來。</p></div></section><div class="metrics"><div><b>{len(notes):02d}</b><span>篇主題筆記</span></div><div><b>{sum(len(n['quiz']) for n in notes):02d}</b><span>道自我測驗</span></div><div><b id="review-count">0</b><span>篇已複習 · 本機記錄</span></div></div><section id="library"><div class="sectionhead"><div><p class="eyebrow">YOUR KNOWLEDGE SHELF</p><h2>今天想弄懂什麼？</h2></div><div class="search"><label class="sr-only" for="search">搜尋筆記標題、主題或關鍵字</label><input id="search" type="search" placeholder="搜尋觀念，例如 TLB、位址、管線…"></div></div><div class="filters" aria-label="依主題篩選">{filters}</div><p id="result-count" role="status">顯示 {len(notes)} 篇筆記</p><div class="cards">{cards}</div><p id="empty" class="empty" hidden>沒有符合條件的筆記。試試其他關鍵字，或切回「全部」。</p></section><section class="system"><div><p class="eyebrow">BUILT TO KEEP GROWING</p><h2>筆記可以增加，<br>整理方式保持一致。</h2><p>每篇內容都遵守同一份專案手冊。新增主題時，AI 只需依範本填寫內容，就能延伸出相同結構的頁面。</p><a href="rules.html">閱讀專案規則與擴充方式 ↗</a></div><div class="workflow"><div><b>01</b>讀 AGENTS.md，理解交付與限制</div><div><b>02</b>新增 JSON：觀念、算例、錯誤、測驗</div><div><b>03</b>建置與驗證，產生一致的網頁</div></div></section>'''
 (OUT/'index.html').write_text(shell('資科學習筆記',body))
 rules=(ROOT/'AGENTS.md').read_text()
 body=f'''<article class="article"><a class="back" href="index.html">← 返回首頁</a><p class="eyebrow">THE PROJECT HANDBOOK</p><h1>讓下一次新增，<br>有規則可循。</h1><p class="lead">這份手冊不是對網頁外觀的模糊描述，而是 AI 可以實際執行的工作契約。</p><div class="example"><h2>怎麼驗證延伸能力？</h2><p>先完成分頁、TLB、管線三篇，再依相同 schema 新增「死結」筆記。共用版型不變，首頁卡片、詳細頁與測驗由建置程式自動產生。</p><p><a class="source" href="AGENTS.md" download>下載完整 AGENTS.md</a></p></div><h2>AGENTS.md 完整內容</h2><pre>{E(rules)}</pre></article>'''
 (OUT/'rules.html').write_text(shell('專案規則',body))
 print(f'Built {len(notes)} notes, {len(notes)+2} HTML pages, {sum(len(n["quiz"]) for n in notes)} quiz questions.')
if __name__=='__main__':build()
