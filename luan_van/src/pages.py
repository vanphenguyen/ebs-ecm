import json,subprocess,sys,re
pdf,tocf=sys.argv[1],sys.argv[2]
n=int(re.search(r'Pages:\s+(\d+)',subprocess.run(['pdfinfo',pdf],capture_output=True,text=True).stdout).group(1))
texts=[re.sub(r'\s+',' ',subprocess.run(['pdftotext','-f',str(i),'-l',str(i),'-layout',pdf,'-'],capture_output=True,text=True).stdout) for i in range(1,n+1)]
toc=json.load(open(tocf)); res={}; start=3
for name,t in toc:
    key=re.sub(r'\s+',' ',t)[:35]
    for i in range(start,n+1):
        if key in texts[i-1]: res[name]=i-1; start=i; break
    else: print('MISSING',t)
print(json.dumps(res)); 
