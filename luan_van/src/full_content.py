# Nội dung bài nghiên cứu hoàn chỉnh (cấu trúc theo mẫu thuyết minh NAFOSTED 02)
# Quy ước: ('h1'|'h2'|'h3', text) tiêu đề; ('p', text) đoạn văn; ('b', text) gạch đầu dòng;
# ('tbl', [tiêu đề cột], [[ô,...],...], [độ rộng dxa]); ('cap', text) chú thích bảng; ('ref', text); ('eq', text)

TITLE = ("Tối ưu hóa quy tắc so khớp nhằm giảm cảnh báo sai trong sàng lọc cấm vận "
         "giao dịch SWIFT tại Ngân hàng TMCP Quân đội")
TITLE_EN = ("Optimizing matching rules to reduce false positives in sanctions screening "
            "of SWIFT transactions at Military Commercial Joint Stock Bank")

B = []
def h1(t): B.append(('h1', t))
def h2(t): B.append(('h2', t))
def h3(t): B.append(('h3', t))
def p(t): B.append(('p', t))
def b(t): B.append(('b', t))
def cap(t): B.append(('cap', t))
def tbl(head, rows, widths): B.append(('tbl', head, rows, widths))
def eq(t): B.append(('eq', t))
def img(f, c, w=16): B.append(('img', f, c, w))

# ---------------------------------------------------------------- THÔNG TIN CHUNG
h1("THÔNG TIN CHUNG VỀ ĐỀ TÀI")
tbl(["Mục", "Nội dung"], [
    ["Tên đề tài", TITLE],
    ["Tên tiếng Anh", TITLE_EN],
    ["Chủ nhiệm đề tài", "Nguyễn Văn Phê, mã học viên B26CHHT080"],
    ["Người hướng dẫn khoa học", "TS. Đỗ Trung Anh"],
    ["Tổ chức chủ trì", "Học viện Công nghệ Bưu chính Viễn thông"],
    ["Đơn vị phối hợp, áp dụng", "Ngân hàng Thương mại Cổ phần Quân đội (MB)"],
    ["Chuyên ngành", "Hệ thống thông tin"],
    ["Thời gian thực hiện", "06 tháng kể từ ngày đề cương được phê duyệt"],
], [2600, 6400])

# ---------------------------------------------------------------- 1. TÓM TẮT
h1("1. TÓM TẮT")
p("Sàng lọc cấm vận là khâu kiểm soát bắt buộc đối với các ngân hàng tham gia thanh toán quốc tế qua mạng SWIFT: "
  "mọi bên liên quan trong điện thanh toán phải được đối chiếu với danh sách cấm vận của Liên Hợp Quốc, OFAC, Liên minh châu Âu, "
  "Vương quốc Anh và cơ quan có thẩm quyền Việt Nam trước khi giao dịch được xử lý. Do tên người và tổ chức có nhiều biến thể, "
  "hệ thống phải sử dụng kỹ thuật so khớp mờ, dẫn đến tỷ lệ cảnh báo sai rất cao. Đối với khách hàng Việt Nam, vấn đề càng trầm trọng "
  "bởi ba đặc thù: tên đường thường được đặt theo tên danh nhân nên dễ bị nhận nhầm là tên người khi địa chỉ được ghép chung với tên "
  "trong điện SWIFT; tên tiếng Việt khi bỏ dấu khiến nhiều tên khác nhau trùng thành một; và họ người Việt phân bố rất lệch, trong đó "
  "họ Nguyễn chiếm khoảng 31,5% đến 38,4% dân số, làm cho việc phân cụm theo họ tạo ra các cụm có kích thước chênh lệch lớn.")
p("Đề tài nghiên cứu một cách định lượng ảnh hưởng của các quy tắc làm sạch, chuẩn hóa, phân cụm và so khớp trên nền tảng "
  "Oracle Enterprise Data Quality (OEDQ) đến độ chính xác (Precision) và độ bao phủ (Recall) của hệ thống sàng lọc. Dữ liệu thực nghiệm "
  "gồm 10 triệu cặp tên và địa chỉ khách hàng được lấy mẫu ngẫu nhiên tại Ngân hàng TMCP Quân đội, trong đó địa chỉ được hoán đổi ngẫu nhiên "
  "giữa các khách hàng để loại bỏ khả năng nhận diện. Trên cơ sở đó, đề tài đề xuất bộ quy tắc phù hợp với đặc thù tên, địa chỉ người Việt "
  "và quy trình kiểm định định kỳ, với mục tiêu giảm ít nhất 30% cảnh báo sai trong khi duy trì Recall không thấp hơn 99%.")
B.append(('kw', "sàng lọc cấm vận; so khớp tên mờ; cảnh báo sai; tên tiếng Việt; phân cụm; Oracle EDQ; SWIFT; ISO 20022"))

# ---------------------------------------------------------------- 2. TỔNG QUAN
h1("2. TỔNG QUAN TÌNH HÌNH NGHIÊN CỨU VÀ SỰ CẦN THIẾT TIẾN HÀNH NGHIÊN CỨU")
h2("2.1. Tình hình nghiên cứu ngoài nước")
h3("2.1.1. So khớp tên và liên kết bản ghi")
p("Bài toán so khớp tên trong sàng lọc cấm vận là một trường hợp riêng của bài toán liên kết bản ghi (record linkage), "
  "có nền tảng lý thuyết xác suất do Fellegi và Sunter xây dựng [1]. Theo mô hình này, mỗi cặp bản ghi được so sánh trên nhiều "
  "thuộc tính, các kết quả so sánh được tổng hợp thành trọng số và cặp bản ghi được phân loại thành khớp, không khớp hoặc cần xem xét "
  "thủ công dựa trên hai ngưỡng (Hình 1). Cách tiếp cận ba vùng quyết định này tương ứng trực tiếp với cách các hệ thống sàng lọc thương mại "
  "phân loại kết quả thành tự động bỏ qua, cảnh báo hoặc chặn.")
img("h2_vungquyetdinh.png", "Hình 1. Ba vùng quyết định theo mô hình Fellegi-Sunter áp dụng trong sàng lọc cấm vận", 15)
p("Winkler [2] phát triển độ đo Jaro-Winkler, ưu tiên các chuỗi có phần đầu giống nhau, phù hợp với chuỗi ngắn như họ tên và được "
  "Cục Điều tra Dân số Hoa Kỳ sử dụng trong thực tế. Cohen và cộng sự [3] so sánh có hệ thống các nhóm độ đo khoảng cách chuỗi gồm "
  "độ đo dựa trên chỉnh sửa (Levenshtein), độ đo heuristic (Jaro, Jaro-Winkler), độ đo dựa trên từ (TF-IDF, Jaccard) và các phương pháp lai; "
  "kết quả cho thấy phương pháp lai kết hợp TF-IDF với Jaro-Winkler cho hiệu quả tốt nhất trên nhiều bộ dữ liệu. Branting [4] đánh giá "
  "các thuật toán so khớp tên trong hệ thống quản lý hồ sơ tòa án và chỉ ra rằng các bước chuẩn hóa chữ hoa, khoảng trắng, dấu câu, "
  "loại bỏ từ dư thừa và so sánh theo từng từ có ảnh hưởng lớn đến sự cân bằng giữa độ chính xác và hiệu năng. Christen [5] hệ thống hóa "
  "toàn bộ quy trình liên kết dữ liệu gồm làm sạch và chuẩn hóa, phân khối, so sánh, phân loại và đánh giá; đây là khung tham chiếu "
  "chính cho thiết kế thực nghiệm của đề tài.")
p("Gần đây, các mô hình học sâu như DeepMatcher [7], Ditto [8] và mô hình ngôn ngữ lớn [9] đã được áp dụng cho so khớp thực thể "
  "và đạt kết quả cao trên các bộ dữ liệu sản phẩm, thư mục. Tuy nhiên, các mô hình này khó giải thích, đòi hỏi tài nguyên tính toán lớn "
  "và chưa được kiểm chứng trong bối cảnh sàng lọc cấm vận, nơi mỗi quyết định bỏ qua cảnh báo cần có căn cứ rõ ràng phục vụ kiểm toán. "
  "Vì vậy, các hệ thống sàng lọc tại ngân hàng hiện nay vẫn chủ yếu dựa trên quy tắc có thể giải thích được.")
h3("2.1.2. Phân khối và phân cụm trong so khớp quy mô lớn")
p("Khi so sánh N bản ghi với M mục trong danh sách, số cặp cần so sánh là N nhân M, không khả thi với dữ liệu hàng chục triệu bản ghi. "
  "Kỹ thuật phân khối (blocking), trong OEDQ gọi là phân cụm (clustering), chỉ so sánh các cặp có cùng khóa cụm. Papadakis và cộng sự [6] "
  "tổng quan các kỹ thuật phân khối và lọc, chỉ ra sự đánh đổi giữa tỷ lệ giảm số cặp so sánh (reduction ratio) và tỷ lệ giữ lại các cặp "
  "khớp đúng (pair completeness). Một khóa cụm quá chặt sẽ loại bỏ cặp khớp đúng ngay từ đầu, dẫn đến bỏ sót mà không bước so khớp nào "
  "bù lại được; ngược lại, một khóa cụm có phân bố lệch sẽ tạo ra các cụm khổng lồ làm tăng mạnh thời gian xử lý. Đây là cơ sở lý thuyết "
  "để đề tài phân tích ảnh hưởng của phân bố họ người Việt đến chiến lược phân cụm.")
h3("2.1.3. Sàng lọc cấm vận: quy định và thông lệ quốc tế")
p("Khuyến nghị 6 và 7 của FATF yêu cầu các quốc gia thực thi biện pháp trừng phạt tài chính có mục tiêu liên quan đến khủng bố và "
  "phổ biến vũ khí hủy diệt hàng loạt [10]. Bộ Tài chính Hoa Kỳ (OFAC) ban hành Khung cam kết tuân thủ OFAC năm 2019 với năm thành phần: "
  "cam kết của lãnh đạo, đánh giá rủi ro, kiểm soát nội bộ, kiểm thử và kiểm toán, đào tạo [11]. Quy định Part 504 của Sở Dịch vụ Tài chính "
  "New York (NYDFS) yêu cầu các tổ chức tài chính duy trì chương trình giám sát và lọc giao dịch được kiểm thử, hiệu chỉnh, có quản trị dữ liệu "
  "đầy đủ và hằng năm phải xác nhận việc tuân thủ [12]. Hướng dẫn sàng lọc cấm vận của Nhóm Wolfsberg năm 2019 [13] đề cập định nghĩa, "
  "các thành phần của chương trình sàng lọc, cách tiếp cận dựa trên rủi ro, công nghệ, tạo và xử lý cảnh báo, dữ liệu tham chiếu, sàng lọc giao dịch "
  "và quản lý danh sách; hướng dẫn nhấn mạnh việc đánh giá hiệu quả hệ thống bằng kiểm thử có kiểm soát thay vì chỉ dựa vào cấu hình mặc định.")
p("Về học thuật, phần lớn nghiên cứu về học máy cho phòng, chống rửa tiền tập trung vào giám sát giao dịch đáng ngờ [14], [15], [16]. "
  "Mảng sàng lọc cấm vận chủ yếu phát triển trong các sản phẩm thương mại như Oracle EDQ, LexisNexis Firco, SAS và NICE Actimize, "
  "với rất ít công bố định lượng về hiệu quả cấu hình quy tắc. Hình 2 mô tả quy trình sàng lọc điển hình và các bước mà đề tài tập trung tối ưu.")
img("h1_quytrinh.png", "Hình 2. Quy trình sàng lọc cấm vận giao dịch SWIFT và phạm vi tác động của đề tài", 16)
h3("2.1.4. Chuyển đổi chuẩn ISO 20022")
p("SWIFT đã kết thúc giai đoạn song song giữa điện MT và điện ISO 20022 (MX) đối với điện thanh toán xuyên biên giới vào ngày 22/11/2025 [17]. "
  "Điện MX (pacs.008, pacs.009) có cấu trúc chi tiết hơn: tên, địa chỉ được tách thành các trường riêng như tên đường, số nhà, thành phố, "
  "mã quốc gia. Điều này mở ra khả năng sàng lọc theo từng thuộc tính và loại bỏ được một phần cảnh báo sai do tên đường bị nhận nhầm là tên người. "
  "Tuy nhiên, trong thực tế nhiều ngân hàng vẫn điền địa chỉ dạng không cấu trúc hoặc ghép tên với địa chỉ, nên hiệu quả thực tế cần được đánh giá bằng thực nghiệm.")

h2("2.2. Tình hình nghiên cứu trong nước")
p("Khung pháp lý về phòng, chống rửa tiền tại Việt Nam đã được hoàn thiện đáng kể với Luật Phòng, chống rửa tiền số 14/2022/QH15 [18], "
  "Nghị định 19/2023/NĐ-CP [19], Thông tư 27/2025/TT-NHNN thay thế Thông tư 09/2023/TT-NHNN [20] và Nghị định 81/2019/NĐ-CP về phòng, chống "
  "phổ biến vũ khí hủy diệt hàng loạt [21]. Các văn bản này yêu cầu đối tượng báo cáo rà soát khách hàng và giao dịch với danh sách đen, "
  "danh sách cảnh báo. Từ tháng 6/2023, Việt Nam bị FATF đưa vào danh sách các quốc gia bị tăng cường giám sát và vẫn nằm trong danh sách này "
  "sau kỳ họp toàn thể tháng 6/2026, tạo áp lực lớn về nâng cao hiệu quả thực thi.")
p("Các nghiên cứu trong nước về phòng, chống rửa tiền chủ yếu tiếp cận dưới góc độ pháp lý, quản trị rủi ro và kinh nghiệm quốc tế; một số nghiên cứu "
  "ứng dụng học máy cho phát hiện gian lận và giao dịch bất thường. Theo tìm hiểu của học viên, chưa có nghiên cứu thực nghiệm định lượng nào được công bố "
  "về hiệu quả so khớp tên trong sàng lọc cấm vận với dữ liệu khách hàng Việt Nam, đặc biệt là chưa có nghiên cứu phân tích tác động của các đặc thù "
  "về tên và địa chỉ người Việt được trình bày ở mục 2.3.")

h2("2.3. Đặc thù tên và địa chỉ người Việt gây cảnh báo sai")
p("Qua thực tế vận hành hệ thống sàng lọc tại ngân hàng, học viên nhận thấy tên và địa chỉ của khách hàng Việt Nam có ba đặc điểm khiến các quy tắc "
  "so khớp thiết kế cho tên phương Tây hoạt động kém hiệu quả. Đây là điểm xuất phát và cũng là đóng góp chính của đề tài.")
h3("2.3.1. Tên đường thường được đặt theo tên danh nhân")
p("Theo Quy chế đặt tên, đổi tên đường, phố và công trình công cộng ban hành kèm Nghị định 91/2005/NĐ-CP [24], tên đường có thể được đặt theo "
  "tên danh nhân, nhân vật lịch sử; tại các đô thị loại đặc biệt và loại I, các đại lộ được đặt theo tên sự kiện lịch sử đặc biệt hoặc danh nhân tiêu biểu. "
  "Do đó, phần lớn tên đường tại các đô thị Việt Nam là họ tên đầy đủ của một người, ví dụ Trần Hưng Đạo, Lê Lợi, Nguyễn Trãi, Phạm Hùng, Lê Văn Lương, "
  "Nguyễn Văn Cừ. Về hình thức, các tên đường này không khác gì tên của một cá nhân.")
p("Trong điện SWIFT MT, thông tin người chuyển (trường 50K) và người hưởng (trường 59) gồm tối đa bốn dòng, mỗi dòng 35 ký tự, trong đó tên và địa chỉ "
  "được ghi liên tiếp dưới dạng văn bản tự do. Khi hệ thống sàng lọc quét toàn bộ nội dung trường này, một dòng địa chỉ như \"12 PHAM HUNG, NAM TU LIEM\" "
  "có thể khớp với một đối tượng trong danh sách có họ tên tương tự, dù khách hàng không liên quan. Bảng 1 và Hình 3 minh họa cơ chế phát sinh cảnh báo sai này "
  "(các tên trong bảng là ví dụ giả định, không phải đối tượng có thật trong danh sách cấm vận).")
cap("Bảng 1. Minh họa cảnh báo sai do tên đường trùng tên người trong điện MT103")
tbl(["Nội dung trường 59 (người hưởng)", "Mục giả định trong danh sách", "Nguyên nhân khớp"], [
    ["NGUYEN THI MAI / 25 LE VAN LUONG / THANH XUAN HA NOI", "LE VAN LUONG", "Tên đường trùng toàn bộ họ tên"],
    ["CONG TY ABC / 10 TRAN HUNG DAO / HOAN KIEM", "TRAN HUNG", "Tên đường chứa họ và tên"],
    ["DO VAN NAM / 8 PHAM HUNG / NAM TU LIEM", "PHAM HUNG", "Tên đường trùng toàn bộ họ tên"],
], [3700, 2600, 2700])
p("Hướng xử lý được đề tài nghiên cứu gồm: nhận diện phần địa chỉ trong trường văn bản tự do dựa trên dấu hiệu số nhà, từ khóa địa giới hành chính "
  "(PHUONG, QUAN, HUYEN, TP, HA NOI...) và từ điển tên đường; giảm trọng số hoặc loại trừ phần địa chỉ khỏi so khớp tên cá nhân; và đối với điện MX, "
  "chỉ so khớp tên trên trường tên, so khớp địa chỉ trên trường địa chỉ có cấu trúc.")
img("h3_mt103.png", "Hình 3. Cơ chế khớp nhầm do tên đường trùng tên người trong trường 59 của điện MT103 (ví dụ giả định)", 15.5)

h3("2.3.2. Dấu tiếng Việt và hiện tượng trùng tên khi bỏ dấu")
p("Tiếng Việt có 29 chữ cái và 6 thanh điệu, sử dụng các dấu phụ để phân biệt nguyên âm (ă, â, ê, ô, ơ, ư), phụ âm (đ) và thanh điệu. Trong khi đó, "
  "tập ký tự của điện SWIFT MT (tập ký tự X) chỉ gồm chữ Latinh không dấu, chữ số và một số ký hiệu, nên tên khách hàng bắt buộc phải bỏ dấu khi đưa vào điện. "
  "Các danh sách cấm vận quốc tế cũng ghi tên bằng chữ Latinh không dấu. Khi bỏ dấu, nhiều tên vốn khác nhau trở thành một chuỗi duy nhất, như minh họa ở Bảng 2 và Hình 4.")
cap("Bảng 2. Một số nhóm tên tiếng Việt trùng nhau sau khi bỏ dấu")
tbl(["Dạng có dấu", "Dạng không dấu"], [
    ["Hưng, Hùng, Hứng, Hừng", "HUNG"],
    ["Thủy, Thùy, Thụy", "THUY"],
    ["Tuấn, Tuân", "TUAN"],
    ["Anh, Ánh, Ảnh", "ANH"],
    ["Đức, Dực, Dức", "DUC"],
    ["Lan, Lân, Lăn", "LAN"],
    ["Nguyễn Văn Hùng, Nguyễn Văn Hưng", "NGUYEN VAN HUNG"],
], [5000, 4000])
p("Hệ quả là một khách hàng tên Nguyễn Văn Hưng và một đối tượng ghi trong danh sách là NGUYEN VAN HUNG (có thể là Hùng) sẽ khớp tuyệt đối về chuỗi ký tự. "
  "Hiện tượng này làm tăng cảnh báo sai trong sàng lọc khách hàng và giao dịch, đồng thời làm giảm giá trị phân biệt của tên khi so khớp. Đề tài sẽ đo "
  "tỷ lệ va chạm khi bỏ dấu trên mẫu dữ liệu khách hàng (số tên có dấu khác nhau cùng ánh xạ về một chuỗi không dấu) và đánh giá các chiến lược: "
  "so khớp trên tên có dấu khi cả hai phía có dấu (sàng lọc khách hàng nội bộ); bổ sung thuộc tính phụ như năm sinh, quốc tịch để phân biệt khi tên trùng; "
  "và điều chỉnh trọng số của các tên có tần suất cao.")
img("h4_bodau.png", "Hình 4. Nhiều tên tiếng Việt có dấu trở thành một chuỗi không dấu", 14.5)

h3("2.3.3. Phân bố họ người Việt rất lệch")
p("Họ người Việt tập trung vào một số ít họ lớn. Theo nghiên cứu của Lê Trung Hoa [22], họ Nguyễn chiếm khoảng 38,4% dân số, tiếp theo là họ Trần (12,1%), "
  "họ Lê (9,5%) và họ Phạm (7,0%); bốn họ này (Hình 5) chiếm khoảng 67% dân số. Ấn phẩm 100 họ phổ biến ở Việt Nam (Nhà xuất bản Khoa học Xã hội, 2022) [23] "
  "đưa ra con số thấp hơn, khoảng 31,5% dân số mang họ Nguyễn. Cần lưu ý rằng đây là số liệu từ các nghiên cứu và mẫu thống kê dân cư; cơ quan nhà nước "
  "chưa công bố thống kê chính thức về tỷ lệ các họ trên phạm vi toàn quốc. Đề tài sẽ đo phân bố thực tế trên mẫu 10 triệu khách hàng để đối chiếu.")
cap("Bảng 3. Tỷ lệ một số họ phổ biến của người Việt")
tbl(["Họ", "Tỷ lệ theo Lê Trung Hoa [22]", "Tỷ lệ theo [23]", "Tỷ lệ trên mẫu MB"], [
    ["Nguyễn", "38,4%", "khoảng 31,5%", "(đo trong nội dung 1)"],
    ["Trần", "12,1%", "", "(đo trong nội dung 1)"],
    ["Lê", "9,5%", "", "(đo trong nội dung 1)"],
    ["Phạm", "7,0%", "", "(đo trong nội dung 1)"],
    ["Cộng 4 họ", "khoảng 67%", "", "(đo trong nội dung 1)"],
], [2000, 2500, 2000, 2500])
img("h5_ho.png", "Hình 5. Tỷ lệ dân số của bốn họ phổ biến nhất (nguồn: Lê Trung Hoa [22]; cột Các họ khác là phần còn lại)", 13.5)
p("Trong OEDQ, phân cụm theo họ là một cấu hình phổ biến vì đơn giản và giữ lại được phần lớn các cặp khớp đúng. Tuy nhiên, với phân bố như trên, "
  "cụm họ Nguyễn chứa khoảng một phần ba đến hai phần năm toàn bộ bản ghi khách hàng, trong khi hàng trăm họ khác chỉ có số bản ghi rất nhỏ. Phân bố cụm "
  "không đều dẫn đến hai hệ quả: thời gian xử lý tập trung vào một số cụm lớn, làm giảm hiệu quả xử lý song song; và trong các cụm lớn, số cặp so sánh "
  "tăng theo bình phương nên số cảnh báo sai cũng tăng mạnh. Ngoài ra, thứ tự họ, tên đệm, tên của người Việt ngược với thứ tự tên, họ của phương Tây, "
  "nên khi đối tác nước ngoài ghi đảo thứ tự, khóa cụm theo từ đầu tiên sẽ không còn chính xác. Đề tài sẽ so sánh các khóa cụm thay thế như kết hợp họ "
  "với chữ cái đầu của tên, khóa theo từ cuối (tên gọi), khóa theo tập từ đã sắp xếp và khóa ngữ âm.")

h2("2.4. Khoảng trống nghiên cứu và sự cần thiết tiến hành nghiên cứu")
p("Từ tổng quan trên có thể rút ra ba khoảng trống nghiên cứu: (i) thiếu phương pháp kiểm thử định lượng, có thể lặp lại cho hệ thống sàng lọc cấm vận; "
  "(ii) thiếu đánh giá tách biệt tác động của từng bước làm sạch, chuẩn hóa, phân cụm và quy tắc so khớp; (iii) chưa có nghiên cứu về các đặc thù tên, "
  "địa chỉ người Việt trong sàng lọc cấm vận.")
p("Vấn đề đề tài tập trung giải quyết là: hệ thống sàng lọc cấm vận giao dịch SWIFT tại ngân hàng phát sinh khối lượng lớn cảnh báo sai, một phần đáng kể "
  "xuất phát từ đặc thù tên và địa chỉ người Việt, trong khi việc hiệu chỉnh quy tắc hiện nay chủ yếu dựa trên kinh nghiệm, thiếu cơ sở định lượng để chứng minh "
  "rằng giảm cảnh báo không làm tăng rủi ro bỏ sót.")
p("Về tính mới, đề tài lần đầu phân tích định lượng tác động của tên đường theo tên danh nhân, hiện tượng trùng tên khi bỏ dấu và phân bố họ lệch đến "
  "hiệu quả sàng lọc cấm vận, trên mẫu dữ liệu quy mô lớn của một ngân hàng thương mại Việt Nam. Về tính thời sự, Việt Nam đang nằm trong danh sách tăng cường "
  "giám sát của FATF, Thông tư 27/2025/TT-NHNN vừa có hiệu lực và SWIFT đã chuyển hẳn sang ISO 20022. Về ý nghĩa khoa học, đề tài bổ sung bằng chứng thực nghiệm "
  "cho lĩnh vực so khớp tên trong một miền ứng dụng có chi phí bỏ sót rất cao và với một ngôn ngữ có đặc điểm riêng. Về ý nghĩa thực tiễn, kết quả giúp ngân hàng "
  "giảm chi phí xử lý cảnh báo, rút ngắn thời gian xử lý giao dịch và có bằng chứng định lượng phục vụ kiểm toán, thanh tra.")

# ---------------------------------------------------------------- 3. MỤC TIÊU
h1("3. MỤC TIÊU CỦA ĐỀ TÀI")
h2("3.1. Mục tiêu tổng quát")
p("Nâng cao hiệu quả hệ thống sàng lọc cấm vận giao dịch SWIFT tại Ngân hàng TMCP Quân đội thông qua tối ưu hóa có cơ sở định lượng các quy tắc làm sạch, "
  "chuẩn hóa, phân cụm và so khớp trên nền tảng Oracle EDQ, có xét đến đặc thù tên và địa chỉ người Việt.")
h2("3.2. Mục tiêu cụ thể")
b("MT1: Phân tích định lượng các đặc thù tên và địa chỉ người Việt trên mẫu 10 triệu khách hàng: phân bố họ, tỷ lệ trùng tên khi bỏ dấu, tỷ lệ địa chỉ chứa tên đường trùng họ tên người.")
b("MT2: Xây dựng bộ dữ liệu kiểm thử có gán nhãn, kết hợp dữ liệu khách hàng đã khử định danh, danh sách cấm vận công khai và các biến thể tên được sinh có kiểm soát.")
b("MT3: Đề xuất bộ quy tắc làm sạch, chuẩn hóa, phân cụm và so khớp giúp giảm ít nhất 30% cảnh báo sai so với cấu hình hiện hành trong khi duy trì Recall từ 99% trở lên trên bộ dữ liệu kiểm thử.")
b("MT4: Đề xuất quy trình kiểm định và hiệu chỉnh định kỳ hệ thống sàng lọc cấm vận phù hợp với quy định Việt Nam và thông lệ quốc tế.")
h2("3.3. Câu hỏi nghiên cứu")
b("CH1: Việc nhận diện và xử lý riêng phần địa chỉ trong trường tên, địa chỉ của điện SWIFT giảm được bao nhiêu cảnh báo sai do tên đường trùng tên người, và có ảnh hưởng đến Recall không?")
b("CH2: Mức độ trùng tên khi bỏ dấu trong dữ liệu khách hàng là bao nhiêu và chiến lược nào giúp hạn chế cảnh báo sai do hiện tượng này?")
b("CH3: Khóa phân cụm nào cân bằng tốt nhất giữa độ đồng đều kích thước cụm, thời gian xử lý và tỷ lệ giữ lại cặp khớp đúng với phân bố họ người Việt?")
b("CH4: Tổ hợp quy tắc so khớp và ngưỡng nào cho hiệu quả tốt nhất với từng nhóm tên (Việt Nam, Trung Quốc, Ả Rập, Nga, Latinh) và loại thực thể (cá nhân, tổ chức)?")
b("CH5: Dữ liệu có cấu trúc của điện ISO 20022 cải thiện hiệu quả sàng lọc như thế nào so với điện MT dạng văn bản tự do?")

# ---------------------------------------------------------------- 4. PHẠM VI, NỘI DUNG, PHƯƠNG PHÁP
h1("4. PHẠM VI, NỘI DUNG, PHƯƠNG PHÁP NGHIÊN CỨU")
h2("4.1. Đối tượng và phạm vi nghiên cứu")
b("Đối tượng nghiên cứu: quy trình và quy tắc sàng lọc cấm vận theo thời gian thực đối với điện thanh toán quốc tế qua mạng SWIFT (điện chuyển tiền khách hàng và điện chuyển tiền giữa các định chế tài chính). Đề tài không đề cập đến giám sát giao dịch đáng ngờ theo hành vi.")
b("Danh sách đối chiếu: OFAC SDN và danh sách hợp nhất không thuộc SDN, Danh sách trừng phạt hợp nhất của Hội đồng Bảo an Liên Hợp Quốc, Danh sách trừng phạt tài chính hợp nhất của Liên minh châu Âu, danh sách của Vương quốc Anh và danh sách do cơ quan có thẩm quyền Việt Nam công bố.")
b("Thực thể sàng lọc: cá nhân, tổ chức; các thuộc tính phụ gồm quốc gia, thành phố và mã BIC.")
b("Nền tảng thực nghiệm: Oracle Enterprise Data Quality trên môi trường thử nghiệm độc lập tại MB, không kết nối với hệ thống thanh toán thật; một số độ đo đối chứng được cài đặt bằng Python.")
b("Thời gian thực hiện: 06 tháng.")
h2("4.2. Dữ liệu nghiên cứu")
h3("4.2.1. Mẫu dữ liệu khách hàng")
p("Dữ liệu thực nghiệm gồm 10 triệu bản ghi tên và địa chỉ khách hàng được lấy mẫu ngẫu nhiên từ cơ sở dữ liệu khách hàng của MB. Để không thể nhận diện "
  "khách hàng thật, thông tin địa chỉ được hoán đổi ngẫu nhiên giữa các bản ghi, tức là mỗi tên được ghép với địa chỉ của một khách hàng khác. Ngoài tên và địa chỉ, "
  "mẫu dữ liệu không chứa bất kỳ thông tin định danh nào khác như số giấy tờ tùy thân, số tài khoản, ngày sinh, số điện thoại. Việc hoán đổi địa chỉ không làm thay đổi "
  "đặc trưng thống kê của từng trường (phân bố họ, tên đệm, tên, tên đường, địa giới hành chính), là các đặc trưng đề tài cần nghiên cứu, nhưng phá vỡ liên kết giữa "
  "một người cụ thể và nơi ở thật của người đó.")
cap("Bảng 4. Cấu trúc mẫu dữ liệu khách hàng")
tbl(["Trường", "Mô tả", "Ghi chú"], [
    ["ID_MAU", "Mã bản ghi sinh ngẫu nhiên", "Không liên kết được với mã khách hàng thật"],
    ["HO_TEN", "Họ tên khách hàng cá nhân hoặc tên tổ chức, có dấu", "Giữ nguyên dạng lưu trữ trong hệ thống nguồn"],
    ["DIA_CHI", "Địa chỉ dạng văn bản, có dấu", "Đã hoán đổi ngẫu nhiên giữa các bản ghi"],
    ["LOAI_KH", "Cá nhân hoặc tổ chức", "Dùng để phân nhóm khi đánh giá"],
], [1800, 4000, 3200])
h3("4.2.2. Danh sách cấm vận")
p("Các danh sách cấm vận công khai nêu tại mục 4.1 được thu thập ở định dạng XML hoặc CSV, hợp nhất về một cấu trúc chung gồm tên chính, các bí danh, loại thực thể, "
  "quốc tịch, ngày sinh và địa chỉ. Danh sách đang được sử dụng trong hệ thống của MB được dùng làm đối chứng để bảo đảm thực nghiệm phản ánh đúng điều kiện vận hành.")
h3("4.2.3. Bộ dữ liệu kiểm thử có gán nhãn")
p("Do không có sẵn nhãn khớp hoặc không khớp cho dữ liệu thực, đề tài xây dựng bộ dữ liệu kiểm thử theo phương pháp chèn mẫu dương có kiểm soát (Hình 6):")
b("Mẫu âm: các bản ghi khách hàng trong mẫu 10 triệu, sau khi đã loại các bản ghi từng được chuyên viên xác nhận là trùng khớp thật (nếu có), được xem là không khớp. Mọi cảnh báo phát sinh trên mẫu âm là cảnh báo sai.")
b("Mẫu dương: tên các đối tượng trong danh sách cấm vận được biến đổi theo phân loại lỗi trong hướng dẫn của Wolfsberg [13] (Bảng 5), sau đó chèn vào trường tên kèm một địa chỉ lấy ngẫu nhiên từ mẫu khách hàng. Hệ thống phải phát hiện được các bản ghi này.")
b("Điện thanh toán: từ các bản ghi trên, đề tài sinh điện MT103, MT202 (trường 50K, 59, 52A, 57A, 70) và pacs.008, pacs.009 theo đúng quy định độ dài dòng và tập ký tự, trong đó điện MT ghép tên với địa chỉ dạng văn bản tự do, điện MX tách tên và địa chỉ thành các trường có cấu trúc.")
cap("Bảng 5. Các dạng biến thể tên được sinh có kiểm soát")
tbl(["Dạng biến thể", "Ví dụ (từ tên gốc giả định NGUYEN VAN HUNG)"], [
    ["Lỗi gõ: chèn, xóa, thay, hoán vị ký tự", "NGUYEN VAN HUGN, NGUEYN VAN HUNG"],
    ["Đảo thứ tự từ", "HUNG NGUYEN VAN, VAN HUNG NGUYEN"],
    ["Viết tắt, bỏ tên đệm", "NGUYEN V HUNG, NGUYEN HUNG"],
    ["Ghép hoặc tách từ", "NGUYENVAN HUNG"],
    ["Phiên âm khác nhau", "NGUYEN VAN HOUNG, NGUIEN VAN HUNG"],
    ["Cắt cụt do giới hạn 35 ký tự mỗi dòng", "Tên tổ chức dài bị ngắt sang dòng sau"],
    ["Thêm danh xưng, ký tự đặc biệt", "MR NGUYEN VAN HUNG, NGUYEN-VAN-HUNG"],
], [4000, 5000])
img("h6_dulieu.png", "Hình 6. Quy trình xây dựng dữ liệu kiểm thử và thực nghiệm", 16)
h3("4.2.4. Bảo vệ dữ liệu cá nhân và tuân thủ")
p("Việc xử lý dữ liệu tuân thủ Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 [25] và Nghị định 356/2025/NĐ-CP [26] cùng quy định nội bộ của MB. Cụ thể: "
  "việc lấy mẫu và hoán đổi địa chỉ do bộ phận quản lý dữ liệu của ngân hàng thực hiện; toàn bộ thực nghiệm diễn ra trong môi trường của ngân hàng, dữ liệu không được "
  "sao chép ra ngoài; luận văn và các công bố chỉ trình bày số liệu tổng hợp (tỷ lệ, phân bố, chỉ số hiệu quả) và các ví dụ giả định, không trình bày bất kỳ bản ghi thật nào; "
  "cấu hình quy tắc chi tiết của ngân hàng chỉ được mô tả ở mức nguyên lý. Học viên sẽ xin phê duyệt của MB trước khi sử dụng dữ liệu.")

h2("4.3. Nội dung nghiên cứu")
h3("Nội dung 1: Khảo sát hiện trạng và phân tích đặc trưng dữ liệu")
b("Nghiên cứu tài liệu [1] đến [26] và tài liệu kỹ thuật OEDQ (các bộ xử lý làm sạch, chuẩn hóa, Advanced Match, Watchlist Screening).")
b("Phỏng vấn bán cấu trúc 5 đến 7 chuyên viên tuân thủ và kỹ thuật về quy trình xử lý cảnh báo; thống kê nguyên nhân cảnh báo sai trên một mẫu cảnh báo đã xử lý (chỉ lấy số liệu tổng hợp).")
b("Phân tích mẫu 10 triệu khách hàng: phân bố họ, tên đệm, tên; số chuỗi tên không dấu tương ứng với nhiều tên có dấu khác nhau; tỷ lệ địa chỉ có tên đường trùng với họ tên phổ biến.")
b("Kết quả: mô hình quy trình sàng lọc hiện tại (BPMN), phân loại nguyên nhân cảnh báo sai, bộ số liệu đặc trưng dữ liệu và cấu hình nền (baseline).")
h3("Nội dung 2: Xây dựng bộ dữ liệu kiểm thử chuẩn")
b("Thu thập, hợp nhất danh sách cấm vận công khai; xây dựng công cụ sinh biến thể tên và sinh điện MT, MX như mục 4.2.3.")
b("Kiểm tra chéo nhãn trên một mẫu ngẫu nhiên với chuyên viên tuân thủ, đánh giá mức độ đồng thuận bằng hệ số Cohen's Kappa.")
b("Kết quả: bộ dữ liệu kiểm thử có gán nhãn và công cụ sinh dữ liệu có thể tái sử dụng cho các lần kiểm thử định kỳ.")
h3("Nội dung 3: Tối ưu quy tắc làm sạch và chuẩn hóa")
b("Nhận diện phần địa chỉ trong trường tên, địa chỉ của điện MT bằng quy tắc dựa trên số nhà, từ khóa địa giới hành chính và từ điển tên đường được trích từ chính mẫu dữ liệu; giảm trọng số hoặc loại trừ phần địa chỉ khi so khớp tên cá nhân.")
b("Chiến lược xử lý dấu: chuẩn hóa Unicode, bỏ dấu có kiểm soát (Đ thành D), so khớp tên có dấu khi cả hai phía có dấu, bổ sung thuộc tính phụ khi tên không dấu trùng.")
b("Chuẩn hóa tên tổ chức: tiền tố, hậu tố pháp lý (CONG TY TNHH, CTCP, JSC, CO., LTD), từ nhiễu, danh xưng, ký tự đặc biệt.")
b("Phương pháp: thực nghiệm loại bỏ từng thành phần (ablation study), mỗi lần bật hoặc tắt một quy tắc so với cấu hình nền và đo thay đổi của các chỉ số tại mục 4.4.")
h3("Nội dung 4: Tối ưu phân cụm, quy tắc so khớp và ngưỡng")
b("So sánh các khóa phân cụm: theo họ; họ kết hợp chữ cái đầu của tên; theo từ cuối; tập từ đã sắp xếp; mã ngữ âm; n-gram. Với mỗi khóa đo phân bố kích thước cụm (kích thước lớn nhất, hệ số Gini), số cặp so sánh, thời gian xử lý và tỷ lệ giữ lại cặp khớp đúng.")
b("So sánh các phép so sánh của Advanced Match (khớp chính xác, khoảng cách chỉnh sửa, số từ khớp, khớp có hoán vị) và các độ đo đối chứng Jaro-Winkler, Levenshtein chuẩn hóa, TF-IDF trên n-gram.")
b("Điều chỉnh trọng số theo tần suất tên: các tên có tần suất cao như họ Nguyễn, tên đệm Văn, Thị mang ít thông tin phân biệt nên được gán trọng số thấp hơn, theo nguyên lý TF-IDF.")
b("Tối ưu ngưỡng bằng tìm kiếm lưới với hàm mục tiêu tối thiểu số cảnh báo sai, ràng buộc Recall từ 99% trở lên; so sánh sàng lọc theo thuộc tính trên điện MX với sàng lọc văn bản tự do trên điện MT.")
h3("Nội dung 5: Quy trình kiểm định, hiệu chỉnh định kỳ và đánh giá tổng thể")
b("Xây dựng quy trình kiểm định gồm: kiểm tra tính đầy đủ, kịp thời của danh sách; kiểm tra toàn vẹn dữ liệu đầu vào; kiểm thử hiệu quả so khớp bằng bộ dữ liệu chuẩn; kiểm thử hồi quy khi thay đổi quy tắc; chỉ số giám sát và quy trình phê duyệt thay đổi.")
b("Đối chiếu với Luật Phòng, chống rửa tiền 2022, Thông tư 27/2025/TT-NHNN, Khung tuân thủ OFAC, NYDFS Part 504 và hướng dẫn Wolfsberg.")
b("Đánh giá tổng thể bộ cấu hình đề xuất; lấy ý kiến chuyên gia tại một buổi tọa đàm chuyên môn.")

h2("4.4. Phương pháp đánh giá")
p("Gọi TP là số mẫu dương được phát hiện, FN là số mẫu dương bị bỏ sót, FP là số cảnh báo phát sinh trên mẫu âm. Các chỉ số đánh giá chính gồm:")
eq("Precision = TP / (TP + FP)          Recall = TP / (TP + FN)")
eq("F2 = 5 × Precision × Recall / (4 × Precision + Recall)")
p("Chỉ số F2 được sử dụng thay cho F1 vì trong sàng lọc cấm vận, chi phí bỏ sót lớn hơn nhiều so với chi phí của một cảnh báo sai; F2 coi trọng Recall gấp đôi Precision. "
  "Bên cạnh đó, đề tài sử dụng các chỉ số vận hành tại Bảng 6.")
cap("Bảng 6. Các chỉ số đánh giá")
tbl(["Chỉ số", "Ý nghĩa"], [
    ["Số cảnh báo trên 1.000 giao dịch", "Khối lượng công việc của chuyên viên"],
    ["Tỷ lệ cảnh báo sai do địa chỉ", "Đo riêng tác động của đặc thù tên đường"],
    ["Tỷ lệ giữ lại cặp khớp đúng (pair completeness)", "Khả năng phân cụm không loại bỏ cặp khớp đúng"],
    ["Tỷ lệ giảm số cặp so sánh (reduction ratio)", "Hiệu quả tính toán của phân cụm"],
    ["Kích thước cụm lớn nhất, hệ số Gini của kích thước cụm", "Mức độ đồng đều của phân cụm"],
    ["Thông lượng, độ trễ xử lý", "Khả năng đáp ứng sàng lọc thời gian thực"],
], [4500, 4500])
p("Để khẳng định sự khác biệt giữa hai cấu hình là có ý nghĩa thống kê, đề tài sử dụng kiểm định McNemar cho các quyết định trên cùng tập dữ liệu và khoảng tin cậy "
  "bootstrap 95% cho các chỉ số. Kết quả được báo cáo theo từng nhóm tên (Việt Nam, Trung Quốc, Ả Rập, Nga, Latinh) và loại thực thể.")

h2("4.5. Công cụ sử dụng")
b("Oracle Enterprise Data Quality: Director, các bộ xử lý làm sạch, chuẩn hóa, Advanced Match, Watchlist Screening; cơ sở dữ liệu Oracle lưu kết quả thực nghiệm.")
b("Python (pandas, RapidFuzz, jellyfish, SciPy) để sinh dữ liệu kiểm thử, cài đặt độ đo đối chứng và phân tích thống kê; Git để quản lý phiên bản cấu hình và kịch bản thực nghiệm, bảo đảm khả năng lặp lại.")
h2("4.6. Sự cần thiết của việc mời chuyên gia")
p("Đề tài cần mời 01 đến 02 chuyên gia trong nước để tư vấn và thẩm định kết quả: chuyên gia nghiệp vụ tuân thủ, phòng, chống rửa tiền tại ngân hàng thương mại "
  "(tối thiểu 5 năm kinh nghiệm xử lý cảnh báo cấm vận) và chuyên gia kỹ thuật về chất lượng dữ liệu, OEDQ (tối thiểu 3 năm kinh nghiệm triển khai). "
  "Chuyên gia tham gia phỏng vấn khảo sát, kiểm tra chéo nhãn dữ liệu và góp ý quy trình kiểm định. Không thuê chuyên gia nước ngoài.")
h2("4.7. Các hoạt động phục vụ nghiên cứu")
b("Khảo sát, phỏng vấn chuyên gia phục vụ nội dung 1 và kiểm tra chất lượng nhãn dữ liệu ở nội dung 2.")
b("Tọa đàm chuyên môn (01 buổi) lấy ý kiến về bộ cấu hình và quy trình kiểm định đề xuất.")
b("Không có hoạt động thuê ngoài, đoàn ra, đoàn vào.")

# ---------------------------------------------------------------- 5. KHẢ THI
h1("5. TÍNH KHẢ THI CỦA NGHIÊN CỨU")
h2("5.1. Khả năng thành công")
p("Đề tài có khả năng thành công cao vì: (i) học viên trực tiếp tham gia xây dựng và vận hành hệ thống sàng lọc cấm vận trên OEDQ tại MB nên nắm vững công cụ, "
  "nghiệp vụ và nguồn gốc các cảnh báo sai; (ii) dữ liệu thực nghiệm quy mô lớn đã được xác định nguồn và phương án khử định danh; (iii) phương pháp thực nghiệm loại bỏ "
  "từng thành phần và tối ưu ngưỡng đã được kiểm chứng trong lĩnh vực liên kết bản ghi; (iv) mục tiêu định lượng phù hợp với mức cải thiện thường đạt được khi tinh chỉnh "
  "quy tắc theo thông lệ ngành.")
h2("5.2. Rủi ro và biện pháp phòng ngừa")
cap("Bảng 7. Rủi ro chính và biện pháp")
tbl(["Rủi ro", "Biện pháp"], [
    ["Chậm phê duyệt sử dụng dữ liệu khách hàng", "Đăng ký sớm từ tháng thứ nhất; trong thời gian chờ, chuẩn bị công cụ và chạy thử trên dữ liệu tổng hợp"],
    ["Thời gian 6 tháng hạn chế", "Ưu tiên ba đặc thù tên, địa chỉ người Việt; các thực nghiệm phụ (so sánh MT và MX) thực hiện nếu còn thời gian"],
    ["Tài nguyên tính toán khi xử lý 10 triệu bản ghi", "Thực nghiệm trên mẫu con 1 triệu bản ghi để chọn cấu hình, chỉ chạy cấu hình tốt nhất trên toàn bộ mẫu"],
    ["Nhãn mẫu âm có thể chứa trùng khớp thật chưa phát hiện", "Rà soát các cặp có điểm khớp rất cao với chuyên viên tuân thủ trước khi tính chỉ số"],
], [3600, 5400])
h2("5.3. Năng lực của chủ nhiệm đề tài và người hướng dẫn")
p("Chủ nhiệm đề tài Nguyễn Văn Phê đang công tác tại Ngân hàng TMCP Quân đội, trực tiếp tham gia xây dựng quy tắc làm sạch, chuẩn hóa dữ liệu và cấu hình so khớp nâng cao "
  "trên OEDQ cho hệ thống sàng lọc cấm vận giao dịch SWIFT, hiểu rõ nghiệp vụ thanh toán quốc tế và yêu cầu tuân thủ. Người hướng dẫn khoa học: TS. Đỗ Trung Anh.")
h2("5.4. Điều kiện cơ sở vật chất")
p("Học viện Công nghệ Bưu chính Viễn thông cung cấp thư viện và cơ sở dữ liệu học thuật. Thực nghiệm OEDQ được thực hiện trên môi trường thử nghiệm độc lập do MB cho phép sử dụng, "
  "tách biệt hoàn toàn với hệ thống vận hành thật.")
cap("Bảng 8. Thiết bị, cơ sở vật chất sử dụng")
tbl(["TT", "Tên thiết bị", "Mục đích sử dụng", "Cơ quan quản lý"], [
    ["1", "Máy chủ, máy ảo môi trường thử nghiệm Oracle EDQ", "Chạy thực nghiệm làm sạch, chuẩn hóa, phân cụm, so khớp", "Ngân hàng TMCP Quân đội"],
    ["2", "Máy trạm phân tích dữ liệu trong mạng nội bộ ngân hàng", "Sinh dữ liệu kiểm thử, phân tích thống kê bằng Python", "Ngân hàng TMCP Quân đội"],
    ["3", "Thư viện, cơ sở dữ liệu học thuật", "Tra cứu tài liệu", "Học viện Công nghệ Bưu chính Viễn thông"],
], [600, 3000, 3200, 2200])

# ---------------------------------------------------------------- 6. KẾ HOẠCH
h1("6. KẾ HOẠCH TRIỂN KHAI")
p("Tiến độ thực hiện các nội dung nghiên cứu được tóm tắt ở Hình 7 và chi tiết ở Bảng 9.")
img("h7_gantt.png", "Hình 7. Tiến độ thực hiện các nội dung nghiên cứu trong 06 tháng", 16)
cap("Bảng 9. Kế hoạch thực hiện trong 06 tháng")
tbl(["STT", "Nội dung, công việc", "Thời gian", "Người thực hiện", "Kết quả, sản phẩm"], [
    ["1", "Nội dung 1: Khảo sát hiện trạng, phân tích đặc trưng dữ liệu", "T1", "Chủ nhiệm", "Báo cáo hiện trạng, số liệu đặc trưng"],
    ["1.1", "Tổng quan tài liệu, đăng ký sử dụng dữ liệu", "T1", "Chủ nhiệm", "Báo cáo tổng quan"],
    ["1.2", "Phỏng vấn chuyên gia; phân tích phân bố họ, trùng tên khi bỏ dấu, tên đường trùng tên người", "T1", "Chủ nhiệm, chuyên gia", "Bảng số liệu đặc trưng; cấu hình nền"],
    ["2", "Nội dung 2: Xây dựng bộ dữ liệu kiểm thử", "T2", "Chủ nhiệm", "Bộ dữ liệu có gán nhãn"],
    ["2.1", "Hợp nhất danh sách cấm vận; sinh biến thể tên và điện MT, MX", "T2", "Chủ nhiệm", "Công cụ sinh dữ liệu"],
    ["2.2", "Kiểm tra chéo nhãn", "T2", "Chủ nhiệm, chuyên gia", "Báo cáo chất lượng nhãn"],
    ["3", "Nội dung 3: Tối ưu làm sạch, chuẩn hóa", "T3", "Chủ nhiệm", "Bộ quy tắc chuẩn hóa"],
    ["3.1", "Nhận diện địa chỉ, xử lý dấu, chuẩn hóa tên tổ chức; thực nghiệm ablation", "T3", "Chủ nhiệm", "Kết quả thực nghiệm"],
    ["4", "Nội dung 4: Tối ưu phân cụm, so khớp, ngưỡng", "T3-T4", "Chủ nhiệm", "Cấu hình tối ưu"],
    ["4.1", "So sánh khóa phân cụm; quy tắc so khớp; trọng số theo tần suất", "T3-T4", "Chủ nhiệm", "Bảng so sánh chỉ số"],
    ["4.2", "Tối ưu ngưỡng, kiểm định thống kê, so sánh MT và MX", "T4", "Chủ nhiệm", "Báo cáo kiểm định"],
    ["5", "Nội dung 5: Quy trình kiểm định và đánh giá tổng thể", "T5", "Chủ nhiệm", "Quy trình kiểm định"],
    ["5.1", "Xây dựng quy trình kiểm định; tọa đàm lấy ý kiến chuyên gia", "T5", "Chủ nhiệm, chuyên gia", "Tài liệu quy trình; biên bản tọa đàm"],
    ["6", "Nội dung 6: Công bố và tổng kết", "T4-T6", "Chủ nhiệm, người hướng dẫn", "Bài báo, luận văn"],
    ["6.1", "Báo cáo tiến độ giữa kỳ", "T3", "Chủ nhiệm", "Báo cáo giữa kỳ"],
    ["6.2", "Viết và gửi bài báo", "T5-T6", "Chủ nhiệm, người hướng dẫn", "01 bài báo"],
    ["6.3", "Hoàn thiện luận văn", "T6", "Chủ nhiệm", "Luận văn thạc sĩ"],
], [700, 3300, 1000, 1600, 2400])

# ---------------------------------------------------------------- 7. KẾT QUẢ
h1("7. KẾT QUẢ ĐỀ TÀI")
h2("7.1. Dự kiến kết quả nghiên cứu")
b("Bộ số liệu định lượng về ba đặc thù tên, địa chỉ người Việt trên mẫu 10 triệu khách hàng: phân bố họ, mức độ trùng tên khi bỏ dấu, tỷ lệ địa chỉ có tên đường trùng tên người.")
b("Bộ dữ liệu kiểm thử có gán nhãn và công cụ sinh dữ liệu, điện thanh toán tổng hợp có thể tái sử dụng cho kiểm thử định kỳ.")
b("Kết quả thực nghiệm về tác động của từng thành phần trong chuỗi xử lý đến Precision, Recall, F2, số cảnh báo và hiệu năng.")
b("Bộ quy tắc làm sạch, chuẩn hóa, phân cụm và so khớp phù hợp với đặc thù tên, địa chỉ người Việt, mục tiêu giảm ít nhất 30% cảnh báo sai với Recall từ 99% trở lên.")
b("Quy trình kiểm định và hiệu chỉnh định kỳ hệ thống sàng lọc cấm vận.")
p("Về ý nghĩa khoa học, đề tài bổ sung bằng chứng thực nghiệm về so khớp tên cho tiếng Việt, một ngôn ngữ có dấu và phân bố họ đặc biệt, trong miền ứng dụng có chi phí bỏ sót cao. "
  "Về tác động đến ngành, kết quả làm cơ sở để các ngân hàng chuẩn hóa việc kiểm thử, hiệu chỉnh hệ thống sàng lọc.")
h2("7.2. Dự kiến kết quả công bố, đào tạo")
cap("Bảng 10. Kết quả công bố, đào tạo")
tbl(["TT", "Kết quả", "Số lượng", "Ghi chú"], [
    ["1", "Bài báo trên tạp chí quốc tế có uy tín", "0", ""],
    ["2", "Bằng độc quyền sáng chế, giải pháp hữu ích", "0", ""],
    ["3", "Bài báo trên tạp chí trong nước", "01", "Tạp chí Ngân hàng, Tạp chí Khoa học và Đào tạo Ngân hàng hoặc tạp chí chuyên ngành công nghệ thông tin trong nước"],
    ["4", "Báo cáo hội nghị, hội thảo khoa học", "0", "Có thể thay thế cho mục 3 tùy tiến độ"],
    ["5", "Kết quả khác", "03", "Bộ dữ liệu kiểm thử và công cụ sinh dữ liệu; bộ quy tắc đề xuất; quy trình kiểm định"],
    ["6", "Đào tạo học viên cao học", "01", "Luận văn thạc sĩ Hệ thống thông tin của chủ nhiệm đề tài"],
], [600, 3300, 1100, 4000])
h2("7.3. Tác động xã hội của đề tài")
b("Góp phần nâng cao năng lực thực thi các biện pháp trừng phạt tài chính có mục tiêu của hệ thống ngân hàng Việt Nam, hỗ trợ mục tiêu đưa Việt Nam ra khỏi danh sách tăng cường giám sát của FATF.")
b("Giảm số khách hàng hợp pháp bị giữ giao dịch do cảnh báo sai, đặc biệt là những người có họ tên phổ biến hoặc cư trú trên các tuyến phố mang tên danh nhân.")
b("Giảm rủi ro bị xử phạt và mất quan hệ ngân hàng đại lý do vi phạm cấm vận, qua đó bảo vệ hoạt động thanh toán xuất nhập khẩu.")
b("Cung cấp tài liệu tham khảo cho giảng dạy về hệ thống thông tin trong lĩnh vực tài chính, ngân hàng.")
h2("7.4. Khả năng ứng dụng và phương thức chuyển giao")
p("Kết quả có thể ứng dụng trực tiếp tại Ngân hàng TMCP Quân đội và các ngân hàng thương mại khác đang sử dụng OEDQ hoặc giải pháp sàng lọc tương tự; bộ dữ liệu kiểm thử "
  "và quy trình kiểm định không phụ thuộc sản phẩm. Phương thức chuyển giao gồm báo cáo kỹ thuật, tài liệu hướng dẫn và buổi chia sẻ kết quả. Công cụ sinh dữ liệu tổng hợp "
  "có thể công bố mã nguồn mở với điều kiện không chứa dữ liệu thật.")

# ---------------------------------------------------------------- 8, 9
h1("8. THÔNG TIN KHÁC CÓ LIÊN QUAN")
p("Chủ nhiệm đề tài chưa nhận tài trợ nghiên cứu từ Quỹ NAFOSTED, nguồn ngân sách nhà nước hoặc nguồn khác.")
h1("9. DỰ TOÁN KINH PHÍ THỰC HIỆN ĐỀ TÀI")
p("Dự toán kinh phí được lập riêng theo mẫu Mau-Thuyetminh-P2-Dutoan (tệp Excel).")

# ---------------------------------------------------------------- TLTK
REFS = [
 "Fellegi, I. P., & Sunter, A. B. (1969). A theory for record linkage. Journal of the American Statistical Association, 64(328), 1183-1210.",
 "Winkler, W. E. (1990). String comparator metrics and enhanced decision rules in the Fellegi-Sunter model of record linkage. Proceedings of the Section on Survey Research Methods, American Statistical Association, 354-369.",
 "Cohen, W. W., Ravikumar, P., & Fienberg, S. E. (2003). A comparison of string distance metrics for name-matching tasks. Proceedings of the IJCAI-03 Workshop on Information Integration on the Web (IIWeb-03).",
 "Branting, L. K. (2003). A comparative evaluation of name-matching algorithms. Proceedings of the 9th International Conference on Artificial Intelligence and Law (ICAIL 2003), ACM.",
 "Christen, P. (2012). Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection. Springer.",
 "Papadakis, G., Skoutas, D., Thanos, E., & Palpanas, T. (2020). Blocking and filtering techniques for entity resolution: A survey. ACM Computing Surveys, 53(2). https://doi.org/10.1145/3377455",
 "Mudgal, S., et al. (2018). Deep learning for entity matching: A design space exploration. Proceedings of the 2018 International Conference on Management of Data (SIGMOD '18), ACM. https://doi.org/10.1145/3183713.3196926",
 "Li, Y., Li, J., Suhara, Y., Doan, A., & Tan, W.-C. (2021). Deep entity matching with pre-trained language models. PVLDB, 14(1), 50-60.",
 "Peeters, R., Steiner, A., & Bizer, C. (2025). Entity matching using large language models. Proceedings of the 28th International Conference on Extending Database Technology (EDBT 2025), 529-541.",
 "FATF (2012, cập nhật). International Standards on Combating Money Laundering and the Financing of Terrorism & Proliferation: The FATF Recommendations.",
 "U.S. Department of the Treasury, OFAC (2019). A Framework for OFAC Compliance Commitments.",
 "New York State Department of Financial Services (2016). 3 NYCRR Part 504: Banking Division Transaction Monitoring and Filtering Program Requirements and Certifications.",
 "The Wolfsberg Group (2019). Wolfsberg Guidance on Sanctions Screening.",
 "Chen, Z., et al. (2018). Machine learning techniques for anti-money laundering (AML) solutions in suspicious transaction detection: a review. Knowledge and Information Systems, 57(2), 245-285. https://doi.org/10.1007/s10115-017-1144-z",
 "Weber, M., et al. (2019). Anti-money laundering in Bitcoin: Experimenting with graph convolutional networks for financial forensics. KDD Workshop on Anomaly Detection in Finance.",
 "Altman, E., et al. (2023). Realistic synthetic financial transactions for anti-money laundering models. Advances in Neural Information Processing Systems 36 (NeurIPS 2023), Datasets and Benchmarks Track.",
 "SWIFT. ISO 20022 for Financial Institutions: Cross-border Payments and Reporting Plus (CBPR+); giai đoạn song song MT và MX kết thúc ngày 22/11/2025.",
 "Quốc hội (2022). Luật Phòng, chống rửa tiền số 14/2022/QH15 ngày 15/11/2022.",
 "Chính phủ (2023). Nghị định 19/2023/NĐ-CP ngày 28/4/2023 quy định chi tiết một số điều của Luật Phòng, chống rửa tiền.",
 "Ngân hàng Nhà nước Việt Nam (2025). Thông tư 27/2025/TT-NHNN ngày 15/9/2025 hướng dẫn thực hiện Luật Phòng, chống rửa tiền (thay thế Thông tư 09/2023/TT-NHNN).",
 "Chính phủ (2019). Nghị định 81/2019/NĐ-CP ngày 11/11/2019 về phòng, chống phổ biến vũ khí hủy diệt hàng loạt.",
 "Lê Trung Hoa (2005). Họ và tên người Việt Nam. Nhà xuất bản Khoa học Xã hội.",
 "100 họ phổ biến ở Việt Nam (2022). Nhà xuất bản Khoa học Xã hội.",
 "Chính phủ (2005). Nghị định 91/2005/NĐ-CP ngày 11/7/2005 ban hành Quy chế đặt tên, đổi tên đường, phố và công trình công cộng.",
 "Quốc hội (2025). Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15.",
 "Chính phủ (2025). Nghị định 356/2025/NĐ-CP ngày 31/12/2025 quy định chi tiết một số điều và biện pháp thi hành Luật Bảo vệ dữ liệu cá nhân.",
]
