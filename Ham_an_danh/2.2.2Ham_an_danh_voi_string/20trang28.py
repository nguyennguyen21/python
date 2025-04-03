# Nhập chuỗi từ người dùng
S = input("Nhập chuỗi S: ")

# Tính tổng các ký số trong chuỗi
sum_digits = sum(int(c) for c in S if c.isdigit())

# In kết quả
print(f"Tổng các ký số trong chuỗi: {sum_digits}")
 