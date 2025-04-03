def NhapSoNhiphan():
    S = input("Nhập chuỗi nhị phân: ")  # Nhập chuỗi nhị phân
    while not all(char in '01' for char in S):  # Kiểm tra tất cả ký tự trong chuỗi
        print("Nhập lại chuỗi nhị phân hợp lệ (chỉ chứa 0 và 1).")
        S = input("Nhập chuỗi nhị phân: ")
    return S  # Trả về chuỗi nhị phân hợp lệ

def tim_do_dai_lien_tiep(S):
    max_length = 0  # Độ dài lớn nhất của chuỗi '0' liên tiếp
    current_length = 0  # Độ dài của chuỗi '0' hiện tại

    for char in S:
        if char == '0':
            current_length += 1  # Nếu là '0', tăng độ dài chuỗi '0'
        else:
            # Nếu gặp '1', so sánh độ dài chuỗi '0' hiện tại với max_length
            if current_length > max_length:
                max_length = current_length
            current_length = 0  # Đặt lại độ dài chuỗi '0' hiện tại khi gặp '1'

    # Kiểm tra lần cuối nếu chuỗi '0' kết thúc ở cuối chuỗi
    if current_length > max_length:
        max_length = current_length

    return max_length

# Nhập chuỗi nhị phân từ người dùng
S = NhapSoNhiphan()

# Gọi hàm và in kết quả
result = tim_do_dai_lien_tiep(S)
print(result)
