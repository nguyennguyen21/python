def thay_the_not_poor(S):
    # Kiểm tra xem từ 'not' có xuất hiện và từ 'poor' có xuất hiện sau nó không
    not_index = S.find('not')
    poor_index = S.find('poor')
    
    # Nếu 'not' xuất hiện trước 'poor', thay thế đoạn đó bằng 'good'
    if not_index != -1 and poor_index != -1 and poor_index > not_index:
        # Thay thế phần từ 'not' đến 'poor' bằng 'good'
        S = S[:not_index] + 'good' + S[poor_index + len('poor'):]

    return S

# Nhập chuỗi S từ người dùng
S = input("Nhập chuỗi S: ")

# Gọi hàm và in kết quả
result = thay_the_not_poor(S)
print(result)
