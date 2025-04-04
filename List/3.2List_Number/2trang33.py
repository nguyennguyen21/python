# Nhập 3 giá trị từ bàn phím
a = input("Nhập chuỗi: ")        # Chuỗi
b = int(input("Nhập số nguyên: ")) # Số nguyên
c = float(input("Nhập số thực: ")) # Số thực


L = [a, b, c]

x = L[0]
y = L[1]
z = L[2]

print(f"Cách 1 - Giá trị của x, y, z: {x}, {y}, {z}")


x, y, z = L  

print(f"Cách 2 - Giá trị của x, y, z: {x}, {y}, {z}")
