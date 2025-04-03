def kiem_tra_so_dong_nhat(n):
    if n <= 0:
        return False  # Số không hợp lệ
    dau = n % 10  # Lấy chữ số cuối cùng
    while n > 0:
        if n % 10 != dau:  # Kiểm tra chữ số cuối có giống chữ số đầu không
            return False
        n //= 10  # Lấy số nguyên (loại bỏ chữ số cuối)
    return True

def kiem_tra_so_dong_nhat_str(n):
    s = str(n)  # Chuyển số n thành chuỗi
    return all(char == s[0] for char in s)  # Kiểm tra xem tất cả các ký tự có giống nhau không

def liet_ke_so_dong_nhat(n):
    result = []
    for i in range(1, n + 1):
        if kiem_tra_so_dong_nhat(i):
            result.append(i)
    return result

def liet_ke_so_dong_nhat_str(n):
    result = []
    for i in range(1, n + 1):
        if kiem_tra_so_dong_nhat_str(i):
            result.append(i)
    return result

# Nhập số nguyên từ người dùng
n = int(input("Nhập số nguyên dương n: "))

# Kiểm tra số n có phải là số đồng nhất không
if kiem_tra_so_dong_nhat(n):
    print(f"{n} là số đồng nhất (Cách 1 - Số nguyên)")
else:
    print(f"{n} không phải là số đồng nhất (Cách 1 - Số nguyên)")

if kiem_tra_so_dong_nhat_str(n):
    print(f"{n} là số đồng nhất (Cách 2 - Chuỗi)")
else:
    print(f"{n} không phải là số đồng nhất (Cách 2 - Chuỗi)")

# Liệt kê các số đồng nhất nhỏ hơn hoặc bằng n (Cách 1 - Số nguyên)
result_1 = liet_ke_so_dong_nhat(n)
print("Các số đồng nhất nhỏ hơn hoặc bằng n (Cách 1 - Số nguyên):")
print(result_1)

# Liệt kê các số đồng nhất nhỏ hơn hoặc bằng n (Cách 2 - Chuỗi)
result_2 = liet_ke_so_dong_nhat_str(n)
print("Các số đồng nhất nhỏ hơn hoặc bằng n (Cách 2 - Chuỗi):")
print(result_2)
