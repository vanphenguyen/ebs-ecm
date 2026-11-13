import re
p = 'full_content.py'
s = open(p, encoding='utf8').read()

def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (s.count(old), old[:90])
    s = s.replace(old, new)

def insert_before(anchor, text):
    global s
    assert s.count(anchor) == 1, anchor
    s = s.replace(anchor, text + anchor)

# --------------------------------------------------------------- bỏ tên giải pháp thương mại
rep('(các bộ xử lý làm sạch, chuẩn hóa, Advanced Match, Watchlist Screening).")', '(các bộ xử lý làm sạch, chuẩn hóa, phân tách cú pháp, khóa ngữ âm, Advanced Match).")')
rep('b("Oracle Enterprise Data Quality: Director, các bộ xử lý làm sạch, chuẩn hóa, Advanced Match, Watchlist Screening; cơ sở dữ liệu Oracle lưu kết quả thực nghiệm.")',
    'b("Oracle Enterprise Data Quality: Director, các bộ xử lý làm sạch, chuẩn hóa, phân tách cú pháp, khóa ngữ âm, Advanced Match; cơ sở dữ liệu Oracle lưu kết quả thực nghiệm.")')

# --------------------------------------------------------------- renumber 2.1.x
rep('h3("2.1.4. Chuyển đổi chuẩn ISO 20022")', 'h3("2.1.5. Chuyển đổi chuẩn ISO 20022")')
rep('h3("2.1.3. Sàng lọc cấm vận: quy định và thông lệ quốc tế")', 'h3("2.1.4. Sàng lọc cấm vận: quy định và thông lệ quốc tế")')
rep('h3("2.1.2. Phân khối và phân cụm trong so khớp quy mô lớn")', 'h3("2.1.3. Phân khối và phân cụm trong so khớp quy mô lớn")')

A = '''h3("2.1.2. Các độ đo tương đồng chuỗi và thuật toán ngữ âm")
p("Các hệ thống so khớp tên dựa trên hai nhóm kỹ thuật chính: độ đo tương đồng chuỗi, đo mức giống nhau về ký tự hoặc về từ, và thuật toán ngữ âm, "
  "mã hóa chuỗi theo cách đọc để các cách viết khác nhau của cùng một âm cho ra cùng một mã. Phần này trình bày các kỹ thuật tiêu biểu và phân tích "
  "mức độ phù hợp của chúng với tên tiếng Việt.")
p("Khoảng cách Levenshtein [36] giữa hai chuỗi s1 và s2 là số phép chèn, xóa, thay thế ký tự tối thiểu để biến chuỗi này thành chuỗi kia. Để so sánh "
  "giữa các cặp có độ dài khác nhau, khoảng cách thường được chuẩn hóa thành độ tương đồng:")
eq("sim_Lev(s1, s2) = 1 - d(s1, s2) / max(|s1|, |s2|)")
p("Độ đo Jaro [37] được phát triển cho bài toán liên kết dữ liệu điều tra dân số. Gọi m là số ký tự khớp (hai ký tự giống nhau và cách nhau không quá "
  "một nửa độ dài chuỗi dài hơn trừ một), t là một nửa số ký tự khớp nhưng sai thứ tự, độ đo Jaro được tính:")
eq("sim_J = (1/3) × ( m/|s1| + m/|s2| + (m - t)/m )")
p("Winkler [2] bổ sung phần thưởng cho các chuỗi có chung tiền tố, với l là độ dài tiền tố chung (tối đa 4) và p là hệ số tỷ lệ (thường bằng 0,1):")
eq("sim_JW = sim_J + l × p × (1 - sim_J)")
p("Với tên nhiều từ, các độ đo dựa trên tập hợp từ hoặc n-gram ký tự thường được sử dụng, như hệ số Jaccard |A ∩ B| / |A ∪ B| hoặc độ tương đồng cosine "
  "trên vectơ trọng số TF-IDF, trong đó trọng số của một từ tỷ lệ nghịch với tần suất xuất hiện của nó trong toàn bộ dữ liệu [3]. Nhóm độ đo này không phụ thuộc "
  "thứ tự từ và tự nhiên giảm vai trò của các từ phổ biến.")
p("Về thuật toán ngữ âm, Soundex [41] giữ chữ cái đầu và mã hóa các phụ âm tiếp theo thành chữ số theo nhóm âm (B, F, P, V thành 1; C, G, J, K, Q, S, X, Z thành 2; "
  "D, T thành 3; L thành 4; M, N thành 5; R thành 6), bỏ nguyên âm và các chữ H, W, Y, gộp các mã liền nhau trùng lặp và cắt hoặc bổ sung để được bốn ký tự. "
  "Metaphone và Double Metaphone [27] sử dụng tập quy tắc phức tạp hơn, mô phỏng cách phát âm tiếng Anh, ví dụ TH được mã hóa thành âm θ (ký hiệu 0), PH thành F.")
p("Để đánh giá mức độ phù hợp với tên tiếng Việt, học viên đã chạy hai thuật toán Soundex và Metaphone (cài đặt trong thư viện jellyfish của Python) trên một số cặp "
  "tên tiếng Việt không dấu. Kết quả ở Bảng {b_soundex} cho thấy cả hai thuật toán đều mắc hai loại lỗi: không gộp được các cách viết của cùng một tên "
  "(PHUONG và FUONG với Soundex; NGHIA và NGIA, NGUYEN và NGUEN với Metaphone) và gộp nhầm các tên khác nhau (THAO, THU, THOA cùng mã T000 và 0; HUNG và HUONG cùng mã).")
cap("Bảng {b_soundex}. Kết quả Soundex và Metaphone trên một số tên tiếng Việt không dấu")
tbl(["Tên", "Soundex", "Metaphone", "Nhận xét"], [
    ["PHUONG / FUONG", "P520 / F520", "FNK / FNK", "Soundex tách nhầm hai cách viết của cùng tên"],
    ["NGHIA / NGIA", "N200 / N200", "NKH / NJ", "Metaphone tách nhầm"],
    ["NGUYEN / NGUEN", "N250 / N250", "NKYN / NKN", "Metaphone tách nhầm"],
    ["GIANG / DANG", "G520 / D520", "JNK / TNK", "Cả hai không phản ánh phương ngữ D, GI"],
    ["TRUNG / CHUNG", "T652 / C520", "TRNK / XNK", "Cả hai không phản ánh việc không phân biệt TR, CH"],
    ["HUYNH / HOANG", "H500 / H520", "HNH / HNK", "Họ tương đương nhưng khác mã: cần bảng tham chiếu"],
    ["THAO, THU, THOA", "T000", "0", "Gộp nhầm nhiều tên khác nhau do coi TH là âm tiếng Anh"],
    ["HUNG / HUONG", "H520 / H520", "HNK / HNK", "Gộp nhầm hai tên khác nhau"],
], [2200, 1900, 1900, 3000])
p("Tương tự, độ đo Jaro-Winkler cho điểm rất cao với các cặp tên tiếng Việt khác nhau nhưng chung họ và tên đệm, trong khi lại cho điểm thấp với cùng một người "
  "bị ghi đảo thứ tự tên (Bảng {b_jw}). Nguyên nhân là phần lớn độ dài chuỗi nằm ở họ và tên đệm phổ biến, còn tên gọi, thành phần có giá trị phân biệt nhất, "
  "lại rất ngắn. Các kết quả này cho thấy không thể áp dụng nguyên trạng các kỹ thuật được thiết kế cho tiếng Anh, và là cơ sở để đề tài đề xuất trọng số theo tần suất "
  "và khóa ngữ âm riêng cho tiếng Việt.")
cap("Bảng {b_jw}. Độ tương đồng Jaro-Winkler và khoảng cách Levenshtein của một số cặp tên")
tbl(["Cặp tên", "Jaro-Winkler", "Levenshtein", "Thực tế"], [
    ["NGUYEN VAN HUNG / NGUYEN VAN HUONG", "0,988", "1", "Hai người khác nhau"],
    ["NGUYEN VAN HUNG / NGUYEN VAN HUY", "0,959", "2", "Hai người khác nhau"],
    ["LE VAN LUONG / LE VAN LONG", "0,983", "1", "Hai tên khác nhau"],
    ["NGUYEN THI LAN / NGUYEN THI LAN ANH", "0,956", "4", "Hai người khác nhau"],
    ["TRAN VAN NAM / NAM TRAN VAN", "0,793", "7", "Cùng một người, đảo thứ tự"],
], [3900, 1500, 1500, 2100])

'''
insert_before('h3("2.1.3. Phân khối và phân cụm trong so khớp quy mô lớn")', A)

B = '''h3("2.1.6. Cấu trúc dữ liệu điện thanh toán SWIFT")
p("Hiểu rõ cấu trúc điện thanh toán là điều kiện để xác định trường nào cần sàng lọc và cách trích xuất dữ liệu. Điện MT103 dùng cho chuyển tiền khách hàng "
  "và MT202 dùng cho chuyển tiền giữa các định chế tài chính [39]. Các trường chứa thông tin về bên tham gia giao dịch, đối tượng chính của sàng lọc, được tổng hợp "
  "ở Bảng {b_mt103}. Đặc điểm quan trọng là phần lớn các trường này ở dạng văn bản tự do có giới hạn số dòng và số ký tự, ngoại trừ các tùy chọn dùng mã BIC.")
cap("Bảng {b_mt103}. Các trường chính của điện MT103 và MT202 liên quan đến sàng lọc")
tbl(["Trường", "Tên trường", "Định dạng", "Nội dung sàng lọc"], [
    ["50a (MT103)", "Người chuyển tiền (Ordering Customer)", "Tùy chọn A (BIC), F, K (tối đa 4 dòng x 35 ký tự)", "Tên, địa chỉ, quốc gia người chuyển"],
    ["52a", "Ngân hàng của người chuyển", "BIC hoặc tên, địa chỉ", "Mã BIC, tên ngân hàng, quốc gia"],
    ["56a", "Ngân hàng trung gian", "BIC hoặc tên, địa chỉ", "Mã BIC, tên ngân hàng, quốc gia"],
    ["57a", "Ngân hàng của người hưởng", "BIC hoặc tên, địa chỉ", "Mã BIC, tên ngân hàng, quốc gia"],
    ["58a (MT202)", "Định chế hưởng", "BIC hoặc tên, địa chỉ", "Mã BIC, tên định chế"],
    ["59a (MT103)", "Người hưởng (Beneficiary Customer)", "Không tùy chọn, A (BIC), F (tối đa 4 dòng x 35 ký tự)", "Tên, địa chỉ, quốc gia người hưởng"],
    ["70", "Thông tin chuyển tiền", "Tối đa 4 dòng x 35 ký tự", "Tên, địa danh, tên tàu, cảng xuất hiện trong nội dung"],
    ["72", "Thông tin giữa ngân hàng gửi và nhận", "Tối đa 6 dòng x 35 ký tự", "Tên, địa danh, hướng dẫn xử lý"],
], [1300, 2600, 2700, 2400])
p("Điện pacs.008 và pacs.009 theo chuẩn ISO 20022 [40] mô tả cùng các bên trên nhưng dưới dạng phần tử XML có cấu trúc (Bảng {b_pacs}). Tên (Nm) được tách khỏi "
  "địa chỉ bưu chính (PstlAdr), và địa chỉ có thể được chia nhỏ thành tên đường, số nhà, mã bưu chính, thành phố và mã quốc gia. Đây là điều kiện thuận lợi để "
  "sàng lọc theo từng thuộc tính; tuy nhiên, chuẩn vẫn cho phép dùng dòng địa chỉ tự do (AdrLine), và chất lượng điền dữ liệu phụ thuộc vào ngân hàng gửi điện.")
cap("Bảng {b_pacs}. Một số phần tử của điện pacs.008 liên quan đến sàng lọc")
tbl(["Phần tử", "Ý nghĩa", "Ghi chú"], [
    ["Dbtr / Nm", "Tên người chuyển", "Tách riêng khỏi địa chỉ"],
    ["Dbtr / PstlAdr", "Địa chỉ người chuyển", "Gồm StrtNm, BldgNb, PstCd, TwnNm, Ctry hoặc AdrLine"],
    ["Cdtr / Nm, PstlAdr", "Tên, địa chỉ người hưởng", "Tương tự Dbtr"],
    ["DbtrAgt, CdtrAgt / BICFI", "Ngân hàng người chuyển, người hưởng", "Mã BIC có cấu trúc"],
    ["IntrmyAgt1", "Ngân hàng trung gian", "Mã BIC hoặc tên, địa chỉ"],
    ["UltmtDbtr, UltmtCdtr", "Người chuyển, người hưởng cuối cùng", "Bên thứ ba, cần sàng lọc"],
    ["RmtInf / Ustrd", "Thông tin chuyển tiền dạng tự do", "Tương tự trường 70 của MT103"],
], [2600, 3000, 3400])
h3("2.1.7. Danh sách cấm vận và đặc điểm dữ liệu danh sách")
p("Danh sách cấm vận là dữ liệu tham chiếu của hệ thống sàng lọc. Danh sách hợp nhất của Hội đồng Bảo an Liên Hợp Quốc gồm các cá nhân, tổ chức thuộc các chế độ trừng phạt "
  "do Hội đồng Bảo an thiết lập. Danh sách SDN của OFAC là danh sách có ảnh hưởng lớn nhất đối với thanh toán bằng đồng đô la Mỹ; theo quy tắc 50% của OFAC [38], "
  "một tổ chức do một hoặc nhiều đối tượng bị chặn sở hữu từ 50% trở lên, trực tiếp hoặc gián tiếp, cũng bị coi là đối tượng bị chặn dù không có tên trong danh sách. "
  "Liên minh châu Âu và Vương quốc Anh duy trì danh sách riêng với phạm vi và thời điểm cập nhật khác nhau.")
p("Về mặt dữ liệu, mỗi mục trong danh sách thường gồm tên chính, nhiều bí danh, loại thực thể, ngày sinh hoặc năm sinh, quốc tịch, địa chỉ và chương trình trừng phạt. "
  "Các bí danh có chất lượng không đồng đều; OFAC phân biệt bí danh mạnh và bí danh yếu (thường là tên ngắn, phổ biến), và khuyến nghị cách xử lý khác nhau đối với "
  "hai loại này. Tên của các đối tượng có nguồn gốc Ả Rập, Trung Quốc, Nga, Triều Tiên được chuyển tự sang chữ Latinh theo nhiều hệ thống khác nhau, nên một người có thể "
  "có hàng chục cách viết. Các danh sách được cập nhật thường xuyên, có khi nhiều lần trong một tuần, đòi hỏi hệ thống sàng lọc phải tái lập chỉ mục và phân cụm nhanh chóng.")
h3("2.1.8. Chất lượng dữ liệu và nền tảng Oracle Enterprise Data Quality")
p("Chất lượng dữ liệu được hiểu là mức độ phù hợp của dữ liệu với mục đích sử dụng. Wang và Strong [34] xác định bốn nhóm chiều chất lượng dữ liệu từ góc nhìn người dùng: "
  "chất lượng nội tại, chất lượng theo ngữ cảnh, chất lượng biểu diễn và khả năng truy cập. Khung tri thức quản lý dữ liệu DAMA-DMBOK [35] sử dụng các chiều phổ biến như "
  "tính đầy đủ, tính duy nhất, tính kịp thời, tính hợp lệ, tính chính xác và tính nhất quán. Trong sàng lọc cấm vận, tính nhất quán về biểu diễn (mã hóa ký tự, kiểu đặt dấu, "
  "viết tắt) và tính hợp lệ về cấu trúc (tên nằm đúng trường) ảnh hưởng trực tiếp đến kết quả so khớp; vì vậy cải thiện chất lượng dữ liệu là điều kiện tiên quyết, "
  "không phải bước phụ trợ.")
p("Oracle Enterprise Data Quality (OEDQ) là nền tảng chất lượng dữ liệu cho phép xây dựng các quy trình xử lý dữ liệu từ các bộ xử lý (processor) được kết nối thành luồng, "
  "thiết kế trên công cụ Director và thực thi trên máy chủ theo lô hoặc theo thời gian thực qua dịch vụ web. Các nhóm chức năng của OEDQ được đề tài khai thác "
  "được tổng hợp ở Bảng {b_oedq}. Ưu điểm của nền tảng là các quy tắc được cấu hình một cách tường minh, có thể kiểm tra và giải thích, phù hợp với yêu cầu giải trình "
  "trong lĩnh vực tuân thủ.")
cap("Bảng {b_oedq}. Các nhóm chức năng của OEDQ được khai thác trong đề tài")
tbl(["Nhóm chức năng", "Ví dụ bộ xử lý, khả năng", "Vai trò trong mô hình đa tầng"], [
    ["Dữ liệu tham chiếu", "Bảng tra cứu, danh sách từ, bảng ánh xạ ký tự", "Tầng 1 đến tầng 3: bảng mã, từ nhiễu, họ tương đương, tên đường"],
    ["Biến đổi chuỗi", "Chuyển chữ hoa, chuẩn hóa khoảng trắng, thay thế ký tự", "Tầng 1: chuẩn hóa mã hóa và ký tự"],
    ["Phân tích cấu trúc", "Phân tách cú pháp theo mẫu, phân loại từ theo danh sách và biểu thức chính quy", "Tầng 2: tách tên khỏi địa chỉ, nhận diện thực thể"],
    ["Hồ sơ dữ liệu", "Phân tích mẫu, phân tích cụm từ, thống kê tần suất", "Nội dung 1: phân tích đặc trưng dữ liệu"],
    ["Mã hóa ngữ âm", "Soundex, Metaphone, khóa tùy chỉnh", "Tầng 4: khóa phân cụm"],
    ["So khớp nâng cao", "Khóa cụm, nhiều phép so sánh, luật khớp có ưu tiên", "Tầng 4, tầng 5: phân cụm và so khớp"],
    ["Thực thi", "Chạy theo lô, dịch vụ web thời gian thực", "Sàng lọc điện thanh toán thời gian thực"],
], [2300, 3600, 3100])

'''
insert_before('h2("2.2. Tình hình nghiên cứu trong nước")', B)

# --------------------------------------------------------------- Section 4: DSR methodology + renumber
for old, new in [('h2("4.8. Các hoạt động', 'h2("4.10. Các hoạt động'), ('h2("4.7. Sự cần thiết', 'h2("4.9. Sự cần thiết'),
                 ('h2("4.6. Công cụ', 'h2("4.8. Công cụ'), ('h2("4.5. Phương pháp đánh giá")', 'h2("4.6. Phương pháp đánh giá")'),
                 ('h2("4.4. Nội dung nghiên cứu")', 'h2("4.5. Nội dung nghiên cứu")'),
                 ('h2("4.3. Khung giải pháp đề xuất: mô hình sàng lọc đa tầng")', 'h2("4.4. Khung giải pháp đề xuất: mô hình sàng lọc đa tầng")'),
                 ('h3("4.2.4. ', 'h3("4.3.4. '), ('h3("4.2.3. ', 'h3("4.3.3. '), ('h3("4.2.2. ', 'h3("4.3.2. '), ('h3("4.2.1. ', 'h3("4.3.1. '),
                 ('h2("4.2. Dữ liệu nghiên cứu")', 'h2("4.3. Dữ liệu nghiên cứu")')]:
    rep(old, new)
rep('như mục 4.2.3.")', 'như mục 4.3.3.")')
rep('sàng lọc đa tầng được đề xuất ở mục 4.3.")', 'sàng lọc đa tầng được đề xuất ở mục 4.4.")')
rep('đo thay đổi của các chỉ số tại mục 4.5.")', 'đo thay đổi của các chỉ số tại mục 4.6.")')

C = '''h2("4.2. Phương pháp luận nghiên cứu")
p("Đề tài được thực hiện theo phương pháp luận khoa học thiết kế (Design Science Research) trong nghiên cứu hệ thống thông tin. Theo Hevner và cộng sự [32], "
  "nghiên cứu khoa học thiết kế tạo ra và đánh giá các sản phẩm nhân tạo (artifact) như mô hình, phương pháp, hiện thực nhằm giải quyết các vấn đề tổ chức được xác định; "
  "đóng góp của nghiên cứu được đánh giá qua tính hữu dụng của sản phẩm và tính chặt chẽ của quá trình thiết kế, đánh giá. Peffers và cộng sự [33] đề xuất quy trình gồm sáu "
  "hoạt động. Bảng {b_dsr} trình bày cách đề tài áp dụng quy trình này; Hình {h_dsr} minh họa các vòng lặp giữa thiết kế và đánh giá.")
cap("Bảng {b_dsr}. Áp dụng quy trình khoa học thiết kế trong đề tài")
tbl(["Hoạt động", "Nội dung trong đề tài", "Mục, nội dung liên quan"], [
    ["1. Xác định vấn đề và động lực", "Cảnh báo sai cao, đặc thù tên và địa chỉ người Việt, thiếu cơ sở định lượng khi hiệu chỉnh", "Mục 2.3, 2.4; nội dung 1"],
    ["2. Xác định mục tiêu của giải pháp", "Giảm ít nhất 30% cảnh báo sai, Recall từ 99% trở lên, giải thích được", "Mục 3"],
    ["3. Thiết kế và phát triển", "Mô hình sàng lọc đa tầng, khóa ngữ âm tiếng Việt, bảng tham chiếu", "Mục 4.4; nội dung 3, 4"],
    ["4. Trình diễn", "Hiện thực trên OEDQ, chạy với bộ dữ liệu kiểm thử", "Nội dung 2, 3, 4"],
    ["5. Đánh giá", "Đo chỉ số theo từng tầng, kiểm định thống kê, lấy ý kiến chuyên gia", "Mục 4.6, 4.7; nội dung 5"],
    ["6. Truyền đạt", "Bài báo, luận văn, buổi chia sẻ kết quả tại ngân hàng", "Mục 7"],
], [2700, 3900, 2400])
img("h9_dsr.png", "Hình {h_dsr}. Quy trình nghiên cứu khoa học thiết kế áp dụng trong đề tài", 15)
p("Bên cạnh đó, đề tài sử dụng kết hợp các phương pháp: nghiên cứu tài liệu để xây dựng cơ sở lý thuyết; phỏng vấn bán cấu trúc chuyên gia để xác định hiện trạng "
  "và nguyên nhân cảnh báo sai; phân tích dữ liệu định lượng trên mẫu 10 triệu bản ghi; thực nghiệm có kiểm soát để so sánh các cấu hình; và kiểm định thống kê để "
  "khẳng định ý nghĩa của các khác biệt.")

'''
insert_before('h2("4.3. Dữ liệu nghiên cứu")', C)

D = '''h2("4.7. Thiết kế thực nghiệm")
h3("4.7.1. Biến nghiên cứu")
p("Thực nghiệm được thiết kế theo dạng so sánh có kiểm soát trên cùng một bộ dữ liệu kiểm thử. Biến độc lập là cấu hình của mô hình sàng lọc, được thay đổi theo từng tầng "
  "và từng tham số (bảng tham chiếu, khóa cụm, luật khớp, ngưỡng). Biến phụ thuộc là các chỉ số hiệu quả ở mục 4.6. Các yếu tố được giữ cố định gồm phiên bản danh sách "
  "cấm vận, bộ dữ liệu kiểm thử và môi trường phần cứng, để mọi khác biệt đo được chỉ do thay đổi cấu hình gây ra.")
h3("4.7.2. Các kịch bản thực nghiệm")
p("Các kịch bản được xây dựng theo nguyên tắc cộng dồn: mỗi kịch bản bổ sung một tầng vào kịch bản trước, qua đó xác định đóng góp riêng của từng tầng (Bảng {b_kichban}). "
  "Ngoài ra, với mỗi tầng, các biến thể tham số được thử nghiệm riêng, ví dụ các mức gộp khác nhau của khóa ngữ âm hoặc các tổ hợp khóa cụm khác nhau.")
cap("Bảng {b_kichban}. Các kịch bản thực nghiệm cộng dồn")
tbl(["Kịch bản", "Cấu hình", "Câu hỏi được trả lời"], [
    ["KB0", "Cấu hình hiện hành (nền)", "Mốc so sánh"],
    ["KB1", "KB0 cộng tầng 1: chuẩn hóa mã hóa, ký tự, giữ hai biểu diễn", "CH2"],
    ["KB2", "KB1 cộng tầng 2: phân tích cấu trúc, tách tên khỏi địa chỉ", "CH1"],
    ["KB3", "KB2 cộng tầng 3: chuẩn hóa ngữ nghĩa, bảng tham chiếu", "CH2, CH4"],
    ["KB4", "KB3 cộng tầng 4: phân cụm đa khóa, khóa ngữ âm tiếng Việt", "CH3, CH6"],
    ["KB5", "KB4 cộng tầng 5: luật khớp ưu tiên, trọng số theo tần suất", "CH4"],
    ["KB6", "KB5 cộng tầng 6: thuộc tính phụ, ngưỡng theo rủi ro", "CH4, CH5"],
], [1400, 5200, 2400])
h3("4.7.3. Cỡ mẫu kiểm thử")
p("Số mẫu dương cần thiết được xác định để ước lượng Recall với độ chính xác mong muốn. Với Recall kỳ vọng p = 0,99, sai số cho phép e = 0,005 và độ tin cậy 95% (z = 1,96), "
  "cỡ mẫu tối thiểu được tính theo công thức ước lượng tỷ lệ:")
eq("n = z² × p × (1 - p) / e² = 1,96² × 0,99 × 0,01 / 0,005² ≈ 1.522")
p("Như vậy, mỗi nhóm cần đánh giá riêng (theo nhóm tên hoặc loại thực thể) cần ít nhất khoảng 1.522 mẫu dương. Với 5 nhóm tên và 2 loại thực thể, bộ dữ liệu kiểm thử cần "
  "tối thiểu khoảng 15.000 mẫu dương; đề tài dự kiến sinh khoảng 50.000 mẫu dương để có dự phòng cho các phân tích chi tiết theo dạng biến thể. Số mẫu âm là toàn bộ "
  "mẫu khách hàng, đủ lớn để ước lượng tỷ lệ cảnh báo sai với sai số rất nhỏ.")
h3("4.7.4. Các yếu tố ảnh hưởng đến tính hợp lệ của kết quả")
p("Theo cách phân loại phổ biến trong nghiên cứu thực nghiệm [42], đề tài nhận diện các yếu tố có thể ảnh hưởng đến tính hợp lệ của kết quả và biện pháp hạn chế tương ứng (Bảng {b_hople}).")
cap("Bảng {b_hople}. Các yếu tố ảnh hưởng đến tính hợp lệ và biện pháp hạn chế")
tbl(["Loại", "Yếu tố", "Biện pháp"], [
    ["Hợp lệ nội tại", "Mẫu âm có thể chứa trùng khớp thật chưa được phát hiện, làm sai lệch số cảnh báo sai", "Rà soát các cặp điểm cao với chuyên viên; báo cáo số cặp được điều chỉnh"],
    ["Hợp lệ nội tại", "Mẫu dương sinh tự động có thể không phản ánh đúng biến thể thực tế", "Phân loại biến thể theo hướng dẫn Wolfsberg; đối chiếu với mẫu cảnh báo đã xử lý"],
    ["Hợp lệ cấu trúc", "Chỉ số Precision, Recall trên dữ liệu kiểm thử khác với hiệu quả vận hành", "Bổ sung chỉ số vận hành: số cảnh báo trên 1.000 giao dịch, độ trễ"],
    ["Hợp lệ ngoại tại", "Kết quả tại một ngân hàng có thể khác ở ngân hàng khác", "Mô tả đặc trưng dữ liệu; đặc thù tên, địa chỉ người Việt mang tính phổ quát"],
    ["Hợp lệ kết luận", "Khác biệt nhỏ giữa cấu hình có thể do ngẫu nhiên", "Kiểm định McNemar, khoảng tin cậy bootstrap"],
], [1700, 3900, 3400])

'''
insert_before('h2("4.8. Công cụ', D)

E = '''h1("KẾT LUẬN")
p("Sàng lọc cấm vận giao dịch thanh toán quốc tế là một khâu kiểm soát quan trọng trong hệ thống phòng, chống rửa tiền, tài trợ khủng bố và phổ biến vũ khí hủy diệt hàng loạt "
  "của ngân hàng. Đề tài đã chỉ ra rằng, với dữ liệu khách hàng Việt Nam, bài toán này không thể được giải quyết hiệu quả bằng cách so sánh chuỗi đơn giản, mà cần được tiếp cận như "
  "một bài toán phân giải thực thể trên dữ liệu kém chất lượng, chịu các ràng buộc về thời gian thực, quy mô và yêu cầu giải trình.")
p("Trên cơ sở phân tích năm nhóm đặc thù của tên và địa chỉ người Việt, gồm tên đường mang tên danh nhân, hiện tượng trùng tên khi bỏ dấu, phân bố họ lệch, các biến thể chính tả "
  "và mã hóa ký tự, địa chỉ đa định dạng sau đợt sắp xếp đơn vị hành chính năm 2025, đề tài đề xuất mô hình sàng lọc đa tầng gồm sáu tầng được hiện thực trên nền tảng OEDQ, "
  "cùng khóa ngữ âm tiếng Việt, bộ bảng tham chiếu và phương pháp đánh giá tách biệt từng tầng theo cách tiếp cận khoa học thiết kế.")
p("Khi hoàn thành, đề tài kỳ vọng cung cấp bằng chứng định lượng về hiệu quả của từng kỹ thuật, một mô hình có thể áp dụng tại Ngân hàng TMCP Quân đội và các ngân hàng thương mại "
  "khác, đồng thời góp phần vào nỗ lực chung của hệ thống ngân hàng Việt Nam trong việc nâng cao hiệu quả thực thi các biện pháp trừng phạt tài chính có mục tiêu. Hướng phát triển "
  "tiếp theo có thể là mở rộng mô hình cho sàng lọc khách hàng định kỳ, sàng lọc tên tàu, cảng trong tài trợ thương mại, và nghiên cứu kết hợp các mô hình học máy có khả năng "
  "giải thích ở tầng chấm điểm.")

'''
rep('# ---------------------------------------------------------------- TLTK', E + '# ---------------------------------------------------------------- TLTK')

rep('''"Quốc hội (2025). Luật Tổ chức chính quyền địa phương số 72/2025/QH15 ngày 16/6/2025.",
]''', '''"Quốc hội (2025). Luật Tổ chức chính quyền địa phương số 72/2025/QH15 ngày 16/6/2025.",
 "Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.",
 "Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77.",
 "Wang, R. Y., & Strong, D. M. (1996). Beyond accuracy: What data quality means to data consumers. Journal of Management Information Systems, 12(4), 5-33.",
 "DAMA International (2017). DAMA-DMBOK: Data Management Body of Knowledge (2nd ed.). Technics Publications.",
 "Levenshtein, V. I. (1966). Binary codes capable of correcting deletions, insertions, and reversals. Soviet Physics Doklady, 10(8), 707-710.",
 "Jaro, M. A. (1989). Advances in record-linkage methodology as applied to matching the 1985 Census of Tampa, Florida. Journal of the American Statistical Association, 84(406), 414-420.",
 "U.S. Department of the Treasury, OFAC (2014). Revised Guidance on Entities Owned by Persons Whose Property and Interests in Property Are Blocked.",
 "SWIFT. Standards MT: Category 1 Customer Payments and Cheques; Category 2 Financial Institution Transfers. Message Reference Guide.",
 "ISO 20022. FIToFICustomerCreditTransferV08 (pacs.008.001.08), Message Definition Report.",
 "Russell, R. C. (1918). Index. U.S. Patent 1,261,167.",
 "Wohlin, C., Runeson, P., Höst, M., Ohlsson, M. C., Regnell, B., & Wesslén, A. (2012). Experimentation in Software Engineering. Springer.",
]''')
rep('"Nghiên cứu tài liệu [1] đến [31]', '"Nghiên cứu tài liệu [1] đến [42]')

# Abbreviations list for front matter
s += '''
ABBR = [
 ("AML", "Anti-Money Laundering: phòng, chống rửa tiền"),
 ("BIC", "Business Identifier Code: mã định danh ngân hàng trong mạng SWIFT"),
 ("BPMN", "Business Process Model and Notation: ký pháp mô hình hóa quy trình"),
 ("CBPR+", "Cross-border Payments and Reporting Plus: chuẩn điện ISO 20022 cho thanh toán xuyên biên giới"),
 ("DSR", "Design Science Research: nghiên cứu khoa học thiết kế"),
 ("EU", "European Union: Liên minh châu Âu"),
 ("FATF", "Financial Action Task Force: Lực lượng đặc nhiệm tài chính"),
 ("FN", "False Negative: bỏ sót"),
 ("FP", "False Positive: cảnh báo sai"),
 ("IBAN", "International Bank Account Number: số tài khoản ngân hàng quốc tế"),
 ("ISO 20022", "Chuẩn quốc tế về thông điệp tài chính"),
 ("MB", "Ngân hàng Thương mại Cổ phần Quân đội"),
 ("MT", "Message Type: điện SWIFT định dạng truyền thống"),
 ("MX", "Điện SWIFT theo chuẩn ISO 20022"),
 ("NHNN", "Ngân hàng Nhà nước Việt Nam"),
 ("NYDFS", "New York State Department of Financial Services: Sở Dịch vụ Tài chính New York"),
 ("OEDQ", "Oracle Enterprise Data Quality: nền tảng chất lượng dữ liệu của Oracle"),
 ("OFAC", "Office of Foreign Assets Control: Văn phòng Kiểm soát Tài sản nước ngoài, Bộ Tài chính Hoa Kỳ"),
 ("SDN", "Specially Designated Nationals and Blocked Persons List: danh sách đối tượng bị chỉ định đặc biệt của OFAC"),
 ("SWIFT", "Society for Worldwide Interbank Financial Telecommunication: Hiệp hội Viễn thông Tài chính Liên ngân hàng Toàn cầu"),
 ("TCVN", "Tiêu chuẩn Việt Nam"),
 ("TP, TN", "True Positive, True Negative: phát hiện đúng, bỏ qua đúng"),
 ("UN", "United Nations: Liên Hợp Quốc"),
]
'''
open(p, 'w', encoding='utf8').write(s)
print('ok')
