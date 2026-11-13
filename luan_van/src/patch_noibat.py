import re
p = 'full_content.py'
s = open(p, encoding='utf8').read()

def rep(old, new, cnt=1):
    global s
    assert s.count(old) == cnt, (s.count(old), old[:80])
    s = s.replace(old, new)

def insert_before(anchor, text):
    global s
    assert s.count(anchor) == 1, anchor
    s = s.replace(anchor, text + anchor)

# ------------------------------------------------------------------ 1. TÓM TẮT
i = s.index('h1("1. TÓM TẮT")'); j = s.index("B.append(('kw'")
s = s[:i] + '''h1("1. TÓM TẮT")
p("Sàng lọc cấm vận là khâu kiểm soát bắt buộc đối với ngân hàng tham gia thanh toán quốc tế: mọi bên trong điện thanh toán phải được "
  "đối chiếu với danh sách cấm vận của Liên Hợp Quốc, OFAC, Liên minh châu Âu, Vương quốc Anh và Việt Nam trước khi giao dịch được xử lý. "
  "Thoạt nhìn, đây chỉ là việc so sánh tên khách hàng với tên trong danh sách. Thực tế, với dữ liệu khách hàng Việt Nam, đó là một bài toán "
  "phân giải thực thể trên dữ liệu kém chất lượng: tên và địa chỉ bị ghép chung trong trường văn bản tự do, tên đường mang tên danh nhân, "
  "dấu tiếng Việt bị lược bỏ khiến nhiều tên khác nhau trùng thành một, cùng một tên tồn tại ở nhiều dạng mã hóa và chính tả, họ người Việt "
  "phân bố rất lệch, địa chỉ thay đổi theo đợt sắp xếp đơn vị hành chính năm 2025. Cách làm đơn giản như bỏ dấu rồi so sánh vừa sinh nhiều "
  "cảnh báo sai, vừa có thể bỏ sót đối tượng.")
p("Đề tài đề xuất mô hình sàng lọc đa tầng thích ứng với dữ liệu tiếng Việt, gồm sáu tầng: chuẩn hóa mã hóa và ký tự; phân tích cấu trúc "
  "trường tự do bằng mẫu để tách tên khỏi địa chỉ; chuẩn hóa ngữ nghĩa dựa trên bảng tham chiếu; phân cụm đa khóa kết hợp khóa ngữ âm tiếng Việt; "
  "so khớp nâng cao nhiều phép so sánh với luật ưu tiên và băng điểm; chấm điểm kết hợp thuộc tính phụ và danh sách loại trừ có kiểm soát. "
  "Mô hình được hiện thực trên nền tảng Oracle Enterprise Data Quality và đánh giá trên 10 triệu cặp tên, địa chỉ khách hàng đã khử định danh "
  "tại Ngân hàng TMCP Quân đội, với mục tiêu giảm ít nhất 30% cảnh báo sai trong khi duy trì Recall không thấp hơn 99%.")
''' + s[j:]

# ------------------------------------------------------------------ 2.3 intro
rep('p("Qua thực tế vận hành hệ thống sàng lọc tại ngân hàng, học viên nhận thấy tên và địa chỉ của khách hàng Việt Nam có ba đặc điểm khiến các quy tắc "\n  "so khớp thiết kế cho tên phương Tây hoạt động kém hiệu quả. Đây là điểm xuất phát và cũng là đóng góp chính của đề tài.")',
    'p("Qua thực tế vận hành hệ thống sàng lọc tại ngân hàng, học viên nhận thấy tên và địa chỉ của khách hàng Việt Nam có năm nhóm đặc điểm khiến các quy tắc "\n  "so khớp thiết kế cho tên phương Tây hoạt động kém hiệu quả. Đây là điểm xuất phát và cũng là đóng góp chính của đề tài.")')

# ------------------------------------------------------------------ new 2.3.4, 2.3.5, 2.4 ; rename old 2.4 -> 2.5
NEW_23 = '''h3("2.3.4. Biến thể chính tả, vùng miền và mã hóa ký tự")
p("Cùng một họ tên có thể tồn tại dưới nhiều dạng chuỗi ký tự khác nhau, kể cả khi còn giữ dấu. Thứ nhất, một số họ có biến thể theo vùng miền "
  "do tục kiêng húy thời các chúa Nguyễn, điển hình là Hoàng và Huỳnh, Vũ và Võ; đây là cùng một họ nhưng khác hoàn toàn về ký tự. Thứ hai, tiếng Việt "
  "tồn tại song song hai kiểu đặt dấu thanh (Hòa và Hoà, Thủy và Thuỷ) và hai cách viết i, y (Lý và Lí, Mỹ và Mĩ). Thứ ba, chữ Việt có dấu có thể được "
  "biểu diễn trong Unicode ở dạng dựng sẵn hoặc dạng tổ hợp [28], hai chuỗi trông giống hệt nhau nhưng khác nhau về mã. Thứ tư, dữ liệu khách hàng "
  "nhập từ trước khi các cơ quan thống nhất dùng bộ mã TCVN 6909:2001 theo Quyết định 72/2002/QĐ-TTg [29] có thể còn lưu bằng các bảng mã cũ như "
  "TCVN3 (ABC) hay VNI; khi chuyển đổi không đúng, tên bị biến thành chuỗi ký tự lạ. Nếu chỉ bỏ dấu một cách đơn giản trên các chuỗi này, kết quả "
  "có thể sai lệch hoàn toàn so với tên thật, dẫn đến bỏ sót.")
cap("Bảng {b_bienthe}. Các dạng biến thể của cùng một tên trong dữ liệu khách hàng")
tbl(["Loại biến thể", "Ví dụ", "Hệ quả nếu so khớp ký tự đơn thuần"], [
    ["Biến thể họ theo vùng miền", "Hoàng và Huỳnh; Vũ và Võ", "Bỏ sót: hai dạng không giống nhau về ký tự"],
    ["Kiểu đặt dấu thanh", "Hòa và Hoà; Thủy và Thuỷ", "Không khớp khi so sánh tên có dấu"],
    ["Cách viết i, y", "Lý và Lí; Mỹ và Mĩ", "Không khớp, kể cả sau khi bỏ dấu"],
    ["Dạng Unicode dựng sẵn và tổ hợp", "Nguyễn (1 ký tự ễ) và Nguyễn (e + dấu mũ + dấu ngã)", "Khác mã, bỏ dấu thủ công có thể để sót ký tự dấu"],
    ["Bảng mã cũ chuyển đổi lỗi", "Tên lưu bằng TCVN3, VNI hiển thị thành chuỗi ký tự lạ", "Sai lệch hoàn toàn, có thể bỏ sót"],
    ["Phiên âm, gõ sai khi nhập", "NGUYEN, NGYUEN, NGUEN", "Cần so khớp mờ có kiểm soát"],
], [2600, 3400, 3000])
h3("2.3.5. Địa chỉ đa định dạng và thay đổi địa giới hành chính")
p("Địa chỉ của khách hàng Việt Nam được ghi theo nhiều quy ước khác nhau: số nhà kèm ngõ, ngách, hẻm; các đơn vị hành chính viết đầy đủ hoặc viết tắt "
  "(Phường, P., F; Quận, Q.; Thành phố, TP.); có hoặc không có dấu. Đặc biệt, theo Nghị quyết 202/2025/QH15 [30], số đơn vị hành chính cấp tỉnh giảm từ "
  "63 xuống 34; theo Luật Tổ chức chính quyền địa phương số 72/2025/QH15 [31], từ ngày 01/7/2025 chính quyền địa phương được tổ chức theo hai cấp "
  "(tỉnh và xã), các đơn vị cấp huyện kết thúc hoạt động. Hệ quả là cùng một nơi cư trú có thể được ghi theo địa giới cũ (có quận, huyện và tên tỉnh cũ) "
  "hoặc địa giới mới, trong khi dữ liệu khách hàng tích lũy qua nhiều năm chứa cả hai dạng. Điều này làm khó việc nhận diện phần địa chỉ trong trường "
  "văn bản tự do và việc dùng thông tin địa lý làm thuộc tính phụ khi so khớp.")

h2("2.4. Vì sao đây không phải là bài toán so sánh chuỗi đơn giản")
p("Một cách tiếp cận trực giác là bỏ dấu tên khách hàng rồi so sánh với danh sách bằng một độ đo khoảng cách chuỗi. Phân tích ở mục 2.3 cho thấy cách làm "
  "này thất bại theo cả hai chiều: nó làm tăng cảnh báo sai (nhiều tên khác nhau trùng thành một, tên đường bị coi là tên người, họ phổ biến khớp với mọi "
  "đối tượng cùng họ) và đồng thời có thể gây bỏ sót (họ biến thể vùng miền, lỗi mã hóa, đảo thứ tự tên, tên bị ngắt dòng). Bên cạnh đặc thù dữ liệu, "
  "bài toán còn chịu các ràng buộc vận hành chặt chẽ được tổng hợp ở Bảng {b_thachthuc}.")
cap("Bảng {b_thachthuc}. Các thách thức của bài toán sàng lọc cấm vận với dữ liệu khách hàng Việt Nam")
tbl(["Nhóm thách thức", "Biểu hiện", "Yêu cầu đối với giải pháp"], [
    ["Chất lượng dữ liệu nguồn", "Lỗi mã hóa, nhiều dạng Unicode, hai kiểu đặt dấu, viết tắt tùy ý", "Chuẩn hóa mã hóa và ký tự trước mọi bước so sánh"],
    ["Cấu trúc trường tự do", "Tên, địa chỉ, số tài khoản ghép chung trong 4 dòng x 35 ký tự", "Phân tích cấu trúc, nhận diện mẫu để tách tên khỏi địa chỉ"],
    ["Ngữ nghĩa tên Việt", "Bỏ dấu gây trùng; họ biến thể vùng miền; tên đệm Văn, Thị ít giá trị phân biệt", "Bảng tham chiếu tương đương, trọng số theo tần suất"],
    ["Đa văn hóa của danh sách", "Tên Ả Rập, Trung Quốc, Nga có nhiều cách chuyển tự sang chữ Latinh", "So khớp ngữ âm, bảng biến thể tên quốc tế"],
    ["Quy mô và phân bố", "10 triệu bản ghi; hàng chục nghìn tên và bí danh trong danh sách; họ Nguyễn chiếm hơn 30%", "Phân cụm đa khóa, kiểm soát kích thước cụm"],
    ["Thời gian thực", "Điện thanh toán phải chờ kết quả sàng lọc trước khi được chuyển đi", "Độ trễ thấp, xử lý ổn định khi danh sách cập nhật hằng ngày"],
    ["Chi phí bất đối xứng", "Bỏ sót một đối tượng có thể dẫn đến chế tài nặng; mỗi cảnh báo sai tốn công xử lý", "Recall gần tuyệt đối, tối ưu Precision trong ràng buộc đó"],
    ["Giải trình và kiểm toán", "Mỗi quyết định bỏ qua cảnh báo phải có căn cứ", "Quy tắc giải thích được, ghi nhận lý do khớp cho từng cảnh báo"],
], [2200, 3700, 3100])
p("Vì vậy, đề tài tiếp cận sàng lọc cấm vận như một bài toán phân giải thực thể (entity resolution) trên dữ liệu kém chất lượng và có ràng buộc vận hành, "
  "đòi hỏi kết hợp nhiều kỹ thuật chất lượng dữ liệu theo một chuỗi xử lý có thiết kế, thay vì một phép so sánh chuỗi đơn lẻ. Đây là cơ sở của mô hình "
  "sàng lọc đa tầng được đề xuất ở mục 4.3.")

'''
insert_before('h2("2.4. Khoảng trống nghiên cứu và sự cần thiết tiến hành nghiên cứu")', NEW_23)
rep('h2("2.4. Khoảng trống nghiên cứu và sự cần thiết tiến hành nghiên cứu")', 'h2("2.5. Khoảng trống nghiên cứu và sự cần thiết tiến hành nghiên cứu")')
rep('"(ii) thiếu đánh giá tách biệt tác động của từng bước làm sạch, chuẩn hóa, phân cụm và quy tắc so khớp; (iii) chưa có nghiên cứu về các đặc thù tên, "\n  "địa chỉ người Việt trong sàng lọc cấm vận.")',
    '"(ii) thiếu đánh giá tách biệt tác động của từng bước làm sạch, chuẩn hóa, phân cụm và quy tắc so khớp; (iii) chưa có nghiên cứu về các đặc thù tên, "\n  "địa chỉ người Việt trong sàng lọc cấm vận; (iv) các kỹ thuật ngữ âm phổ biến như Soundex, Metaphone [27] được thiết kế cho tiếng Anh, chưa có khóa ngữ âm "\n  "phù hợp với chữ Quốc ngữ không dấu.")')
# contributions after the "Về tính mới" paragraph
insert_before('# ---------------------------------------------------------------- 3. MỤC TIÊU', '''p("Các đóng góp dự kiến của đề tài gồm:")
b("Hệ thống hóa và đo lường định lượng các đặc thù của tên, địa chỉ người Việt gây cảnh báo sai và bỏ sót trong sàng lọc cấm vận.")
b("Đề xuất mô hình sàng lọc đa tầng thích ứng với dữ liệu tiếng Việt, hiện thực trên nền tảng chất lượng dữ liệu OEDQ.")
b("Đề xuất khóa ngữ âm tiếng Việt cho phân cụm và so khớp, cùng bộ bảng tham chiếu tiếng Việt (họ tương đương, tên đường, đơn vị hành chính cũ và mới, loại hình doanh nghiệp).")
b("Xây dựng bộ dữ liệu kiểm thử có gán nhãn và phương pháp đánh giá tách biệt từng tầng, có thể lặp lại.")
b("Đề xuất quy trình kiểm định, hiệu chỉnh định kỳ phù hợp quy định Việt Nam và thông lệ quốc tế.")

''')

# ------------------------------------------------------------------ 3. objectives & questions
rep('b("MT3: Đề xuất bộ quy tắc làm sạch, chuẩn hóa, phân cụm và so khớp giúp giảm ít nhất 30% cảnh báo sai so với cấu hình hiện hành trong khi duy trì Recall từ 99% trở lên trên bộ dữ liệu kiểm thử.")',
    'b("MT3: Thiết kế và hiện thực trên OEDQ mô hình sàng lọc đa tầng thích ứng với dữ liệu tiếng Việt, giúp giảm ít nhất 30% cảnh báo sai so với cấu hình hiện hành trong khi duy trì Recall từ 99% trở lên trên bộ dữ liệu kiểm thử.")')
rep('b("CH5: Dữ liệu có cấu trúc của điện ISO 20022 cải thiện hiệu quả sàng lọc như thế nào so với điện MT dạng văn bản tự do?")',
    'b("CH5: Dữ liệu có cấu trúc của điện ISO 20022 cải thiện hiệu quả sàng lọc như thế nào so với điện MT dạng văn bản tự do?")\nb("CH6: Khóa ngữ âm thích ứng tiếng Việt cải thiện tỷ lệ giữ lại cặp khớp đúng và Recall như thế nào so với Soundex, Metaphone?")')

# ------------------------------------------------------------------ 4.3 new framework section; renumber 4.3..4.7
for a, b_ in [('h2("4.7. Các hoạt động', 'h2("4.8. Các hoạt động'), ('h2("4.6. Sự cần thiết', 'h2("4.7. Sự cần thiết'),
              ('h2("4.5. Công cụ', 'h2("4.6. Công cụ'), ('h2("4.4. Phương pháp đánh giá")', 'h2("4.5. Phương pháp đánh giá")'),
              ('h2("4.3. Nội dung nghiên cứu")', 'h2("4.4. Nội dung nghiên cứu")')]:
    rep(a, b_)
rep('thực nghiệm loại bỏ từng thành phần (ablation study), mỗi lần bật hoặc tắt một quy tắc so với cấu hình nền và đo thay đổi của các chỉ số tại mục 4.4.")',
    'thực nghiệm loại bỏ từng thành phần (ablation study), mỗi lần bật hoặc tắt một quy tắc so với cấu hình nền và đo thay đổi của các chỉ số tại mục 4.5.")')

FRAME = '''h2("4.3. Khung giải pháp đề xuất: mô hình sàng lọc đa tầng")
p("Từ các thách thức ở mục 2.4, đề tài đề xuất mô hình sàng lọc đa tầng (Hình {h_mohinh}). Mỗi tầng giải quyết một nhóm vấn đề cụ thể và tạo đầu vào sạch hơn "
  "cho tầng sau; mỗi tầng có thể bật, tắt và đo lường riêng, giúp đánh giá đóng góp của từng tầng. Mô hình được hiện thực bằng các bộ xử lý sẵn có của "
  "nền tảng chất lượng dữ liệu OEDQ (bảng tra ký tự, bảng tham chiếu, phân tách cú pháp theo mẫu, khóa ngữ âm, so khớp nâng cao), kết hợp các bảng tham chiếu "
  "và quy tắc do đề tài xây dựng riêng cho tiếng Việt.")
img("h8_mohinh.png", "Hình {h_mohinh}. Mô hình sàng lọc đa tầng thích ứng với dữ liệu tiếng Việt", 16)
h3("Tầng 1: Chuẩn hóa mã hóa và ký tự")
p("Tầng đầu tiên đưa mọi chuỗi về cùng một biểu diễn trước khi so sánh: phát hiện và chuyển đổi dữ liệu còn lưu bằng bảng mã cũ (TCVN3, VNI) sang Unicode; "
  "chuẩn hóa về dạng dựng sẵn [28]; thống nhất kiểu đặt dấu thanh; chuyển chữ hoa, chuẩn hóa khoảng trắng và dấu câu. Điểm khác biệt so với cách làm thông thường "
  "là mỗi tên được giữ song song hai biểu diễn: dạng có dấu đã chuẩn hóa (dùng khi cả hai phía đều có dấu, ví dụ sàng lọc khách hàng nội bộ) và dạng không dấu "
  "(dùng khi đối chiếu với điện SWIFT và danh sách quốc tế). Nhờ vậy thông tin về dấu không bị mất đi mà vẫn khai thác được ở các tầng sau.")
h3("Tầng 2: Phân tích cấu trúc và nhận diện mẫu")
p("Tầng này giải quyết vấn đề tên, địa chỉ và các thông tin khác bị ghép chung trong trường văn bản tự do. Mỗi dòng được tách thành các từ; mỗi từ được phân loại "
  "dựa trên bảng tham chiếu (họ người Việt, tên đệm phổ biến, tên đường, đơn vị hành chính cũ và mới, loại hình doanh nghiệp, danh xưng, từ nhiễu) và dựa trên "
  "mẫu ký tự (số nhà, mã BIC 8 hoặc 11 ký tự, số tài khoản, IBAN). Chuỗi nhãn của các từ tạo thành mẫu cấu trúc của dòng; từ mẫu này, quy tắc phân loại xác định "
  "dòng là tên, địa chỉ hay thông tin khác, đồng thời nhận diện loại thực thể (cá nhân hoặc tổ chức). Với các trường tự do dài như thông tin chuyển tiền, kỹ thuật "
  "cửa sổ trượt n từ được dùng để phát hiện tên bị nhúng trong câu. Bảng {b_mau} minh họa cách phân tích một trường người hưởng.")
cap("Bảng {b_mau}. Minh họa phân tích mẫu cấu trúc trường 59 của điện MT103")
tbl(["Dòng", "Mẫu nhãn từ", "Kết quả phân loại"], [
    ["NGUYEN THI MAI", "[HỌ] [ĐỆM] [TÊN]", "Tên cá nhân: đưa vào so khớp tên"],
    ["25 LE VAN LUONG", "[SỐ] [HỌ] [ĐỆM] [TÊN ĐƯỜNG]", "Địa chỉ: chỉ dùng làm thuộc tính phụ, không so khớp như tên người"],
    ["P THANH XUAN TRUNG", "[ĐƠN VỊ HC] [ĐỊA DANH]", "Địa chỉ cấp xã"],
    ["HA NOI VIET NAM", "[TỈNH] [QUỐC GIA]", "Địa chỉ: suy ra mã quốc gia VN"],
], [2600, 3200, 3200])
h3("Tầng 3: Chuẩn hóa ngữ nghĩa dựa trên bảng tham chiếu")
p("Sau khi đã biết vai trò của từng từ, tầng này đưa các cách viết khác nhau của cùng một khái niệm về một dạng chuẩn: loại hình doanh nghiệp (CÔNG TY TNHH, "
  "CTY TNHH, CO., LTD, LIMITED cùng về LTD), danh xưng (ÔNG, BÀ, MR, MRS bị loại khỏi tên), họ tương đương theo vùng miền (HUYNH và HOANG, VO và VU), biến thể i, y, "
  "và các biến thể chuyển tự của tên quốc tế trong danh sách (MOHAMMED, MUHAMMAD; tiền tố AL, ABU, BIN). Mỗi tên được sinh ra nhiều dạng chuẩn: dạng đầy đủ, "
  "dạng đã loại từ nhiễu, dạng tập từ không phụ thuộc thứ tự và dạng ngữ âm, làm đầu vào cho phân cụm và so khớp.")
h3("Tầng 4: Phân cụm đa khóa và khóa ngữ âm tiếng Việt")
p("Để giải quyết phân bố họ lệch, đề tài thay khóa cụm đơn theo họ bằng nhiều khóa song song, mỗi bản ghi có thể thuộc nhiều cụm: khóa theo từng từ có giá trị "
  "phân biệt (loại các từ tần suất cao như NGUYEN, VAN, THI khỏi khóa), khóa theo phần đầu của tên gọi, khóa tập từ đã sắp xếp và khóa ngữ âm. Kích thước cụm được "
  "giới hạn và giám sát. Các thuật toán ngữ âm phổ biến như Soundex và Metaphone [27] được thiết kế cho cách phát âm tiếng Anh nên không phản ánh đúng chữ Quốc ngữ "
  "không dấu. Đề tài đề xuất khóa ngữ âm tiếng Việt dựa trên các quy tắc gộp những cách viết có cách đọc tương tự (Bảng {b_nguam}); mức độ gộp của từng quy tắc "
  "sẽ được đánh giá riêng vì gộp càng mạnh thì càng ít bỏ sót nhưng cụm càng lớn.")
cap("Bảng {b_nguam}. Một số quy tắc dự kiến của khóa ngữ âm tiếng Việt")
tbl(["Quy tắc", "Cơ sở", "Ví dụ"], [
    ["NGH thành NG; GH thành G", "Cùng âm, khác quy tắc chính tả", "NGHIA và NGIA cùng khóa"],
    ["PH thành F", "Cách viết khi phiên âm sang hệ thống nước ngoài", "PHUONG và FUONG cùng khóa"],
    ["K (trừ tổ hợp KH), Q thành C", "Cùng âm đầu, khác quy tắc chính tả", "KIM và CIM cùng khóa; QUANG và CUANG cùng khóa"],
    ["D, GI, R thành Z", "Phương ngữ Bắc phát âm như nhau", "GIANG và DANG cùng khóa"],
    ["TR thành CH; S thành X", "Phương ngữ không phân biệt", "TRUNG và CHUNG cùng khóa"],
    ["Y thành I", "Hai cách viết i, y", "THUY và THUI cùng khóa"],
], [2600, 3200, 3200])
h3("Tầng 5: So khớp nâng cao với luật ưu tiên và băng điểm")
p("Mỗi cặp ứng viên trong cùng cụm được so sánh bằng nhiều phép so sánh trên các dạng chuẩn ở tầng 3: khớp chính xác, khoảng cách chỉnh sửa ký tự, tỷ lệ từ khớp, "
  "khớp không phụ thuộc thứ tự, khớp chữ cái đầu cho tên viết tắt, khớp ngữ âm và khớp chứa (tên ngắn nằm trong tên dài). Kết quả các phép so sánh được kết hợp "
  "bằng hệ thống luật khớp có thứ tự ưu tiên, mỗi luật gắn với một băng điểm (Bảng {b_luat}). Từ có tần suất cao trong dữ liệu người Việt được gán trọng số thấp. "
  "Với mỗi cảnh báo, hệ thống ghi lại luật đã kích hoạt và các từ đã khớp, giúp chuyên viên xử lý nhanh và đáp ứng yêu cầu giải trình.")
cap("Bảng {b_luat}. Minh họa hệ thống luật khớp theo thứ tự ưu tiên")
tbl(["Ưu tiên", "Điều kiện khớp", "Băng điểm"], [
    ["1", "Khớp chính xác toàn bộ tên ở dạng chuẩn", "Rất cao"],
    ["2", "Khớp toàn bộ các từ, không phụ thuộc thứ tự", "Cao"],
    ["3", "Khớp toàn bộ từ, tối đa một từ lệch không quá 1 ký tự", "Cao"],
    ["4", "Khớp ngữ âm toàn bộ từ có giá trị phân biệt", "Trung bình"],
    ["5", "Khớp chữ cái đầu của tên đệm, các từ còn lại khớp chính xác", "Trung bình"],
    ["6", "Chỉ khớp các từ tần suất cao (họ, tên đệm phổ biến)", "Không cảnh báo"],
], [1200, 5600, 2200])
h3("Tầng 6: Chấm điểm kết hợp thuộc tính phụ và ra quyết định")
p("Điểm của tên được điều chỉnh theo các thuộc tính phụ: quốc gia suy ra từ địa chỉ, mã BIC hoặc mã quốc gia trong điện MX; năm sinh và quốc tịch khi có; "
  "sự phù hợp về loại thực thể (một cá nhân trong danh sách khớp với tên tổ chức sẽ bị giảm điểm); vị trí khớp (khớp nằm trong phần đã được nhận diện là địa chỉ "
  "bị giảm điểm đối với danh sách cá nhân). Ngưỡng ra quyết định được phân tầng theo rủi ro, chẳng hạn ngưỡng thấp hơn với các chương trình cấm vận toàn diện. "
  "Cuối cùng, danh sách loại trừ có kiểm soát ghi nhận các cặp khách hàng và mục danh sách đã được chuyên viên xác nhận không trùng để không cảnh báo lặp lại; "
  "mỗi mục loại trừ phải được phê duyệt hai cấp và tự động hết hiệu lực khi thông tin khách hàng hoặc mục danh sách thay đổi.")

'''
insert_before('h2("4.4. Nội dung nghiên cứu")', FRAME)
rep('h3("Nội dung 3: Tối ưu quy tắc làm sạch và chuẩn hóa")', 'h3("Nội dung 3: Hiện thực và tối ưu tầng 1 đến tầng 3")')
rep('h3("Nội dung 4: Tối ưu phân cụm, quy tắc so khớp và ngưỡng")', 'h3("Nội dung 4: Hiện thực và tối ưu tầng 4 đến tầng 6")')
rep('b("So sánh các khóa phân cụm: theo họ;', 'b("Xây dựng khóa ngữ âm tiếng Việt và so sánh với Soundex, Metaphone về tỷ lệ giữ lại cặp khớp đúng và kích thước cụm.")\nb("So sánh các khóa phân cụm: theo họ;')
rep('p("Để khẳng định sự khác biệt giữa hai cấu hình là có ý nghĩa thống kê,',
    'p("Việc đánh giá được thực hiện tách biệt theo từng tầng của mô hình: lần lượt thêm từng tầng vào cấu hình nền và đo mức thay đổi của các chỉ số, qua đó "\n  "xác định đóng góp riêng của mỗi tầng và mỗi đặc thù dữ liệu.")\np("Để khẳng định sự khác biệt giữa hai cấu hình là có ý nghĩa thống kê,')

# ------------------------------------------------------------------ 7.1
rep('b("Bộ quy tắc làm sạch, chuẩn hóa, phân cụm và so khớp phù hợp với đặc thù tên, địa chỉ người Việt, mục tiêu giảm ít nhất 30% cảnh báo sai với Recall từ 99% trở lên.")',
    'b("Mô hình sàng lọc đa tầng thích ứng với dữ liệu tiếng Việt được hiện thực trên OEDQ, mục tiêu giảm ít nhất 30% cảnh báo sai với Recall từ 99% trở lên.")\nb("Khóa ngữ âm tiếng Việt và bộ bảng tham chiếu tiếng Việt: họ tương đương, tên đường, đơn vị hành chính cũ và mới, loại hình doanh nghiệp, từ nhiễu.")')

# ------------------------------------------------------------------ references
rep(' "Chính phủ (2025). Nghị định 356/2025/NĐ-CP ngày 31/12/2025 quy định chi tiết một số điều và biện pháp thi hành Luật Bảo vệ dữ liệu cá nhân.",\n]',
    ''' "Chính phủ (2025). Nghị định 356/2025/NĐ-CP ngày 31/12/2025 quy định chi tiết một số điều và biện pháp thi hành Luật Bảo vệ dữ liệu cá nhân.",
 "Philips, L. (2000). The double metaphone search algorithm. C/C++ Users Journal, 18(6), 38-43.",
 "The Unicode Consortium. Unicode Standard Annex #15: Unicode Normalization Forms.",
 "Thủ tướng Chính phủ (2002). Quyết định 72/2002/QĐ-TTg ngày 10/6/2002 về việc thống nhất dùng bộ mã các ký tự chữ Việt theo tiêu chuẩn TCVN 6909:2001 trong trao đổi thông tin điện tử giữa các tổ chức của Đảng và Nhà nước.",
 "Quốc hội (2025). Nghị quyết 202/2025/QH15 ngày 12/6/2025 về việc sắp xếp đơn vị hành chính cấp tỉnh.",
 "Quốc hội (2025). Luật Tổ chức chính quyền địa phương số 72/2025/QH15 ngày 16/6/2025.",
]''')
rep('"Nghiên cứu tài liệu [1] đến [26]', '"Nghiên cứu tài liệu [1] đến [31]')
open(p, 'w', encoding='utf8').write(s)
print('patched')
