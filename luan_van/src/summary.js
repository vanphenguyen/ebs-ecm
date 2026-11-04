const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,AlignmentType,LevelFormat,Table,TableRow,TableCell,WidthType,BorderStyle}=require('docx');
const F='Times New Roman', SZ=25; // 12.5pt
const sp={before:0,after:50,line:276};
const r=(t,o={})=>new TextRun({text:t,font:F,size:SZ,...o});
const p=(runs,o={})=>new Paragraph({children:Array.isArray(runs)?runs:[r(runs)],spacing:sp,alignment:AlignmentType.JUSTIFIED,indent:{firstLine:425},...o});
const h=t=>new Paragraph({children:[r(t,{bold:true})],spacing:{before:90,after:40,line:276},keepNext:true});
const li=(t,ref)=>new Paragraph({children:Array.isArray(t)?t:[r(t)],numbering:{reference:ref,level:0},spacing:sp,alignment:AlignmentType.JUSTIFIED});
const nb={top:{style:BorderStyle.NONE,size:0,color:'FFFFFF'},bottom:{style:BorderStyle.NONE,size:0,color:'FFFFFF'},left:{style:BorderStyle.NONE,size:0,color:'FFFFFF'},right:{style:BorderStyle.NONE,size:0,color:'FFFFFF'}};
const cell=(ps,w)=>new TableCell({children:ps,width:{size:w,type:WidthType.DXA},borders:nb});
const c=(t,o={})=>new Paragraph({children:[r(t,o)],alignment:AlignmentType.CENTER,spacing:{before:0,after:0}});
const numCfg=(ref,fmt,text,left=709,hang=284)=>({reference:ref,levels:[{level:0,format:fmt,text,alignment:AlignmentType.LEFT,style:{paragraph:{indent:{left,hanging:hang}},run:{font:F,size:SZ}}}]});
const W=9071;
const header=new Table({width:{size:W,type:WidthType.DXA},columnWidths:[3800,5271],borders:{top:nb.top,bottom:nb.bottom,left:nb.left,right:nb.right,insideHorizontal:nb.top,insideVertical:nb.top},rows:[new TableRow({children:[
  cell([c('HỌC VIỆN CÔNG NGHỆ',{size:23}),c('BƯU CHÍNH VIỄN THÔNG',{size:23,bold:true})],3800),
  cell([c('CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM',{size:23,bold:true}),c('Độc lập - Tự do - Hạnh phúc',{size:24,bold:true})],5271)]})]});
const ip=(k,v)=>new Paragraph({children:[r(k),r(v,{bold:true})],spacing:{before:0,after:20,line:264}});
const infoTbl=new Table({width:{size:W,type:WidthType.DXA},columnWidths:[3800,5271],margins:{left:0,right:0,top:0,bottom:0},borders:{top:nb.top,bottom:nb.bottom,left:nb.left,right:nb.right,insideHorizontal:nb.top,insideVertical:nb.top},rows:[
 new TableRow({children:[cell([ip('Học viên: ','Nguyễn Văn Phê')],3800),cell([ip('Mã học viên: ','B26CHHT080')],5271)]}),
 new TableRow({children:[cell([ip('Chuyên ngành: ','Hệ thống thông tin')],3800),cell([ip('Nơi công tác: ','Ngân hàng TMCP Quân đội (MB)')],5271)]})]});
const kv=(k,v)=>new Paragraph({children:[r(k),r(v,{bold:true})],spacing:{before:0,after:20,line:264}});
const children=[header,
 new Paragraph({children:[r('ĐỀ XUẤT HƯỚNG NGHIÊN CỨU LUẬN VĂN THẠC SĨ',{bold:true,size:27})],alignment:AlignmentType.CENTER,spacing:{before:140,after:80}}),
 infoTbl,
 new Paragraph({children:[r('Người hướng dẫn dự kiến: '),r('TS. Đỗ Trung Anh',{bold:true})],spacing:{before:0,after:20,line:264}}),
 h('1. Tên đề tài dự kiến'),
 p([r('Tiếng Việt: ',{italic:true}),r('Nghiên cứu tối ưu hóa quy tắc làm sạch, chuẩn hóa và so khớp mờ nhằm giảm cảnh báo sai trong hệ thống sàng lọc cấm vận giao dịch thanh toán quốc tế qua mạng SWIFT: thực nghiệm trên nền tảng Oracle Enterprise Data Quality.')]),
 p([r('Tiếng Anh: ',{italic:true}),r('Optimizing data cleansing, standardization and fuzzy matching rules to reduce false positives in sanctions screening of SWIFT cross-border payments: an empirical study on Oracle Enterprise Data Quality.',{italic:true})]),
 h('2. Lý do lựa chọn đề tài'),
 p('Sàng lọc cấm vận là khâu kiểm soát bắt buộc đối với ngân hàng tham gia thanh toán quốc tế: các bên trong điện SWIFT phải được đối chiếu với danh sách cấm vận của Liên Hợp Quốc, OFAC, Liên minh châu Âu, Vương quốc Anh và cơ quan có thẩm quyền Việt Nam trước khi giao dịch được xử lý. Do tên người và tổ chức có nhiều biến thể (phiên âm, viết tắt, lỗi nhập liệu, bỏ dấu, đảo thứ tự), hệ thống phải dùng kỹ thuật so khớp mờ, kéo theo tỷ lệ cảnh báo sai rất cao. Phần lớn cảnh báo được chuyên viên kết luận là không trùng khớp, gây tốn nguồn lực và làm chậm giao dịch của khách hàng. Ngược lại, nới lỏng quy tắc lại làm tăng nguy cơ bỏ sót đối tượng bị cấm vận.'),
 p('Hiện nay việc hiệu chỉnh quy tắc chủ yếu dựa vào kinh nghiệm và cấu hình mặc định của nhà cung cấp, thiếu cơ sở định lượng để chứng minh việc giảm cảnh báo không làm tăng rủi ro bỏ sót. Các nghiên cứu quốc tế về so khớp tên (Cohen và cộng sự, 2003; Christen, 2012) cho thấy hiệu quả phụ thuộc nhiều vào bước tiền xử lý và đặc điểm dữ liệu; hướng dẫn của Nhóm Wolfsberg (2019) khuyến nghị kiểm thử hệ thống bằng dữ liệu có kiểm soát. Trong nước, theo tìm hiểu của học viên, chưa có nghiên cứu thực nghiệm định lượng về vấn đề này, nhất là với đặc thù tên tiếng Việt không dấu và tên doanh nghiệp Việt Nam. Bên cạnh đó, Việt Nam đang nằm trong danh sách tăng cường giám sát của FATF từ tháng 6/2023, Thông tư 27/2025/TT-NHNN vừa có hiệu lực và SWIFT đã chuyển hẳn sang chuẩn ISO 20022 từ ngày 22/11/2025, khiến yêu cầu nâng cao hiệu quả sàng lọc càng trở nên cấp thiết. Học viên đang trực tiếp tham gia xây dựng quy tắc làm sạch, chuẩn hóa và so khớp (Advanced Match) trên nền tảng OEDQ tại MB, nên có điều kiện thuận lợi để thực hiện đề tài.'),
 h('3. Mục tiêu và câu hỏi nghiên cứu'),
 p('Mục tiêu chung của đề tài là nâng cao hiệu quả hệ thống sàng lọc cấm vận giao dịch SWIFT thông qua việc tối ưu hóa có cơ sở định lượng các quy tắc xử lý dữ liệu và so khớp trên OEDQ. Các mục tiêu cụ thể gồm:'),
 li('Xây dựng bộ dữ liệu kiểm thử có gán nhãn từ các danh sách cấm vận công khai, kết hợp kỹ thuật sinh biến thể tên và điện thanh toán tổng hợp theo định dạng MT và ISO 20022.','m'),
 li('Đánh giá tác động của từng bước làm sạch, chuẩn hóa, phân cụm, quy tắc so khớp và ngưỡng đến độ chính xác (Precision) và độ bao phủ (Recall).','m'),
 li('Đề xuất cấu hình giảm ít nhất 30% cảnh báo sai so với cấu hình hiện hành trong khi duy trì Recall từ 99% trở lên, cùng quy trình kiểm định và hiệu chỉnh định kỳ.','m'),
 p('Đề tài tập trung trả lời ba câu hỏi: (1) Các quy tắc làm sạch, chuẩn hóa ảnh hưởng thế nào đến Precision và Recall? (2) Chiến lược phân cụm và tổ hợp quy tắc so khớp, ngưỡng nào phù hợp với từng nhóm tên (Việt Nam, Trung Quốc, Ả Rập, Nga, Latinh)? (3) Dữ liệu có cấu trúc của điện ISO 20022 cải thiện hiệu quả sàng lọc ra sao so với điện MT dạng văn bản tự do?'),
 h('4. Đối tượng và phạm vi nghiên cứu'),
 p('Đối tượng nghiên cứu là quy trình và quy tắc sàng lọc cấm vận theo thời gian thực đối với điện thanh toán quốc tế qua SWIFT. Đề tài không đề cập đến giám sát giao dịch đáng ngờ theo hành vi. Thực nghiệm được tiến hành trên môi trường OEDQ thử nghiệm, tách biệt với hệ thống vận hành; dữ liệu sử dụng là dữ liệu công khai và dữ liệu tổng hợp, dữ liệu thực (nếu được phép) chỉ dùng ở dạng đã ẩn danh.'),
 h('5. Phương pháp và nội dung thực hiện'),
 li('Nghiên cứu tài liệu, khảo sát quy trình và phỏng vấn chuyên viên tuân thủ để xác định cấu hình nền và các nguyên nhân chính gây cảnh báo sai.','s'),
 li('Thu thập, hợp nhất các danh sách cấm vận công khai; xây dựng công cụ sinh biến thể tên theo phân loại lỗi của Wolfsberg và sinh điện MT103, MT202, pacs.008, pacs.009 có gán nhãn.','s'),
 li('Thực nghiệm loại bỏ từng thành phần (ablation study) đối với các quy tắc làm sạch, chuẩn hóa; so sánh các khóa phân cụm, quy tắc Advanced Match và một số độ đo đối chứng (Jaro-Winkler, Levenshtein, TF-IDF trên n-gram), được cài đặt bằng Python.','s'),
 li('Tối ưu ngưỡng theo hàm mục tiêu giảm cảnh báo sai với ràng buộc Recall; đánh giá bằng Precision, Recall, F2-score, số cảnh báo trên 1.000 giao dịch, thời gian xử lý; kiểm định ý nghĩa thống kê bằng kiểm định McNemar.','s'),
 li('Đề xuất quy trình kiểm định, hiệu chỉnh định kỳ, đối chiếu với quy định Việt Nam và thông lệ quốc tế (OFAC, NYDFS Part 504, Wolfsberg).','s'),
 h('6. Kết quả dự kiến'),
 p('Đề tài dự kiến tạo ra bộ dữ liệu kiểm thử và công cụ sinh dữ liệu có thể tái sử dụng; bộ kết quả thực nghiệm định lượng về tác động của từng thành phần trong chuỗi xử lý; đề xuất quy tắc chuẩn hóa, so khớp phù hợp với tên tiếng Việt; và quy trình kiểm định hệ thống sàng lọc có thể áp dụng tại MB cũng như các ngân hàng thương mại khác. Học viên dự kiến công bố 01 bài báo trên tạp chí khoa học trong nước hoặc tại hội thảo chuyên ngành.'),
 h('7. Kế hoạch thực hiện dự kiến (12 tháng)'),
 p('Tháng 1 đến tháng 2: tổng quan tài liệu, khảo sát hiện trạng. Tháng 3 đến tháng 4: xây dựng bộ dữ liệu kiểm thử. Tháng 5 đến tháng 8: thực nghiệm và phân tích kết quả. Tháng 9 đến tháng 10: xây dựng quy trình kiểm định, lấy ý kiến chuyên gia. Tháng 11 đến tháng 12: viết bài báo, hoàn thiện luận văn.'),
 h('Tài liệu tham khảo chính'),
 li('Christen, P. (2012). Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection. Springer.','r'),
 li('Cohen, W. W., Ravikumar, P., & Fienberg, S. E. (2003). A comparison of string distance metrics for name-matching tasks. Proceedings of the IJCAI-03 Workshop on Information Integration on the Web.','r'),
 li('The Wolfsberg Group (2019). Wolfsberg Guidance on Sanctions Screening.','r'),
 li('Quốc hội (2022). Luật Phòng, chống rửa tiền số 14/2022/QH15; Ngân hàng Nhà nước Việt Nam (2025). Thông tư 27/2025/TT-NHNN.','r'),
 p('Kính mong Thầy xem xét và cho ý kiến định hướng để học viên hoàn thiện đề cương chi tiết.',{spacing:{before:80,after:40,line:276}}),
 new Paragraph({children:[r('Hà Nội, ngày ..... tháng ..... năm 2026',{italic:true})],alignment:AlignmentType.RIGHT,spacing:{before:60,after:0}}),
 new Paragraph({children:[r('Học viên',{bold:true})],alignment:AlignmentType.RIGHT,indent:{right:900},spacing:{before:0,after:320}}),
 new Paragraph({children:[r('Nguyễn Văn Phê',{bold:true})],alignment:AlignmentType.RIGHT,indent:{right:600},spacing:{before:0,after:0}}),
];
const doc=new Document({numbering:{config:[numCfg('m',LevelFormat.LOWER_LETTER,'%1)'),numCfg('s',LevelFormat.DECIMAL,'Bước %1.',1276,851),numCfg('r',LevelFormat.DECIMAL,'[%1]',851,426)]},
 sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:964,bottom:851,left:1701,right:1134}}},children}]});
Packer.toBuffer(doc).then(b=>fs.writeFileSync(process.argv[2],b));
