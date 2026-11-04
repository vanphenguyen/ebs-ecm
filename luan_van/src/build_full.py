import re, sys, json
from xml.sax.saxutils import escape
sys.path.insert(0, sys.argv[2])
import full_content as K
DOC=sys.argv[1]; PAGES=json.loads(sys.argv[3]) if len(sys.argv)>3 else {}
x=open(DOC,encoding='utf8').read()
b=x.find('<w:body>')+len('<w:body>')
head=x[:b]; body=x[b:]
sect=re.findall(r'<w:sectPr.*?</w:sectPr>',body,re.S)[-1]
cover=re.search(r'<w:tbl>.*?</w:tbl>',body,re.S).group(0)

def sub_t(s,old,new):
    o='>'+escape(old)+'<'; assert o in s, old; return s.replace(o,'>'+escape(new)+'<',1)
cover=sub_t(cover,'BÀI TIỂU LUẬN ','THUYẾT MINH ĐỀ TÀI NGHIÊN CỨU')
cover=sub_t(cover,'DỮ LIỆU LỚN','')
cover=sub_t(cover,'BÀI TOÁN PHÂN LỚP QUY MÔ LỚN VỚI APACHE SPARK VÀ MLLIB: HƯỚNG DẪN KỸ THUẬT TOÀN DIỆN',K.TITLE.upper())
cover=sub_t(cover,'Nguyễn Ngọc Điệp','Đỗ Trung Anh')
cover=sub_t(cover,'   Học viên: Nghiêm Quốc Việt','   Học viên: Nguyễn Văn Phê')
cover=sub_t(cover,' – ',' - ')
cover=sub_t(cover,'B24CHHT100','B26CHHT080')
cover=sub_t(cover,'M24CQHT02-B','..........')
cover=sub_t(cover,'Hà Nội - 2025','Hà Nội - 2026')
ps=re.findall(r'<w:p[ >].*?</w:p>',cover,re.S)
empty=re.sub(r'<w:r[ >].*?</w:r>','',ps[12])
for p in ps:
    t=''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p))
    if 'Đàm Văn Trung' in t or 'Mai Việt Hùng' in t: cover=cover.replace(p,empty,1)

F='<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>'
def rpr(sz=26,b=False,i=False): return f'<w:rPr>{F}{"<w:b/><w:bCs/>" if b else ""}{"<w:i/><w:iCs/>" if i else ""}<w:color w:val="000000"/><w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/><w:lang w:val="vi-VN"/></w:rPr>'
def run(t,**k): return f'<w:r>{rpr(**k)}<w:t xml:space="preserve">{escape(t)}</w:t></w:r>'
def para(content,jc='both',ind='',before=0,after=100,line=312,style='',keep=False,extra=''):
    st=f'<w:pStyle w:val="{style}"/>' if style else ''
    return f'<w:p><w:pPr>{st}{"<w:keepNext/>" if keep else ""}<w:spacing w:before="{before}" w:after="{after}" w:line="{line}" w:lineRule="auto"/>{ind}<w:jc w:val="{jc}"/>{extra}</w:pPr>{content}</w:p>'
def P(t): return para(run(t),ind='<w:ind w:firstLine="567"/>')
def BL(t): return para(run('- '+t),ind='<w:ind w:left="567" w:hanging="284"/>')
bm=[0]
def H(t,lvl):
    bm[0]+=1; name=f'_Toc9000{bm[0]:03d}'
    sz={1:28,2:26,3:26}[lvl]; it= lvl==3
    c=f'<w:bookmarkStart w:id="{900+bm[0]}" w:name="{name}"/>{run(t,sz=sz,b=True,i=it)}<w:bookmarkEnd w:id="{900+bm[0]}"/>'
    return para(c,jc='left',before=240 if lvl==1 else 160,after=100,style=f'Heading{lvl}',keep=True,extra='<w:outlineLvl w:val="%d"/>'%(lvl-1) if False else ''), name
def CAP(t): return para(run(t,sz=24,b=True,i=False),jc='center',before=120,after=60,keep=True)
def EQ(t): return para(run(t,i=True),jc='center',before=60,after=60)
bd='<w:tblBorders>'+''.join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="000000"/>' for s in ['top','left','bottom','right','insideH','insideV'])+'</w:tblBorders>'
def TBL(head,rows,w):
    tw=sum(w)
    def cell(t,wd,hdr=False):
        sh='<w:shd w:val="clear" w:color="auto" w:fill="E7E6E6"/>' if hdr else ''
        return f'<w:tc><w:tcPr><w:tcW w:w="{wd}" w:type="dxa"/>{sh}<w:vAlign w:val="center"/></w:tcPr>{para(run(t,sz=24,b=hdr),jc="center" if hdr or len(t)<8 else "left",before=40,after=40,line=264)}</w:tc>'
    g=''.join(f'<w:gridCol w:w="{v}"/>' for v in w)
    tr=lambda cells,hdr=False: '<w:tr>'+('<w:trPr><w:cantSplit/><w:tblHeader/></w:trPr>' if hdr else '<w:trPr><w:cantSplit/></w:trPr>')+''.join(cell(c,v,hdr) for c,v in zip(cells,w))+'</w:tr>'
    return f'<w:tbl><w:tblPr><w:tblW w:w="{tw}" w:type="dxa"/><w:jc w:val="center"/>{bd}<w:tblLayout w:type="fixed"/><w:tblCellMar><w:left w:w="80" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr><w:tblGrid>{g}</w:tblGrid>{tr(head,True)}{"".join(tr(r) for r in rows)}</w:tbl>'+para('',after=0,line=240)
PB='<w:p><w:r><w:br w:type="page"/></w:r></w:p>'
import os, shutil
from PIL import Image as _Im
WD=os.path.dirname(DOC); FIG=os.path.join(os.path.dirname(sys.argv[2].rstrip('/')),'fig')
RELS=os.path.join(WD,'_rels','document.xml.rels'); rels=open(RELS,encoding='utf8').read(); nimg=[0]
def IMG(f,cap,wcm):
    global rels
    nimg[0]+=1; n=nimg[0]; rid=f'rIdFig{n}'; tgt=f'media/fig{n}.png'
    shutil.copy(os.path.join(FIG,f),os.path.join(WD,tgt))
    rels=rels.replace('</Relationships>',f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{tgt}"/></Relationships>')
    W,H=_Im.open(os.path.join(FIG,f)).size; cx=int(wcm*360000); cy=int(cx*H/W)
    d=(f'<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{5000+n}" name="Hinh {n}"/>'
       f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
       f'<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
       f'<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:nvPicPr><pic:cNvPr id="{5000+n}" name="fig{n}.png"/><pic:cNvPicPr/></pic:nvPicPr>'
       f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
       f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r>')
    return para(d,jc='center',before=120,after=40,line=240,keep=True)+para(run(cap,sz=24,i=True),jc='center',before=0,after=160)

out=[]; toc=[]
for blk in K.B:
    k=blk[0]
    if k in('h1','h2','h3'):
        lvl=int(k[1]);
        if lvl==1 and blk[1].startswith(('2.','3.','4.','5.','6.','7.')): out.append(PB)
        xml,name=H(blk[1],lvl); out.append(xml)
        if lvl<=2: toc.append((lvl,blk[1],name))
    elif k=='p': out.append(P(blk[1]))
    elif k=='b': out.append(BL(blk[1]))
    elif k=='cap': out.append(CAP(blk[1]))
    elif k=='eq': out.append(EQ(blk[1]))
    elif k=='kw': out.append(para(run('Từ khóa: ',b=True,i=True)+run(blk[1],i=True),ind='<w:ind w:firstLine="567"/>'))
    elif k=='tbl': out.append(TBL(blk[1],blk[2],blk[3]))
    elif k=='img': out.append(IMG(blk[1],blk[2],blk[3]))
out.append(PB); xml,name=H('TÀI LIỆU THAM KHẢO',1); out.append(xml); toc.append((1,'TÀI LIỆU THAM KHẢO',name))
for i,r in enumerate(K.REFS,1): out.append(para(run(f'[{i}] '+r),ind='<w:ind w:left="567" w:hanging="567"/>'))

# TOC
tl=[para(run('MỤC LỤC',sz=28,b=True),jc='center',after=200)]
TAB='<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9016"/></w:tabs>'
for n,(lvl,t,name) in enumerate(toc):
    pg=str(PAGES.get(name,''))
    begin='<w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r><w:r><w:fldChar w:fldCharType="separate"/></w:r>' if n==0 else ''
    end='<w:r><w:fldChar w:fldCharType="end"/></w:r>' if n==len(toc)-1 else ''
    c=begin+f'<w:hyperlink w:anchor="{name}" w:history="1">'+run(t,sz=26,b=(lvl==1))+f'<w:r>{rpr()}<w:tab/></w:r>'+run(pg,sz=26,b=(lvl==1))+'</w:hyperlink>'+end
    tl.append(para(c,jc='left',after=30,line=252,style=f'TOC{lvl}',ind=f'<w:ind w:left="{0 if lvl==1 else 284}"/>',extra='').replace('<w:pPr>','<w:pPr>'+'' ,1).replace('<w:jc w:val="left"/>','<w:jc w:val="left"/>'+'',1).replace(f'<w:pStyle w:val="TOC{lvl}"/>',f'<w:pStyle w:val="TOC{lvl}"/>{TAB}'))
newbody=cover+PB+''.join(tl)+PB+''.join(out)+sect+'</w:body></w:document>'
open(DOC,'w',encoding='utf8').write(head+newbody); open(RELS,'w',encoding='utf8').write(rels)
json.dump([(n,t) for _,t,n in toc],open(sys.argv[2]+'/toc.json','w'),ensure_ascii=False)
print('ok', len(toc))
