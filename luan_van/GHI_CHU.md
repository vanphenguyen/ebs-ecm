# Ghi chú luận văn thạc sĩ

## Thông tin chung
- Học viên: Nguyễn Văn Phê, mã học viên B26CHHT080, lớp M26CQHT02-B
- Chuyên ngành: Hệ thống thông tin
- Cơ sở đào tạo: Học viện Công nghệ Bưu chính Viễn thông
- Người hướng dẫn: TS. Đỗ Trung Anh
- Nơi công tác, nơi áp dụng: Ngân hàng Thương mại Cổ phần Quân đội (MB)

## Đề tài (tên hiện hành)
Nghiên cứu giải pháp chuẩn hóa dữ liệu và so khớp tên nhằm giảm cảnh báo sai trong sàng lọc
cấm vận giao dịch thanh toán quốc tế tại ngân hàng thương mại Việt Nam.
- Tên tiếng Anh: Data standardization and name matching solutions for reducing false positives
  in sanctions screening of international payments at Vietnamese commercial banks.
- MB là đơn vị phối hợp, nơi thử nghiệm và đánh giá (không đưa vào tên đề tài).
- Thời gian thực hiện: 06 tháng.
- Đặc thù tên, địa chỉ người Việt cần xử lý: tên đường theo tên danh nhân (điện SWIFT ghép tên + địa chỉ);
  trùng tên khi bỏ dấu (Hưng = Hùng = HUNG); họ phân bố lệch (Nguyễn 38,4% theo Lê Trung Hoa 2005,
  khoảng 31,5% theo "100 họ phổ biến ở Việt Nam" 2022) làm cụm theo họ không đều.
- Dữ liệu: mẫu ngẫu nhiên 10 triệu tên và địa chỉ khách hàng MB, địa chỉ hoán đổi ngẫu nhiên giữa
  các bản ghi, không có thông tin định danh nào khác.
- Trang bìa theo mẫu `src/Mau_trang_bia.docx`; cấu trúc nội dung theo mẫu NAFOSTED 02.

## Quy ước trình bày
- Văn phong học thuật tiếng Việt, xưng "học viên".
- Không dùng gạch ngang dài (– hoặc —) và dấu "…"; dùng dấu phẩy, gạch nối thường hoặc "...".
- Viết hoa tên cơ quan theo Nghị định 30/2020/NĐ-CP.
- Văn bản pháp lý AML hiện hành: Luật PCRT 14/2022/QH15, Nghị định 19/2023/NĐ-CP,
  Thông tư 27/2025/TT-NHNN (thay thế Thông tư 09/2023/TT-NHNN), Nghị định 81/2019/NĐ-CP.

## Tệp
- `../NguyenVanPhe_B26CHHT080_BaoCaoCuoiKy_PPNCKH.docx`: báo cáo cuối kỳ môn PPNCKH, bản nghiên cứu hoàn chỉnh (bản chính).
- `../Thuyet_minh_NAFOSTED_Sanctions_Screening.docx`: thuyết minh theo mẫu NAFOSTED 02.
- `../De_xuat_huong_nghien_cuu_Nguyen_Van_Phe.docx`: bản đề xuất 2 trang gửi thầy.
- `src/`: mẫu gốc và mã sinh tài liệu (content.py chứa nội dung thuyết minh).

## Định hướng làm nổi bật (đã đưa vào bản PPNCKH)
- Bài toán được trình bày như phân giải thực thể trên dữ liệu kém chất lượng, không phải so sánh chuỗi đơn giản.
- Mô hình sàng lọc đa tầng 6 tầng: chuẩn hóa mã hóa và ký tự; phân tích cấu trúc, nhận diện mẫu; chuẩn hóa ngữ nghĩa;
  phân cụm đa khóa và khóa ngữ âm tiếng Việt; so khớp nâng cao có luật ưu tiên, băng điểm; chấm điểm với thuộc tính phụ, danh sách loại trừ.
- Không nhắc tên giải pháp thương mại sàng lọc giao dịch của Oracle trong bài; chỉ nói nền tảng OEDQ.
- Bảng, hình được đánh số tự động: dùng nhãn {b_ten}, {h_ten} trong full_content.py.
