import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import sys
OUT=sys.argv[1]
plt.rcParams.update({'font.family':'Liberation Serif','font.size':10.5})
INK='#0b0b0b'; INK2='#52514e'; BLUE='#2a78d6'; ORANGE='#eb6834'; FILL='#eaf2fc'; FILLO='#fdeee7'; FILLG='#f2f2f0'
def box(ax,x,y,w,h,t,fc,ec,fs=10.5,bold=False,ha='center'):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.06',fc=fc,ec=ec,lw=1.2))
    tx=x+w/2 if ha=='center' else x+0.12
    ax.text(tx,y+h/2,t,ha=ha,va='center',fontsize=fs,color=INK,fontweight='bold' if bold else 'normal',linespacing=1.25)
def arrow(ax,x1,y1,x2,y2,c=INK2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>',color=c,lw=1.3,shrinkA=0,shrinkB=0))
layers=[('Tầng 1','Chuẩn hóa mã hóa\nvà ký tự','Chuyển bảng mã cũ TCVN3, VNI sang Unicode; chuẩn hóa dạng dựng sẵn;\nthống nhất kiểu đặt dấu; giữ song song dạng có dấu và không dấu'),
('Tầng 2','Phân tích cấu trúc,\nnhận diện mẫu','Tách từ, gán nhãn theo bảng tham chiếu và mẫu ký tự; tách tên khỏi\nđịa chỉ; nhận diện cá nhân, tổ chức; cửa sổ trượt cho trường tự do'),
('Tầng 3','Chuẩn hóa ngữ nghĩa','Loại hình doanh nghiệp, danh xưng, từ nhiễu; họ tương đương HOANG,\nHUYNH và VU, VO; biến thể chuyển tự tên quốc tế'),
('Tầng 4','Phân cụm đa khóa','Nhiều khóa song song, loại từ tần suất cao khỏi khóa, giới hạn kích\nthước cụm; khóa ngữ âm tiếng Việt'),
('Tầng 5','So khớp nâng cao','Nhiều phép so sánh: chính xác, chỉnh sửa ký tự, không phụ thuộc thứ tự,\nngữ âm, viết tắt; luật ưu tiên, băng điểm, trọng số theo tần suất'),
('Tầng 6','Chấm điểm và\nra quyết định','Thuộc tính phụ: quốc gia, năm sinh, loại thực thể, vị trí khớp; ngưỡng\ntheo rủi ro; danh sách loại trừ có kiểm soát; ghi nhận lý do khớp')]
H=0.78; G=0.22; n=len(layers); top=1.1+n*(H+G)
fig,ax=plt.subplots(figsize=(9.4,7.6)); ax.set_xlim(-0.1,10.15); ax.set_ylim(-0.05,top+1.15); ax.axis('off')
box(ax,0.0,top+0.25,3.1,0.75,'Điện SWIFT MT, MX',FILLG,INK2,fs=10)
box(ax,3.45,top+0.25,3.1,0.75,'Dữ liệu khách hàng',FILLG,INK2,fs=10)
box(ax,6.9,top+0.25,3.1,0.75,'Danh sách cấm vận',FILLG,INK2,fs=10)
yl=top+0.1
ax.plot([1.55,8.45],[yl,yl],color=INK2,lw=1.2)
for xx in (1.55,5.0,8.45): ax.plot([xx,xx],[top+0.25,yl],color=INK2,lw=1.2)
arrow(ax,1.275,yl,1.275,top-0.02)
ax.plot([1.275,1.55],[yl,yl],color=INK2,lw=1.2)
for i,(t,name,desc) in enumerate(layers):
    y=top-(i+1)*(H+G)+G
    box(ax,0.0,y,2.55,H,f'{t}\n{name}',FILL,BLUE,fs=10.5,bold=False)
    box(ax,2.8,y,7.2,H,desc,'white',BLUE,fs=9.6,ha='left')
    if i<n-1: arrow(ax,1.275,y,1.275,y-G)
yb=0.05
arrow(ax,1.275,top-n*(H+G)+G,1.275,yb+0.8)
box(ax,0.0,yb,3.1,0.8,'Không cảnh báo',FILLG,INK2,fs=10)
box(ax,3.45,yb,3.1,0.8,'Cảnh báo kèm lý do khớp',FILLO,ORANGE,fs=10)
box(ax,6.9,yb,3.1,0.8,'Chặn, báo cáo theo quy định',FILLO,ORANGE,fs=10)
ax.plot([1.275,8.45],[yb+0.95,yb+0.95],color=INK2,lw=1.2)
for xx in (5.0,8.45): arrow(ax,xx,yb+0.95,xx,yb+0.8)
fig.savefig(f'{OUT}/h8_mohinh.png',dpi=220,bbox_inches='tight',facecolor='white')
