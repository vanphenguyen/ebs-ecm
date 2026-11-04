import re, sys
from xml.sax.saxutils import escape
SRC=sys.argv[1]
x=open(SRC,encoding='utf8').read()
b=x.find('<w:body>')
head,body=x[:b],x[b:]
items=[m for m in re.finditer(r'<w:p[ >].*?</w:p>|<w:tbl>.*?</w:tbl>',body,re.S)]

FONT='<w:rFonts w:asciiTheme="majorHAnsi" w:hAnsiTheme="majorHAnsi" w:cstheme="majorHAnsi"/>'
def runs(text,bold=False,italic=False):
    out=[]
    for k,seg in enumerate(re.split(r'\*\*',text)):
        if not seg: continue
        bb = bold or (k%2==1)
        rpr=FONT+('<w:b/><w:bCs/>' if bb else '')+('<w:i/><w:iCs/>' if italic else '')+'<w:sz w:val="26"/><w:szCs w:val="26"/><w:lang w:val="vi-VN"/>'
        out.append(f'<w:r><w:rPr>{rpr}</w:rPr><w:t xml:space="preserve">{escape(seg)}</w:t></w:r>')
    return ''.join(out)
def P(text,kind='body',bold=False,italic=False,jc='both'):
    ind={'body':'<w:ind w:firstLine="426"/>','h':'','bullet':'<w:ind w:left="709" w:hanging="283"/>',
         'bullet2':'<w:ind w:left="1134" w:hanging="283"/>','ref':'<w:ind w:left="567" w:hanging="567"/>','cell':''}[kind]
    sp='<w:spacing w:before="60" w:after="60" w:line="276" w:lineRule="auto"/>' if kind!='cell' else '<w:spacing w:before="40" w:after="40" w:line="264" w:lineRule="auto"/>'
    if kind=='bullet': text='- '+text
    if kind=='bullet2': text='+ '+text
    if kind=='h': bold=True
    return f'<w:p><w:pPr>{sp}{ind}<w:jc w:val="{jc}"/><w:rPr>{FONT}<w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr></w:pPr>{runs(text,bold,italic)}</w:p>'
def blocks(spec):
    """spec: list of strings with prefixes: '# ' heading, '- ' bullet, '+ ' bullet2, '[n] ' ref, else body"""
    out=[]
    for s in spec:
        if s.startswith('# '): out.append(P(s[2:],'h'))
        elif s.startswith('## '): out.append(P(s[3:],'h',italic=True))
        elif s.startswith('- '): out.append(P(s[2:],'bullet'))
        elif s.startswith('+ '): out.append(P(s[2:],'bullet2'))
        elif re.match(r'\[\d+\] ',s): out.append(P(s,'ref'))
        else: out.append(P(s))
    return ''.join(out)

def set_text(xml,new):  # replace whole paragraph text keeping first run formatting
    rs=re.findall(r'<w:r>.*?</w:r>|<w:r [^>]*>.*?</w:r>',xml,re.S)
    first=rs[0]; nr=re.sub(r'<w:t[^>]*>[^<]*</w:t>','<w:t xml:space="preserve">'+escape(new)+'</w:t>',first,count=1)
    s=xml.find(rs[0]); e=xml.rfind(rs[-1])+len(rs[-1])
    return xml[:s]+nr+xml[e:]

def cell_fill(tc,paras):
    i=tc.find('<w:p '); j=tc.rfind('</w:p>')+6
    if i<0: i=tc.find('<w:p>')
    return tc[:i]+''.join(paras)+tc[j:]
def C(text,bold=False,italic=False,jc='left'):
    return [P(t,'cell',bold,italic,jc) for t in text.split('\n')]

import content as K
rep={}   # index -> replacement xml
after={} # index -> xml appended after
it=lambda i: items[i].group(0)

rep[3]=set_text(it(3),'Tên đề tài: '+K.TITLE)
rep[4]=set_text(it(4),'Tổ chức chủ trì: '+K.ORG)
rep[5]=set_text(it(5),'Chủ nhiệm đề tài: '+K.PI)
rep[6]=set_text(it(6),'Thời gian thực hiện đề tài: '+K.MONTHS+' tháng.')
rep[9]=blocks(K.ABSTRACT)
rep[10]=P('Từ khóa: '+K.KEYWORDS,'body',italic=True)
rep[16]=blocks(K.S21)
after[19]=blocks(K.S22)
rep[22]=blocks(K.S3)
after[25]=blocks(K.S4)
rep[28]=blocks(K.S4_EXPERT)
rep[30]=blocks(K.S4_ACT)
after[32]=blocks(K.S5_SUCCESS)
after[33]=blocks(K.S5_SOTA)
after[34]=blocks(K.S5_POT)
after[35]=blocks(K.S5_CAP)
after[36]=blocks(K.S5_FAC)
after[44]=blocks(K.S71)
rep[50]=blocks(K.S73)
rep[51]=set_text(it(51),'7.4 Khả năng ứng dụng kết quả nghiên cứu, phương thức chuyển giao và địa chỉ ứng dụng (Đối với đề tài Đột xuất, Tiềm năng):')+blocks(K.S74)

def rows_of(t): return re.findall(r'<w:tr[ >].*?</w:tr>',t,re.S)
def cells_of(r): return re.findall(r'<w:tc>.*?</w:tc>',r,re.S)
def fill_row(r,vals):
    cs=cells_of(r); out=r
    for c,v in zip(cs,vals):
        if v is None: continue
        out=out.replace(c,cell_fill(c,v),1)
    return out

# Equipment table (37)
t=it(37); rs=rows_of(t); tpl=rs[1]
new=[fill_row(tpl,[C(str(n+1),jc='center')]+[C(a) for a in row]) for n,row in enumerate(K.EQUIP)]
rep[37]=t.replace(rs[1]+rs[2],''.join(new)) if rs[1]+rs[2] in t else t
assert rep[37]!=t
# Plan table (40)
t=it(40); rs=rows_of(t); tplH=rs[1]; tplW=rs[2]
new=[]
for stt,task,time,who,res in K.PLAN:
    main='.' not in stt
    new.append(fill_row(tplH if main else tplW,[C(stt,bold=main,jc='center'),C(task,bold=main,italic=not main),C(time,jc='center'),C(who),C(res)]))
body_rows=''.join(rs[1:])
s=t.find(rs[1]); e=t.rfind(rs[-1])+len(rs[-1])
rep[40]=t[:s]+''.join(new)+t[e:]
# Publication table (47)
t=it(47); rs=rows_of(t); out=t
for k,(qty,note) in K.PUB.items():
    r=rs[k]; out=out.replace(r,fill_row(r,[None,None,C(qty,jc='center'),C(note)]),1)
rep[47]=out
# Funding table (54)
t=it(54); rs=rows_of(t); out=t
for k in (2,5,8):
    r=rs[k]; out=out.replace(r,fill_row(r,[None,C(K.FUND_NONE),C('-',jc='center'),C('-',jc='center'),C('-',jc='center')]),1)
rep[54]=out

# assemble
pieces=[];last=0
for i,m in enumerate(items):
    pieces.append(body[last:m.start()])
    pieces.append(rep.get(i,m.group(0)))
    if i in after: pieces.append(after[i])
    last=m.end()
pieces.append(body[last:])
open(SRC,'w',encoding='utf8').write(head+''.join(pieces))
print('ok')
