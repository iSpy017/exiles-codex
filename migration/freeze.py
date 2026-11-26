import json,hashlib,sys,os,pathlib
src,out=sys.argv[1],sys.argv[2]
d=json.load(open(src,encoding='utf-8'))
root=pathlib.Path(out); man=[]
for x in d['docs']:
    p=root/'legacy'/x['file_name']; p.parent.mkdir(parents=True,exist_ok=True)
    b=x['content'].encode('utf-8'); p.write_bytes(b)
    man.append(dict(path=x['file_name'],uuid=x['uuid'],created_at=x['created_at'],chars=len(x['content']),est_tokens=x['estimated_token_count'],sha256=hashlib.sha256(b).hexdigest()))
man.sort(key=lambda m:m['path'])
json.dump(dict(exported_at=d['exported_at'],source='claude.ai project '+d['project'],count=len(man),docs=man),open(root/'legacy'/'MANIFEST.json','w'),indent=1)
# verify
bad=[m for m in man if hashlib.sha256((root/'legacy'/m['path']).read_bytes()).hexdigest()!=m['sha256']]
print(len(man),'docs; hash mismatches:',len(bad),'; total chars',sum(m['chars'] for m in man))
