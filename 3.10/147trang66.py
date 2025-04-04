import random

# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

# Tạo list L gồm n số nguyên ngẫu nhiên từ -100 đến 100
L = [random.randint(-100, 100) for _ in range(n)]
print("List L:", L)

# Dùng list comprehension để lọc các số > 0
M1 = [x for x in L if x > 0]
print("List M1 (dùng list comprehension):", M1)

# Dùng anonymous function (lambda) với filter để lọc các số > 0
M2 = list(filter(lambda x: x > 0, L))
print("List M2 (dùng filter và lambda):", M2)

print(" Danh sách số nguyên ban đầu (L):", L)
print("Những số dương lung linh (M1):", M1)
