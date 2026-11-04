import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import sys
OUT=sys.argv[1]
plt.rcParams.update({'font.family':'Liberation Serif','font.size':11,'axes.edgecolor':'#9a9994','axes.linewidth':0.8})
INK='#0b0b0b'; INK2='#52514e'; BLUE='#2a78d6'; ORANGE='#eb6834'; AQUA='#1baf7a'; GRID='#e4e3df'; FILL='#eaf2fc'; FILLO='#fdeee7'; FILLG='#f2f2f0'

def box(ax,x,y,w,h,t,fc=FILL,ec=BLUE,fs=10.5,bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.02,rounding_size=0.08',fc=fc,ec=ec,lw=1.2))
    ax.text(x+w/2,y+h/2,t,ha='center',va='center',fontsize=fs,color=INK,fontweight='bold' if bold else 'normal',wrap=True)
def arrow(ax,x1,y1,x2,y2,c=INK2):
    ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='-|>',color=c,lw=1.3,shrinkA=0,shrinkB=0))
def save(fig,name):
    fig.savefig(f'{OUT}/{name}.png',dpi=220,bbox_inches='tight',facecolor='white'); plt.close(fig)

# H1: quy trình sàng lọc
fig,ax=plt.subplots(figsize=(9.2,3.3)); ax.set_xlim(0,10); ax.set_ylim(0,3.6); ax.axis('off')
steps=[('Điện SWIFT\nMT / MX',FILLG,INK2),('Trích xuất\ntrường dữ liệu',FILL,BLUE),('Làm sạch,\nchuẩn hóa',FILL,BLUE),('Phân cụm\n(clustering)',FILL,BLUE),('So khớp\n(Advanced\nMatch)',FILL,BLUE),('Chấm điểm,\nso ngưỡng',FILL,BLUE)]
w=1.38; gap=0.25
for i,(t,fc,ec) in enumerate(steps):
    x=0.05+i*(w+gap); box(ax,x,2.0,w,1.1,t,fc,ec,fs=10)
    if i: arrow(ax,x-gap,2.55,x,2.55)
box(ax,1.2,0.25,2.6,0.95,'Không cảnh báo:\ngiao dịch được xử lý tiếp',FILLG,INK2,fs=10)
box(ax,4.5,0.25,2.4,0.95,'Cảnh báo:\nchuyên viên xem xét',FILLO,ORANGE,fs=10)
box(ax,7.5,0.25,2.4,0.95,'Khớp đúng: chặn,\nbáo cáo theo quy định',FILLO,ORANGE,fs=10)
xe=0.05+5*(w+gap)+w/2
arrow(ax,xe,2.0,2.5,1.2); arrow(ax,xe,2.0,5.7,1.2); arrow(ax,6.9,0.72,7.5,0.72)
ax.text(5.05,3.42,'Phạm vi tác động của đề tài: các bước làm sạch, chuẩn hóa, phân cụm, so khớp và ngưỡng',ha='center',fontsize=10,color=BLUE,style='italic')
ax.add_patch(Rectangle((0.05+2*(w+gap)-0.08,1.9),3*w+2*gap+0.16+ (w+gap),1.3,fill=False,ec=BLUE,lw=1,ls=(0,(4,3))))
save(fig,'h1_quytrinh')

# H2: ba vùng quyết định
fig,ax=plt.subplots(figsize=(8.5,2.2)); ax.set_xlim(0,100); ax.set_ylim(0,3); ax.axis('off')
ax.add_patch(Rectangle((0,1.2),50,0.7,fc=FILLG,ec='white',lw=2)); ax.add_patch(Rectangle((50,1.2),35,0.7,fc=FILLO,ec='white',lw=2)); ax.add_patch(Rectangle((85,1.2),15,0.7,fc='#f7c9b6',ec='white',lw=2))
ax.text(25,1.55,'Không khớp: tự động bỏ qua',ha='center',va='center',fontsize=10.5,color=INK)
ax.text(67.5,1.55,'Cảnh báo: xem xét thủ công',ha='center',va='center',fontsize=10.5,color=INK)
ax.text(92.5,1.55,'Khớp',ha='center',va='center',fontsize=10.5,color=INK)
for xv,lab in [(50,'Ngưỡng dưới'),(85,'Ngưỡng trên')]:
    ax.plot([xv,xv],[1.05,2.1],color=INK,lw=1.4); ax.text(xv,2.25,lab,ha='center',fontsize=10,color=INK)
arrow(ax,0,0.75,100,0.75,INK2); ax.text(50,0.3,'Điểm tương đồng của cặp (bản ghi, mục trong danh sách) tăng dần',ha='center',fontsize=10,color=INK2)
save(fig,'h2_vungquyetdinh')

# H3: trường 59 MT103
fig,ax=plt.subplots(figsize=(8.6,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
ax.text(0.1,3.15,':59:/123456789 (trường người hưởng, tối đa 4 dòng x 35 ký tự)',fontsize=10.5,color=INK2,family='Liberation Mono')
lines=[('NGUYEN THI MAI','Tên khách hàng',FILL,BLUE),('25 LE VAN LUONG','Địa chỉ: tên đường',FILLO,ORANGE),('THANH XUAN','Địa chỉ: quận',FILLG,INK2),('HA NOI VIET NAM','Địa chỉ: tỉnh, quốc gia',FILLG,INK2)]
for i,(t,lab,fc,ec) in enumerate(lines):
    y=2.45-i*0.62
    ax.add_patch(Rectangle((0.1,y),4.0,0.5,fc=fc,ec=ec,lw=1.1)); ax.text(0.22,y+0.25,t,va='center',fontsize=11,family='Liberation Mono',color=INK)
    ax.text(4.25,y+0.25,lab,va='center',fontsize=10,color=INK2)
box(ax,7.0,1.35,2.85,0.9,'Mục trong danh sách\n(giả định): LE VAN LUONG',FILLO,ORANGE,fs=10)
arrow(ax,6.15,2.0,7.0,1.85,ORANGE)
ax.text(8.42,0.85,'Khớp nhầm: tên đường\nbị coi là tên người',ha='center',fontsize=10,color=ORANGE,style='italic')
save(fig,'h3_mt103')

# H4: bỏ dấu
fig,ax=plt.subplots(figsize=(8.2,3.0)); ax.set_xlim(0,10); ax.set_ylim(0,3.4); ax.axis('off')
src=['Hưng','Hùng','Hứng','Hừng']; src2=['Thủy','Thùy','Thụy']
for i,t in enumerate(src):
    y=2.9-i*0.48; box(ax,0.3,y-0.18,1.6,0.38,t,FILL,BLUE,fs=11); arrow(ax,1.9,y,3.6,2.15)
box(ax,3.6,1.9,1.7,0.5,'HUNG',FILLO,ORANGE,fs=11.5,bold=True)
for i,t in enumerate(src2):
    y=2.9-i*0.48; box(ax,5.9,y-0.18,1.6,0.38,t,FILL,BLUE,fs=11); arrow(ax,7.5,y,8.2,2.4)
box(ax,8.2,2.15,1.6,0.5,'THUY',FILLO,ORANGE,fs=11.5,bold=True)
ax.text(5,0.55,'Tên có dấu trong hệ thống khách hàng   →   tên không dấu trong điện SWIFT và danh sách cấm vận',ha='center',fontsize=10,color=INK2)
ax.text(5,0.15,'Nhiều tên khác nhau trở thành cùng một chuỗi ký tự, làm mất khả năng phân biệt khi so khớp',ha='center',fontsize=10,color=INK2,style='italic')
save(fig,'h4_bodau')

# H5: tỷ lệ họ (Lê Trung Hoa 2005)
names=['Nguyễn','Trần','Lê','Phạm','Các họ khác']; vals=[38.4,12.1,9.5,7.0,33.0]
fig,ax=plt.subplots(figsize=(7.4,3.4))
cols=[BLUE]*4+['#b9b8b3']
bars=ax.bar(names,vals,color=cols,width=0.6,edgecolor='white',linewidth=2,zorder=3)
for b_,v in zip(bars,vals): ax.text(b_.get_x()+b_.get_width()/2,v+0.8,f'{v:.1f}%'.replace('.',','),ha='center',fontsize=10.5,color=INK)
ax.set_ylabel('Tỷ lệ dân số (%)',color=INK2); ax.set_ylim(0,45); ax.grid(axis='y',color=GRID,zorder=0); ax.tick_params(colors=INK2)
for s in ['top','right']: ax.spines[s].set_visible(False)
ax.text(4,39,'Bốn họ lớn nhất\nchiếm khoảng 67%',ha='center',fontsize=10,color=INK2,style='italic')
save(fig,'h5_ho')

# H6: quy trình dữ liệu và nghiên cứu
fig,ax=plt.subplots(figsize=(9.2,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off')
box(ax,0.05,2.75,2.1,0.95,'Mẫu ngẫu nhiên\n10 triệu tên, địa chỉ\nkhách hàng MB',FILLG,INK2,fs=9.5)
box(ax,2.55,2.75,2.1,0.95,'Hoán đổi ngẫu nhiên\nđịa chỉ giữa\ncác bản ghi',FILL,BLUE,fs=9.5)
box(ax,5.05,2.75,2.1,0.95,'Mẫu âm\n(không khớp)',FILL,BLUE,fs=9.5)
box(ax,5.05,1.45,2.1,0.95,'Mẫu dương: biến thể\ntên trong danh sách\ncấm vận',FILLO,ORANGE,fs=9.5)
box(ax,2.55,1.45,2.1,0.95,'Danh sách cấm vận\nOFAC, UN, EU, UK,\nViệt Nam',FILLG,INK2,fs=9.5)
box(ax,7.6,2.1,2.3,0.95,'Sinh điện MT103,\nMT202, pacs.008,\npacs.009 có gán nhãn',FILL,BLUE,fs=9.5)
box(ax,7.6,0.15,2.3,0.95,'Đánh giá: Precision,\nRecall, F2, số cảnh báo,\nhiệu năng',FILLO,ORANGE,fs=9.5)
box(ax,4.0,0.15,3.0,0.95,'Thực nghiệm trên OEDQ:\nchuẩn hóa, phân cụm,\nso khớp, ngưỡng',FILL,BLUE,fs=9.5)
arrow(ax,2.15,3.22,2.55,3.22); arrow(ax,4.65,3.22,5.05,3.22); arrow(ax,4.65,1.92,5.05,1.92)
arrow(ax,7.15,3.22,7.6,2.75); arrow(ax,7.15,1.92,7.6,2.4); arrow(ax,8.75,2.1,6.5,1.1); arrow(ax,7.0,0.62,7.6,0.62)
save(fig,'h6_dulieu')

# H7: Gantt 6 tháng
tasks=[('ND1. Khảo sát, phân tích đặc trưng dữ liệu',0,1),('ND2. Xây dựng bộ dữ liệu kiểm thử',1,1),('ND3. Tối ưu làm sạch, chuẩn hóa',2,1),('ND4. Tối ưu phân cụm, so khớp, ngưỡng',2,2),('ND5. Quy trình kiểm định, đánh giá',4,1),('ND6. Công bố, hoàn thiện luận văn',3,3)]
fig,ax=plt.subplots(figsize=(8.6,3.0))
for i,(t,s,d) in enumerate(tasks[::-1]):
    ax.barh(i,d,left=s,height=0.5,color=ORANGE if t.startswith('ND6') else BLUE,edgecolor='white',linewidth=2,zorder=3)
ax.set_yticks(range(len(tasks))); ax.set_yticklabels([t for t,_,_ in tasks[::-1]],color=INK)
ax.set_xticks([i+0.5 for i in range(6)]); ax.set_xticklabels([f'Tháng {i+1}' for i in range(6)],color=INK2)
ax.set_xticks(range(7),minor=True); ax.grid(axis='x',which='minor',color=GRID,zorder=0); ax.tick_params(which='both',length=0)
ax.set_xlim(0,6)
for s in ['top','right','left']: ax.spines[s].set_visible(False)
save(fig,'h7_gantt')
print('done')
