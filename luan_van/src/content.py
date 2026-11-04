TITLE = ("Nghiên cứu tối ưu hóa quy tắc làm sạch, chuẩn hóa và so khớp mờ nhằm giảm cảnh báo sai "
         "trong hệ thống sàng lọc cấm vận giao dịch thanh toán quốc tế qua mạng SWIFT: "
         "thực nghiệm trên nền tảng Oracle Enterprise Data Quality")
ORG = "Học viện Công nghệ Bưu chính Viễn thông"
PI = "Nguyễn Văn Phê (mã học viên: B26CHHT080)"
MONTHS = "12"
KEYWORDS = ("sàng lọc cấm vận; phòng, chống rửa tiền (AML); so khớp tên mờ; chất lượng dữ liệu; "
            "Oracle EDQ; SWIFT; ISO 20022; cảnh báo sai (false positive)")

ABSTRACT = [
    "Sàng lọc cấm vận (sanctions screening) là yêu cầu bắt buộc đối với các ngân hàng tham gia thanh toán quốc tế qua mạng SWIFT: "
    "mọi bên liên quan trong điện thanh toán phải được đối chiếu "
    "với các danh sách cấm vận (OFAC, Liên Hợp Quốc, EU, Vương quốc Anh, Việt Nam) trước khi giao dịch được xử lý. "
    "Do tên người và tổ chức có nhiều biến thể (phiên âm, viết tắt, lỗi nhập liệu, bỏ dấu, đảo thứ tự), các hệ thống sàng lọc phải dùng kỹ thuật so khớp mờ, "
    "dẫn đến tỷ lệ cảnh báo sai rất cao, thường trên 90%, trong khi nới lỏng quy tắc lại làm tăng nguy cơ bỏ sót đối tượng bị cấm vận.",
    "Đề tài nghiên cứu một cách định lượng ảnh hưởng của các bước làm sạch, chuẩn hóa dữ liệu, chiến lược phân cụm (clustering) và quy tắc so khớp nâng cao "
    "(Advanced Match) đến độ chính xác (Precision) và độ bao phủ (Recall) của hệ thống sàng lọc xây dựng trên nền tảng Oracle Enterprise Data Quality (OEDQ), "
    "thông qua việc xây dựng bộ dữ liệu kiểm thử có gán nhãn từ các danh sách cấm vận công khai kết hợp kỹ thuật sinh biến thể tên có kiểm soát và điện thanh toán "
    "tổng hợp theo định dạng SWIFT MT và ISO 20022 (MX); từ đó đề xuất bộ quy tắc tối ưu (đặc biệt cho tên tiếng Việt) và khung kiểm định, hiệu chỉnh định kỳ cho các ngân hàng Việt Nam. "
    "Mục tiêu định lượng là giảm ít nhất 30% số cảnh báo sai so với cấu hình nền trong khi duy trì Recall không thấp hơn 99% trên bộ dữ liệu kiểm thử.",
]

S21 = [
    "## a) Tình hình nghiên cứu ngoài nước",
    "**So khớp tên và liên kết bản ghi.** Bài toán so khớp tên là một trường hợp của liên kết bản ghi (record linkage) với nền tảng lý thuyết xác suất "
    "do Fellegi và Sunter đặt ra [1]. Winkler phát triển độ đo Jaro-Winkler phù hợp với chuỗi ngắn như tên người [2]. Cohen và cộng sự [3], Branting [4] "
    "đã so sánh có hệ thống các độ đo khoảng cách chuỗi (Levenshtein, Jaro-Winkler, TF-IDF, Monge-Elkan, các phương pháp lai) cho bài toán so khớp tên và "
    "cho thấy không có độ đo nào vượt trội trong mọi trường hợp; hiệu quả phụ thuộc mạnh vào đặc điểm dữ liệu và bước tiền xử lý. Christen [5] tổng hợp "
    "toàn bộ quy trình liên kết dữ liệu: làm sạch, chuẩn hóa, phân khối (blocking/indexing), so sánh, phân loại và đánh giá. Papadakis và cộng sự [6] "
    "khảo sát các kỹ thuật phân khối, chỉ ra sự đánh đổi giữa chi phí tính toán và khả năng bỏ sót cặp khớp đúng, tương ứng trực tiếp với cơ chế "
    "clustering trong OEDQ. Gần đây, các mô hình học sâu như DeepMatcher [7], Ditto [8] và mô hình ngôn ngữ lớn [9] được áp dụng cho so khớp thực thể, "
    "đạt kết quả cao trên dữ liệu thương mại điện tử nhưng chưa được kiểm chứng rộng rãi trong bối cảnh sàng lọc cấm vận đòi hỏi tính giải thích và kiểm toán.",
    "**Sàng lọc cấm vận và phòng, chống rửa tiền.** Khuyến nghị 6 và 7 của FATF yêu cầu các quốc gia thực thi biện pháp trừng phạt tài chính có mục tiêu [10]. "
    "Bộ Tài chính Hoa Kỳ (OFAC) ban hành Khung cam kết tuân thủ OFAC (2019), nhấn mạnh việc kiểm thử và đánh giá định kỳ hệ thống sàng lọc [11]. "
    "Quy định NYDFS Part 504 (2016) yêu cầu các tổ chức tài chính chứng minh hệ thống lọc giao dịch được kiểm thử, hiệu chỉnh và quản trị dữ liệu đầy đủ [12]. "
    "Nhóm Wolfsberg (2019) ban hành hướng dẫn về sàng lọc cấm vận, trong đó khuyến nghị đo lường hiệu quả hệ thống bằng kiểm thử có kiểm soát "
    "(tên biến thể, kiểm tra hồi quy) thay vì chỉ dựa vào cấu hình mặc định của nhà cung cấp [13]. Về học máy cho AML, Chen và cộng sự [14] tổng quan các "
    "kỹ thuật phát hiện giao dịch đáng ngờ; Weber và cộng sự [15], Altman và cộng sự [16] xây dựng dữ liệu và mô hình đồ thị cho phát hiện rửa tiền. "
    "Tuy nhiên, phần lớn nghiên cứu học thuật tập trung vào giám sát giao dịch (transaction monitoring); mảng sàng lọc cấm vận chủ yếu được phát triển trong "
    "các sản phẩm thương mại (Oracle EDQ, LexisNexis Firco, SAS, NICE Actimize...) với ít công bố định lượng về hiệu quả cấu hình quy tắc.",
    "**Chuyển đổi chuẩn ISO 20022.** SWIFT đã kết thúc giai đoạn song song MT/MX đối với điện thanh toán xuyên biên giới vào ngày 22/11/2025 [17]. "
    "Điện MX (pacs.008, pacs.009) cung cấp dữ liệu có cấu trúc (tên, địa chỉ phân tách, mã quốc gia, LEI), mở ra khả năng sàng lọc theo từng thuộc tính, "
    "nhưng đồng thời đòi hỏi thiết kế lại luồng trích xuất và quy tắc so khớp. Đây là vấn đề mới, còn ít nghiên cứu đánh giá thực nghiệm.",
    "## b) Tình hình nghiên cứu trong nước",
    "Khung pháp lý tại Việt Nam đã được hoàn thiện đáng kể với Luật Phòng, chống rửa tiền số 14/2022/QH15, Nghị định 19/2023/NĐ-CP, Thông tư 27/2025/TT-NHNN (thay thế Thông tư 09/2023/TT-NHNN) "
    "và Nghị định 81/2019/NĐ-CP về phòng, chống phổ biến vũ khí hủy diệt hàng loạt, trong đó yêu cầu đối tượng báo cáo rà soát khách hàng và giao dịch với "
    "danh sách đen, danh sách cảnh báo [18-21]. Từ tháng 6/2023, Việt Nam bị FATF đưa vào danh sách các quốc gia bị tăng cường giám sát và vẫn nằm trong danh sách này sau kỳ họp toàn thể tháng 6/2026, tạo áp lực lớn "
    "về nâng cao hiệu quả thực thi. Các nghiên cứu trong nước về AML chủ yếu tiếp cận dưới góc độ pháp lý, quản trị rủi ro và kinh nghiệm quốc tế; "
    "một số nghiên cứu ứng dụng học máy cho phát hiện gian lận, giao dịch bất thường. Theo tìm hiểu của nhóm, hiện chưa có nghiên cứu thực nghiệm định lượng "
    "nào công bố về hiệu quả so khớp tên trong sàng lọc cấm vận, đặc biệt với đặc thù tên tiếng Việt không dấu (tỷ lệ trùng họ, tên đệm rất cao) "
    "và tên doanh nghiệp Việt Nam có nhiều tiền tố/hậu tố pháp lý (CÔNG TY TNHH, CTCP, JSC, CO., LTD...).",
    "## c) Nhận xét và kết quả nghiên cứu của chủ nhiệm đề tài",
    "Từ tổng quan trên, có thể thấy khoảng trống nghiên cứu: (i) thiếu phương pháp kiểm thử định lượng, có thể lặp lại cho hệ thống sàng lọc cấm vận; "
    "(ii) thiếu đánh giá tác động riêng rẽ của từng bước làm sạch, chuẩn hóa, phân cụm và quy tắc so khớp; (iii) chưa có nghiên cứu cho đặc thù tên Việt Nam "
    "và bối cảnh chuyển đổi ISO 20022 tại các ngân hàng Việt Nam.",
    "Chủ nhiệm đề tài hiện trực tiếp tham gia xây dựng và vận hành hệ thống sàng lọc cấm vận cho giao dịch thanh toán quốc tế qua SWIFT trên nền tảng OEDQ "
    "tại Ngân hàng Thương mại Cổ phần Quân đội (MB), bao gồm thiết kế quy tắc làm sạch, chuẩn hóa dữ liệu và cấu hình Advanced Match. "
    "[Bổ sung các bài báo, báo cáo, dự án đã thực hiện nếu có.]",
    "## Tài liệu tham khảo chính",
    "[1] Fellegi, I. P., & Sunter, A. B. (1969). A theory for record linkage. Journal of the American Statistical Association, 64(328), 1183-1210.",
    "[2] Winkler, W. E. (1990). String comparator metrics and enhanced decision rules in the Fellegi-Sunter model of record linkage. Proceedings of the Section on Survey Research Methods, American Statistical Association, 354-369.",
    "[3] Cohen, W. W., Ravikumar, P., & Fienberg, S. E. (2003). A comparison of string distance metrics for name-matching tasks. Proceedings of the IJCAI-03 Workshop on Information Integration on the Web (IIWeb-03).",
    "[4] Branting, L. K. (2003). A comparative evaluation of name-matching algorithms. Proceedings of the 9th International Conference on Artificial Intelligence and Law (ICAIL 2003), ACM.",
    "[5] Christen, P. (2012). Data Matching: Concepts and Techniques for Record Linkage, Entity Resolution, and Duplicate Detection. Springer.",
    "[6] Papadakis, G., Skoutas, D., Thanos, E., & Palpanas, T. (2020). Blocking and filtering techniques for entity resolution: A survey. ACM Computing Surveys, 53(2). https://doi.org/10.1145/3377455",
    "[7] Mudgal, S., et al. (2018). Deep learning for entity matching: A design space exploration. Proceedings of the 2018 International Conference on Management of Data (SIGMOD '18), ACM. https://doi.org/10.1145/3183713.3196926",
    "[8] Li, Y., Li, J., Suhara, Y., Doan, A., & Tan, W.-C. (2021). Deep entity matching with pre-trained language models. PVLDB, 14(1), 50-60.",
    "[9] Peeters, R., Steiner, A., & Bizer, C. (2025). Entity matching using large language models. Proceedings of the 28th International Conference on Extending Database Technology (EDBT 2025), 529-541.",
    "[10] FATF (2012, cập nhật). International Standards on Combating Money Laundering and the Financing of Terrorism & Proliferation, The FATF Recommendations.",
    "[11] U.S. Department of the Treasury, OFAC (2019). A Framework for OFAC Compliance Commitments.",
    "[12] New York State Department of Financial Services (2016). 3 NYCRR Part 504, Banking Division Transaction Monitoring and Filtering Program Requirements and Certifications.",
    "[13] The Wolfsberg Group (2019). Wolfsberg Guidance on Sanctions Screening.",
    "[14] Chen, Z., et al. (2018). Machine learning techniques for anti-money laundering (AML) solutions in suspicious transaction detection: a review. Knowledge and Information Systems, 57(2), 245-285. https://doi.org/10.1007/s10115-017-1144-z",
    "[15] Weber, M., et al. (2019). Anti-money laundering in Bitcoin: Experimenting with graph convolutional networks for financial forensics. KDD Workshop on Anomaly Detection in Finance.",
    "[16] Altman, E., et al. (2023). Realistic synthetic financial transactions for anti-money laundering models. Advances in Neural Information Processing Systems 36 (NeurIPS 2023), Datasets and Benchmarks Track.",
    "[17] SWIFT. ISO 20022 for Financial Institutions, Cross-border Payments and Reporting Plus (CBPR+); giai đoạn song song MT/MX kết thúc ngày 22/11/2025. https://www.swift.com",
    "[18] Quốc hội (2022). Luật Phòng, chống rửa tiền số 14/2022/QH15 ngày 15/11/2022.",
    "[19] Chính phủ (2023). Nghị định 19/2023/NĐ-CP ngày 28/4/2023 quy định chi tiết một số điều của Luật Phòng, chống rửa tiền.",
    "[20] Ngân hàng Nhà nước Việt Nam (2025). Thông tư 27/2025/TT-NHNN ngày 15/9/2025 hướng dẫn thực hiện Luật Phòng, chống rửa tiền (thay thế Thông tư 09/2023/TT-NHNN).",
    "[21] Chính phủ (2019). Nghị định 81/2019/NĐ-CP ngày 11/11/2019 về phòng, chống phổ biến vũ khí hủy diệt hàng loạt.",
]

S22 = [
    "**Vấn đề đề tài tập trung giải quyết:** Hệ thống sàng lọc cấm vận giao dịch SWIFT tại các ngân hàng phát sinh khối lượng lớn cảnh báo sai, "
    "trong khi việc điều chỉnh quy tắc hiện chủ yếu dựa trên kinh nghiệm và cấu hình mặc định của nhà cung cấp, thiếu cơ sở định lượng để chứng minh "
    "rằng việc giảm cảnh báo không làm tăng nguy cơ bỏ sót. Đề tài trả lời các câu hỏi nghiên cứu:",
    "- CH1: Từng bước làm sạch, chuẩn hóa dữ liệu (chuẩn hóa ký tự, bỏ dấu, loại từ nhiễu, chuẩn hóa tiền tố/hậu tố pháp lý, tách, ghép từ) ảnh hưởng như thế nào đến Precision và Recall?",
    "- CH2: Chiến lược phân cụm (clustering key) ảnh hưởng thế nào đến sự đánh đổi giữa hiệu năng xử lý và khả năng bỏ sót?",
    "- CH3: Tổ hợp quy tắc so khớp và ngưỡng nào cho hiệu quả tốt nhất với từng nhóm tên (Việt Nam, Trung Quốc, Ả Rập, Nga, Latinh) và loại thực thể (cá nhân, tổ chức, tàu)?",
    "- CH4: Dữ liệu có cấu trúc của điện ISO 20022 (MX) cải thiện hiệu quả sàng lọc như thế nào so với điện MT dạng văn bản tự do?",
    "**Tính mới:** (i) Lần đầu xây dựng bộ dữ liệu chuẩn có gán nhãn và khung kiểm thử định lượng cho sàng lọc cấm vận trong bối cảnh Việt Nam; "
    "(ii) đánh giá tách biệt tác động của từng thành phần trong chuỗi xử lý (ablation study) trên nền tảng sản phẩm thương mại thực tế; "
    "(iii) đề xuất quy tắc chuẩn hóa, so khớp riêng cho tên tiếng Việt và tên doanh nghiệp Việt Nam.",
    "**Tính thời sự:** Việt Nam vẫn nằm trong danh sách tăng cường giám sát của FATF (từ tháng 6/2023); SWIFT vừa hoàn tất chuyển đổi sang ISO 20022; các lệnh cấm vận quốc tế "
    "(liên quan xung đột Nga-Ukraine, Trung Đông...) được cập nhật liên tục với số lượng lớn, làm tăng mạnh khối lượng cảnh báo tại các ngân hàng.",
    "**Ý nghĩa khoa học:** Đóng góp phương pháp đánh giá thực nghiệm cho lĩnh vực so khớp tên trong một miền ứng dụng có yêu cầu đặc thù "
    "(chi phí bỏ sót rất lớn, yêu cầu giải thích và kiểm toán). **Ý nghĩa thực tiễn:** Kết quả giúp ngân hàng giảm chi phí xử lý cảnh báo, "
    "rút ngắn thời gian xử lý giao dịch, đồng thời có bằng chứng định lượng phục vụ kiểm toán nội bộ, thanh tra của NHNN và yêu cầu của ngân hàng đại lý.",
]

S3 = [
    "**Mục tiêu tổng quát:** Nâng cao hiệu quả hệ thống sàng lọc cấm vận giao dịch thanh toán quốc tế qua SWIFT thông qua tối ưu hóa có cơ sở định lượng "
    "các quy tắc làm sạch, chuẩn hóa dữ liệu và so khớp mờ trên nền tảng Oracle EDQ.",
    "**Mục tiêu cụ thể:**",
    "- MT1: Xây dựng bộ dữ liệu kiểm thử chuẩn có gán nhãn (tối thiểu 100.000 bản ghi) gồm biến thể tên của đối tượng trong các danh sách cấm vận công khai và điện thanh toán tổng hợp theo định dạng MT103/MT202 và pacs.008/pacs.009.",
    "- MT2: Đánh giá định lượng tác động của từng thành phần (làm sạch, chuẩn hóa, phân cụm, quy tắc so khớp, ngưỡng) đến Precision, Recall, F2-score, số cảnh báo trên 1.000 giao dịch và thời gian xử lý.",
    "- MT3: Đề xuất bộ cấu hình tối ưu giúp giảm ít nhất 30% cảnh báo sai so với cấu hình nền trong khi duy trì Recall ≥ 99% trên bộ dữ liệu kiểm thử.",
    "- MT4: Đề xuất khung phương pháp kiểm định và hiệu chỉnh định kỳ (tuning & testing framework) cho hệ thống sàng lọc cấm vận, phù hợp quy định Việt Nam và thông lệ quốc tế.",
]

S4 = [
    "# 4.1. Phạm vi nghiên cứu",
    "- Đối tượng: quy trình và hệ thống sàng lọc cấm vận theo thời gian thực đối với điện thanh toán quốc tế qua mạng SWIFT (điện chuyển tiền khách hàng và chuyển tiền giữa các định chế), không bao gồm giám sát giao dịch đáng ngờ theo hành vi.",
    "- Danh sách đối chiếu: OFAC SDN và Consolidated, Danh sách hợp nhất của Hội đồng Bảo an Liên Hợp Quốc, Danh sách trừng phạt tài chính hợp nhất của EU, Danh sách của Vương quốc Anh (OFSI/FCDO) và danh sách do cơ quan có thẩm quyền Việt Nam công bố.",
    "- Thực thể sàng lọc: cá nhân, tổ chức, tàu biển, quốc gia/vùng lãnh thổ, thành phố/cảng, mã BIC.",
    "- Nền tảng thực nghiệm: Oracle Enterprise Data Quality trên môi trường thử nghiệm độc lập, không kết nối với hệ thống thanh toán thật; các thuật toán so sánh bổ sung được cài đặt bằng Python.",
    "- Dữ liệu: dữ liệu công khai và dữ liệu tổng hợp. Dữ liệu giao dịch thực (nếu được ngân hàng cho phép) chỉ dùng ở dạng đã ẩn danh, tổng hợp số liệu, không công bố thông tin khách hàng hay cấu hình nội bộ chi tiết.",
    "# 4.2. Nội dung và phương pháp nghiên cứu",
    "## Nội dung 1: Tổng quan và khảo sát hiện trạng",
    "- Phương pháp: nghiên cứu tài liệu (các nguồn [1]-[21]), phân tích tài liệu kỹ thuật OEDQ (Watchlist Screening, các processor làm sạch, Advanced Match), phỏng vấn bán cấu trúc 5-7 chuyên viên tuân thủ và kỹ thuật về quy trình xử lý cảnh báo.",
    "- Kết quả: mô hình hóa quy trình sàng lọc hiện tại (BPMN), phân loại nguyên nhân phát sinh cảnh báo sai (trùng tên phổ biến, từ chung trong tên tổ chức, tên địa danh, tên tàu...), xác định cấu hình nền (baseline).",
    "## Nội dung 2: Xây dựng bộ dữ liệu kiểm thử chuẩn có gán nhãn",
    "- Thu thập và chuẩn hóa các danh sách cấm vận công khai (định dạng XML/CSV), hợp nhất bí danh (alias), ngày sinh, quốc tịch, địa chỉ.",
    "- Xây dựng công cụ sinh biến thể tên có kiểm soát theo phân loại lỗi trong hướng dẫn Wolfsberg [13]: lỗi gõ (chèn/xóa/thay/hoán vị ký tự), đảo thứ tự từ, viết tắt, bỏ hoặc thêm từ, ghép/tách từ, bỏ dấu, phiên âm khác nhau, thay ký tự đặc biệt, cắt cụt do giới hạn độ dài trường SWIFT (35 ký tự/dòng).",
    "- Sinh điện thanh toán tổng hợp theo MT103/MT202 (trường 50K, 59, 52A, 57A, 70, 72) và pacs.008/pacs.009, nhúng các biến thể tên vào các vị trí khác nhau; bổ sung tên khách hàng không bị cấm vận (gồm nhiều tên tiếng Việt, tên doanh nghiệp Việt Nam) làm mẫu âm.",
    "- Gán nhãn: mỗi cặp (điện, mục danh sách) được gán nhãn khớp đúng/không khớp; một mẫu ngẫu nhiên được chuyên gia kiểm tra chéo để đánh giá độ tin cậy nhãn (hệ số Cohen's Kappa).",
    "## Nội dung 3: Thực nghiệm tối ưu bước làm sạch và chuẩn hóa dữ liệu",
    "- Thiết kế thực nghiệm loại bỏ từng thành phần (ablation): bắt đầu từ cấu hình nền, lần lượt bật/tắt và thay đổi từng quy tắc: chuẩn hóa chữ hoa, ký tự đặc biệt; bỏ dấu tiếng Việt; danh sách từ nhiễu (noise words); chuẩn hóa hậu tố pháp lý (LIMITED/LTD, JOINT STOCK COMPANY/JSC, CÔNG TY TNHH...); chuẩn hóa tước hiệu, danh xưng; bảng quy đổi phiên âm phổ biến (MOHAMMED/MUHAMMAD...).",
    "- Đề xuất bộ quy tắc chuẩn hóa riêng cho tên tiếng Việt và tên doanh nghiệp Việt Nam.",
    "## Nội dung 4: Thực nghiệm tối ưu phân cụm, quy tắc so khớp và ngưỡng",
    "- Phân cụm: so sánh các khóa phân cụm (tiền tố ký tự, từ đã sắp xếp, mã ngữ âm như Metaphone, n-gram) theo hai tiêu chí: tỷ lệ cặp khớp đúng bị loại ở bước phân cụm (pair completeness) và số cặp so sánh/thời gian xử lý.",
    "- Quy tắc so khớp: đánh giá các phép so sánh trong Advanced Match (khớp chính xác, khoảng cách chỉnh sửa ký tự, số từ khớp, khớp từ có trọng số, khớp có hoán vị, khớp chứa) và độ đo bổ sung (Jaro-Winkler, Levenshtein chuẩn hóa, TF-IDF cosine trên n-gram) cài đặt bằng Python để đối chứng.",
    "- Sử dụng thuộc tính phụ (quốc gia, năm sinh, loại thực thể) như điều kiện tăng/giảm mức ưu tiên cảnh báo; so sánh sàng lọc theo thuộc tính trên điện MX với sàng lọc văn bản tự do trên điện MT.",
    "- Tối ưu ngưỡng bằng tìm kiếm lưới (grid search) với hàm mục tiêu: tối thiểu số cảnh báo sai với ràng buộc Recall ≥ 99%; báo cáo đường cong Precision-Recall và F2-score (ưu tiên Recall).",
    "- Kiểm định thống kê: dùng kiểm định McNemar và khoảng tin cậy bootstrap để khẳng định sự khác biệt giữa các cấu hình có ý nghĩa thống kê; đánh giá chéo theo từng nhóm tên và loại thực thể.",
    "## Nội dung 5: Đề xuất khung kiểm định, hiệu chỉnh định kỳ và đánh giá tổng thể",
    "- Xây dựng khung kiểm định gồm: kiểm tra tính đầy đủ, kịp thời của danh sách; kiểm tra toàn vẹn dữ liệu đầu vào (trích xuất đúng trường điện); kiểm thử hiệu quả so khớp bằng bộ dữ liệu chuẩn; kiểm thử hồi quy khi thay đổi quy tắc; chỉ số giám sát (KPI/KRI) và quy trình phê duyệt thay đổi.",
    "- Đối chiếu khung với Luật Phòng, chống rửa tiền 2022, Thông tư 27/2025/TT-NHNN, Khung tuân thủ OFAC, NYDFS Part 504 và hướng dẫn Wolfsberg.",
    "- Đánh giá tổng thể bộ cấu hình đề xuất; nếu được ngân hàng chấp thuận, chạy lại (back-test) trên tập điện lịch sử đã ẩn danh và so sánh với kết quả xử lý của chuyên viên.",
    "## Công cụ và kỹ thuật sử dụng",
    "- Oracle Enterprise Data Quality (Director, các processor làm sạch, chuẩn hóa, Advanced Match, Watchlist Screening); cơ sở dữ liệu Oracle/PostgreSQL lưu kết quả thực nghiệm.",
    "- Python (pandas, RapidFuzz, jellyfish, scikit-learn, SciPy) để sinh dữ liệu, cài đặt độ đo đối chứng và phân tích thống kê; Git để quản lý phiên bản cấu hình và kịch bản thực nghiệm, bảo đảm khả năng lặp lại.",
]

S4_EXPERT = [
    "Đề tài cần mời 01-02 chuyên gia trong nước để tư vấn và thẩm định kết quả: chuyên gia nghiệp vụ tuân thủ/phòng, chống rửa tiền tại ngân hàng thương mại "
    "(tối thiểu 5 năm kinh nghiệm xử lý cảnh báo cấm vận, ưu tiên có chứng chỉ CAMS/CGSS) và chuyên gia kỹ thuật về chất lượng dữ liệu/OEDQ "
    "(tối thiểu 3 năm kinh nghiệm triển khai). Chuyên gia tham gia phỏng vấn khảo sát, kiểm tra chéo nhãn dữ liệu và góp ý khung kiểm định. "
    "Không thuê chuyên gia nước ngoài.",
]
S4_ACT = [
    "- Khảo sát, phỏng vấn chuyên gia: phục vụ Nội dung 1 (hiện trạng, nguyên nhân cảnh báo sai) và kiểm tra chất lượng nhãn dữ liệu (Nội dung 2).",
    "- Tọa đàm/hội thảo chuyên môn (01 buổi): lấy ý kiến về bộ cấu hình và khung kiểm định đề xuất trước khi hoàn thiện (Nội dung 5).",
    "- Tham gia hội nghị khoa học trong nước để công bố kết quả.",
    "- Không có hoạt động thuê ngoài, đoàn ra, đoàn vào.",
]

S5_SUCCESS = [
    "Đề tài có khả năng thành công cao vì: (i) dữ liệu chính là các danh sách cấm vận công khai và dữ liệu tổng hợp, không phụ thuộc vào việc được cấp dữ liệu khách hàng; "
    "(ii) phương pháp thực nghiệm loại bỏ từng thành phần và tối ưu ngưỡng là phương pháp đã được kiểm chứng trong lĩnh vực liên kết bản ghi; "
    "(iii) nền tảng OEDQ đã được triển khai thực tế, chủ nhiệm đề tài nắm vững công cụ; (iv) mục tiêu định lượng (giảm ≥ 30% cảnh báo sai, Recall ≥ 99%) "
    "phù hợp với mức cải thiện thường đạt được khi tinh chỉnh quy tắc theo thông lệ ngành.",
]
S5_SOTA = ["Không áp dụng, đề tài không đăng ký bằng độc quyền sáng chế, giải pháp hữu ích hay giống cây trồng."]
S5_POT = ["Không áp dụng (đề tài không đăng ký loại hình Tiềm năng). Sản phẩm của đề tài là bộ dữ liệu kiểm thử, bộ cấu hình quy tắc và khung kiểm định có thể chuyển giao cho các ngân hàng."]
S5_CAP = [
    "Chủ nhiệm đề tài có kinh nghiệm thực tế trong xây dựng, vận hành hệ thống sàng lọc cấm vận giao dịch SWIFT trên nền tảng OEDQ (thiết kế quy tắc làm sạch, chuẩn hóa, so khớp nâng cao), "
    "hiểu rõ nghiệp vụ thanh toán quốc tế và yêu cầu tuân thủ. Người hướng dẫn khoa học: TS. Đỗ Trung Anh.",
]
S5_FAC = [
    "Tổ chức chủ trì có phòng máy, thư viện và cơ sở dữ liệu học thuật phục vụ nghiên cứu. Thực nghiệm OEDQ được thực hiện trên môi trường thử nghiệm độc lập "
    "(bản cài đặt phục vụ phát triển/kiểm thử hoặc môi trường do đơn vị công tác cho phép sử dụng), tách biệt hoàn toàn với hệ thống vận hành thật.",
]
EQUIP = [
    ("Máy chủ/máy ảo môi trường thử nghiệm Oracle EDQ", "Chạy thực nghiệm cấu hình làm sạch, chuẩn hóa, so khớp", "Ngân hàng TMCP Quân đội (MB)"),
    ("Máy tính cá nhân cấu hình cao (≥ 16 GB RAM)", "Sinh dữ liệu, cài đặt thuật toán đối chứng, phân tích thống kê bằng Python", "Chủ nhiệm đề tài"),
    ("Cơ sở dữ liệu học thuật, thư viện", "Tra cứu tài liệu, tổng quan nghiên cứu", "Tổ chức chủ trì"),
]

PLAN = [
    ("1", "Nội dung 1: Tổng quan và khảo sát hiện trạng", "T1-T2", "Chủ nhiệm", "Báo cáo tổng quan và hiện trạng"),
    ("1.1", "Công việc 1.1: Tổng quan tài liệu về so khớp tên, sàng lọc cấm vận, ISO 20022, quy định pháp lý", "T1-T2", "Chủ nhiệm", "Báo cáo tổng quan tài liệu"),
    ("1.2", "Công việc 1.2: Khảo sát quy trình, phỏng vấn chuyên gia, xác định cấu hình nền", "T2", "Chủ nhiệm, chuyên gia", "Mô hình quy trình (BPMN), phân loại nguyên nhân cảnh báo sai"),
    ("2", "Nội dung 2: Xây dựng bộ dữ liệu kiểm thử chuẩn", "T3-T4", "Chủ nhiệm", "Bộ dữ liệu có gán nhãn"),
    ("2.1", "Công việc 2.1: Thu thập, hợp nhất, chuẩn hóa danh sách cấm vận công khai", "T3", "Chủ nhiệm", "CSDL danh sách hợp nhất"),
    ("2.2", "Công việc 2.2: Xây dựng công cụ sinh biến thể tên và điện MT/MX tổng hợp; gán nhãn, kiểm tra chéo", "T3-T4", "Chủ nhiệm, chuyên gia", "Công cụ sinh dữ liệu; bộ dữ liệu ≥ 100.000 bản ghi"),
    ("3", "Nội dung 3: Thực nghiệm tối ưu làm sạch, chuẩn hóa", "T5-T6", "Chủ nhiệm", "Báo cáo kết quả thực nghiệm"),
    ("3.1", "Công việc 3.1: Thiết lập môi trường thực nghiệm, đo cấu hình nền", "T5", "Chủ nhiệm", "Kết quả baseline"),
    ("3.2", "Công việc 3.2: Thực nghiệm ablation các quy tắc chuẩn hóa; đề xuất quy tắc cho tên Việt Nam", "T5-T6", "Chủ nhiệm", "Bộ quy tắc chuẩn hóa đề xuất"),
    ("4", "Nội dung 4: Thực nghiệm phân cụm, quy tắc so khớp, ngưỡng", "T6-T8", "Chủ nhiệm", "Bộ cấu hình so khớp tối ưu"),
    ("4.1", "Công việc 4.1: Thực nghiệm khóa phân cụm và quy tắc Advanced Match; cài đặt độ đo đối chứng", "T6-T7", "Chủ nhiệm", "Bảng so sánh Precision/Recall/hiệu năng"),
    ("4.2", "Công việc 4.2: Tối ưu ngưỡng, so sánh MT và MX, kiểm định thống kê", "T7-T8", "Chủ nhiệm", "Cấu hình tối ưu; báo cáo kiểm định"),
    ("5", "Nội dung 5: Khung kiểm định và đánh giá tổng thể", "T9-T10", "Chủ nhiệm", "Khung kiểm định, hiệu chỉnh định kỳ"),
    ("5.1", "Công việc 5.1: Xây dựng khung kiểm định, đối chiếu quy định", "T9", "Chủ nhiệm", "Tài liệu khung kiểm định"),
    ("5.2", "Công việc 5.2: Tọa đàm lấy ý kiến chuyên gia; back-test trên dữ liệu ẩn danh (nếu được phép)", "T10", "Chủ nhiệm, chuyên gia", "Biên bản tọa đàm; báo cáo đánh giá"),
    ("6", "Nội dung 6: Công bố, báo cáo và tổng kết", "T6-T12", "Chủ nhiệm, người hướng dẫn", "Bài báo, báo cáo"),
    ("6.1", "Công việc 6.1: Báo cáo tiến độ giữa kỳ", "T6", "Chủ nhiệm", "Báo cáo giữa kỳ"),
    ("6.2", "Công việc 6.2: Viết và gửi bài báo tạp chí, báo cáo hội thảo", "T9-T12", "Chủ nhiệm, người hướng dẫn", "01 bài báo, 01 báo cáo hội thảo"),
    ("6.3", "Công việc 6.3: Hoàn thiện báo cáo tổng kết/luận văn", "T11-T12", "Chủ nhiệm", "Báo cáo tổng kết/luận văn thạc sĩ"),
]

S71 = [
    "- Bộ dữ liệu kiểm thử chuẩn có gán nhãn (≥ 100.000 bản ghi) và công cụ sinh biến thể tên, điện thanh toán MT/MX tổng hợp, có thể tái sử dụng cho kiểm thử định kỳ.",
    "- Bộ kết quả thực nghiệm định lượng về tác động của từng bước làm sạch, chuẩn hóa, phân cụm, quy tắc so khớp và ngưỡng đến Precision, Recall, F2-score và hiệu năng.",
    "- Bộ cấu hình quy tắc tối ưu trên OEDQ (mô tả ở mức nguyên lý, không lộ cấu hình nội bộ), đặc biệt cho tên tiếng Việt và doanh nghiệp Việt Nam; mục tiêu giảm ≥ 30% cảnh báo sai, Recall ≥ 99%.",
    "- Khung phương pháp kiểm định và hiệu chỉnh định kỳ hệ thống sàng lọc cấm vận phù hợp quy định Việt Nam và thông lệ quốc tế.",
    "**Ý nghĩa khoa học:** bổ sung bằng chứng thực nghiệm cho lĩnh vực so khớp tên/liên kết bản ghi trong miền ứng dụng có chi phí bỏ sót cao; "
    "cung cấp phương pháp đánh giá có thể lặp lại. **Tác động đến ngành:** làm cơ sở để các ngân hàng chuẩn hóa việc kiểm thử, hiệu chỉnh hệ thống sàng lọc, nâng cao hiệu quả tuân thủ.",
]
PUB = {
    1: ("0", "Ghi cụ thể:\n- Số bài báo trên tạp chí Q1: 0; Q2: 0.\n- Danh sách tạp chí: không đăng ký."),
    5: ("01", "Tạp chí Ngân hàng hoặc Tạp chí Khoa học & Đào tạo Ngân hàng hoặc tạp chí chuyên ngành HTTT/CNTT trong nước"),
    7: ("01", "Hội thảo khoa học quốc gia/quốc tế về CNTT, HTTT hoặc tài chính, ngân hàng tổ chức tại Việt Nam"),
    9: ("03", "Bộ dữ liệu kiểm thử và công cụ sinh dữ liệu; bộ cấu hình quy tắc đề xuất; khung kiểm định"),
    11: ("01", "Chủ nhiệm đề tài bảo vệ luận văn thạc sĩ Hệ thống thông tin"),
}
for k in (2, 3, 4, 6, 8, 10):
    PUB[k] = ("0", "")

S73 = [
    "- Góp phần nâng cao năng lực thực thi các biện pháp trừng phạt tài chính có mục tiêu và phòng, chống rửa tiền, tài trợ khủng bố, tài trợ phổ biến vũ khí hủy diệt hàng loạt của hệ thống ngân hàng Việt Nam, hỗ trợ mục tiêu đưa Việt Nam ra khỏi danh sách tăng cường giám sát của FATF.",
    "- Giảm chi phí vận hành và thời gian chờ xử lý giao dịch thanh toán quốc tế cho doanh nghiệp, người dân; giảm số khách hàng hợp pháp (đặc biệt người có tên phổ biến) bị chặn, giữ giao dịch do cảnh báo sai.",
    "- Giảm rủi ro bị phạt, mất quan hệ ngân hàng đại lý (de-risking) do vi phạm cấm vận, qua đó bảo vệ uy tín hệ thống ngân hàng và hoạt động xuất nhập khẩu.",
    "- Cung cấp tài liệu tham khảo cho giảng dạy, đào tạo về hệ thống thông tin trong lĩnh vực tài chính, ngân hàng và tuân thủ.",
]
S74 = [
    "Kết quả có thể ứng dụng trực tiếp tại Ngân hàng Thương mại Cổ phần Quân đội (MB) và các ngân hàng thương mại, chi nhánh ngân hàng nước ngoài tại Việt Nam đang sử dụng OEDQ "
    "hoặc các giải pháp sàng lọc khác (khung kiểm định và bộ dữ liệu kiểm thử không phụ thuộc sản phẩm). Phương thức chuyển giao: báo cáo kỹ thuật, "
    "tài liệu hướng dẫn, hội thảo/tọa đàm chia sẻ kết quả; bộ dữ liệu tổng hợp và công cụ sinh dữ liệu có thể công bố mã nguồn mở (không chứa dữ liệu thật).",
]
FUND_NONE = "Không có"
