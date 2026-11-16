"""Validate the content contract and generated internal links, without dependencies."""
import json,pathlib,re,datetime
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
ROOT=pathlib.Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
def run():
 files=sorted((ROOT/'content/notes').glob('*.json'));assert files,'No content'
 slugs=set();questions=0
 for file in files:
  n=json.loads(file.read_text()); required={'slug','title','category','summary','minutes','updated','objectives','concepts','example','mistakes','quiz','sources'}
  assert required<=n.keys(),f'{file}: missing fields'
  assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',n['slug']) and n['slug']==file.stem
  assert n['slug'] not in slugs;slugs.add(n['slug'])
  assert n['category'] in {'記憶體','計算機組織','作業系統'}
  assert type(n['minutes'])==int and n['minutes']>0
  datetime.date.fromisoformat(n['updated'])
  for k in ['title','summary']:assert isinstance(n[k],str) and n[k].strip()
  for k in ['objectives','mistakes']:assert len(n[k])>=2 and all(isinstance(s,str) and s.strip() for s in n[k])
  assert len(n['concepts'])>=2 and all(c.get('term') and c.get('explanation') for c in n['concepts'])
  ex=n['example'];assert ex.get('question') and ex.get('answer') and len(ex['steps'])>=2 and all(ex['steps'])
  assert len(n['quiz'])>=2
  for q in n['quiz']:
   assert q['question'] and q['explanation'];assert len(q['options'])==4 and len(set(q['options']))==4 and all(q['options']);assert type(q['answer'])==int and 0<=q['answer']<4;questions+=1
  assert n['sources'] and all(s['label'] and s['url'].startswith('https://') for s in n['sources'])
 pages={}
 for file in (ROOT/'dist').rglob('*.html'):
  p=Page();p.feed(file.read_text());pages[file.resolve()]=p
 for file,p in pages.items():
  for link in p.links:
   u=urlparse(link)
   if u.scheme or u.netloc:continue
   path=(file.parent/unquote(u.path)).resolve() if u.path else file
   assert path.is_relative_to((ROOT/'dist').resolve()),f'Outside dist: {link}'
   assert path.exists(),f'Broken link {file}: {link}'
   if u.fragment:assert unquote(u.fragment) in pages[path].ids,f'Missing anchor: {link}'
 for slug in slugs:
  path=(ROOT/'dist/notes'/f'{slug}.html').resolve()
  assert {'objectives','concepts','example','mistakes','quiz','sources'}<=pages[path].ids
  assert f'notes/{slug}.html' in (ROOT/'dist/index.html').read_text()
 assert (ROOT/'dist/AGENTS.md').read_bytes()==(ROOT/'AGENTS.md').read_bytes()
 print(f'PASS: {len(slugs)} notes, {questions} questions, {len(pages)} pages; schema, section order targets, internal links and AGENTS copy valid.')
if __name__=='__main__':run()
