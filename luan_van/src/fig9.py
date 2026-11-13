import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import sys
OUT=sys.argv[1]
plt.rcParams.update({'font.family':'Liberation Serif','font.size':10.5})
INK='#0b0b0b'; INK2='#52514e'; BLUE='#2a78d6'; ORANGE='#eb6834'; FILL='#eaf2fc'; FILLO='#fdeee7'
def box(ax,x,y,w,h,t,fc,ec):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.06',fc=fc,ec=ec,lw=1.2))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=10,color=INK,linespacing=1.25)
def arrow(ax,x1,y1,x2,y2,c=INK2,cs='arc3'):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>',color=c,lw=1.3,shrinkA=0,shrinkB=0,connectionstyle=cs))
fig,ax=plt.subplots(figsize=(9.2,3.9)); ax.set_xlim(-0.1,10.1); ax.set_ylim(-0.1,4.2); ax.axis('off')
W=2.9; H=1.05
top=[('1. Xác định vấn đề\nCảnh báo sai, đặc thù\ntên, địa chỉ người Việt',FILL,BLUE),('2. Mục tiêu giải pháp\nGiảm 30% cảnh báo sai,\nRecall từ 99%',FILL,BLUE),('3. Thiết kế, phát triển\nMô hình 6 tầng, khóa ngữ âm,\nbảng tham chiếu',FILLO,ORANGE)]
bot=[('6. Truyền đạt\nBài báo, luận văn,\nchia sẻ tại ngân hàng',FILL,BLUE),('5. Đánh giá\nChỉ số theo tầng, kiểm định\nthống kê, ý kiến chuyên gia',FILLO,ORANGE),('4. Trình diễn\nHiện thực trên OEDQ,\nchạy dữ liệu kiểm thử',FILLO,ORANGE)]
xs=[0.0,3.55,7.1]
for (t,fc,ec),x in zip(top,xs): box(ax,x,2.75,W,H,t,fc,ec)
for (t,fc,ec),x in zip(bot,xs): box(ax,x,0.25,W,H,t,fc,ec)
arrow(ax,2.9,3.27,3.55,3.27); arrow(ax,6.45,3.27,7.1,3.27); arrow(ax,8.55,2.75,8.55,1.3)
arrow(ax,7.1,0.77,6.45,0.77); arrow(ax,3.55,0.77,2.9,0.77)
arrow(ax,5.0,1.3,7.6,2.75,ORANGE,'arc3,rad=-0.25')
ax.text(4.75,1.95,'Vòng lặp cải tiến thiết kế',fontsize=10,color=ORANGE,style='italic',ha='right')
fig.savefig(f'{OUT}/h9_dsr.png',dpi=220,bbox_inches='tight',facecolor='white')
