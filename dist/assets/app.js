'use strict';
const cards=[...document.querySelectorAll('.card')];
const search=document.querySelector('#search');
let category='全部';
const normalize=text=>text.toLocaleLowerCase().trim();
function filter(){const query=normalize(search?.value||'');let shown=0;cards.forEach(card=>{const match=(category==='全部'||card.dataset.category===category)&&normalize(card.dataset.search).includes(query);card.hidden=!match;if(match)shown++;});const count=document.querySelector('#result-count');if(count)count.textContent=`顯示 ${shown} 篇筆記`;const empty=document.querySelector('#empty');if(empty)empty.hidden=shown!==0;}
search?.addEventListener('input',filter);
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{category=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));filter();}));
document.querySelectorAll('.quiz').forEach(quiz=>quiz.addEventListener('submit',event=>{event.preventDefault();const selected=quiz.querySelector('input:checked');const output=quiz.querySelector('.feedback');if(!selected){output.textContent='請先選擇一個答案。';return;}const correct=Number(selected.value)===Number(quiz.dataset.answer);output.textContent=(correct?'✓ 答對了！':'✗ 再想一下。')+' '+quiz.dataset.explanation;}));
const storageKey='cs-notes-lab-reviewed-v1';
function readProgress(){try{const value=JSON.parse(localStorage.getItem(storageKey)||'[]');return Array.isArray(value)?value.filter(x=>typeof x==='string'):[];}catch{return [];}}
function updateProgress(){const reviewed=readProgress();document.querySelectorAll('[data-progress]').forEach(label=>{label.textContent=reviewed.includes(label.dataset.progress)?'✓ 已複習':'尚未標記';});const button=document.querySelector('[data-mark]');if(button){const done=reviewed.includes(button.dataset.mark);button.setAttribute('aria-pressed',String(done));button.textContent=done?'✓ 已複習｜取消標記':'標記這篇已複習';}const total=document.querySelector('#review-count');if(total)total.textContent=cards.filter(c=>reviewed.includes(c.dataset.slug)).length;}
document.querySelector('[data-mark]')?.addEventListener('click',event=>{const slug=event.currentTarget.dataset.mark;const reviewed=readProgress();const next=reviewed.includes(slug)?reviewed.filter(x=>x!==slug):[...reviewed,slug];try{localStorage.setItem(storageKey,JSON.stringify(next));updateProgress();}catch{document.querySelector('#storage-status').textContent='此瀏覽器無法儲存複習標記；筆記與測驗仍可使用。';}});
filter();updateProgress();
