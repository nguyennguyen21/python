import math

# Nhập chuỗi số từ bàn phím
S = input("Nhập dãy số cách nhau bởi dấu phẩy: ")

# Chuyển chuỗi thành danh sách số nguyên
listS = [int(num.strip()) for num in S.split(',')]

# ---------------------- Bước b ----------------------

# Cách 1: Tính tổng bằng vòng lặp
sum_using_loop = 0
for num in listS:
    sum_using_loop += num

print(f"Cách 1 - Tổng các số (dùng vòng lặp): {sum_using_loop}")

# Cách 2: Tính tổng bằng hàm sum
sum_using_sum = sum(listS)
print(f"Cách 2 - Tổng các số (dùng hàm sum): {sum_using_sum}")


# ---------------------- Bước c ----------------------

# Cách 1: Tính tích bằng vòng lặp
product_using_loop = 1
for num in listS:
    product_using_loop *= num

print(f"Cách 1 - Tích các số (dùng vòng lặp): {product_using_loop}")

# Cách 2: Tính tích bằng hàm math.prod
product_using_prod = math.prod(listS)
print(f"Cách 2 - Tích các số (dùng hàm math.prod): {product_using_prod}")


# ---------------------- Bước d ----------------------

# Cách 1: Tìm số nhỏ nhất bằng vòng lặp
min_using_loop = listS[0]
for num in listS:
    if num < min_using_loop:
        min_using_loop = num

print(f"Cách 1 - Số nhỏ nhất (dùng vòng lặp): {min_using_loop}")

# Cách 2: Tìm số nhỏ nhất bằng hàm min
min_using_min = min(listS)
print(f"Cách 2 - Số nhỏ nhất (dùng hàm min): {min_using_min}")
