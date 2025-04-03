# a) Hàm nhận 1 đối số là số nguyên n và trả về trị tuyệt đối của n.
abs_value = lambda n: abs(n)

# b) Hàm nhận 1 đối số là số nguyên n và trả về giá trị của n + 15.
add_15 = lambda n: n + 15

# c) Hàm nhận 2 đối số là số nguyên (x, y), trả về tích của x và y.
multiply = lambda x, y: x * y

# d) Hàm nhận 2 đối số là số nguyên (x, y), trả về tổng các số từ x đến y.
sum_range = lambda x, y: sum(range(x, y + 1))

# e) Hàm nhận 1 đối số là số nguyên n nằm trong khoảng từ 0 đến 9, hàm thực hiện in ra chữ số tương ứng.
num_to_word = lambda n: {0: 'không', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bốn', 5: 'năm', 
                          6: 'sáu', 7: 'bảy', 8: 'tám', 9: 'chín'}.get(n, "Không hợp lệ")

# f) Hàm nhận 1 đối số là số thực (float) là điểm trung bình dtb. Hàm trả về xếp loại tương ứng.
grade = lambda dtb: "xuất sắc" if dtb >= 9 else "giỏi" if dtb >= 8 else "khá" if dtb >= 6.5 else "trung bình" if dtb >= 5 else "yếu"

# g) Hàm nhận 1 đối số là số thực r là bán kính của hình tròn. Cho biết diện tích và chu vi hình tròn.
circle_properties = lambda r: (3.14159 * r ** 2, 2 * 3.14159 * r)  # Trả về tuple (diện tích, chu vi)

# h) Hàm nhận 2 đối số là số thực d, r là chiều dài và chiều rộng của hình chữ nhật. Cho biết chu vi và diện tích hình chữ nhật.
rectangle_properties = lambda d, r: (2 * (d + r), d * r)  # Trả về tuple (chu vi, diện tích)

# i) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là bội số của 13 hoặc 19 hay không?
is_multiple_of_13_or_19 = lambda n: n % 13 == 0 or n % 19 == 0

# j) Hàm nhận 3 tham số là số nguyên (a, b, c). Cho biết a, b, c có là 3 cạnh hợp lệ của 1 tam giác hay không?
is_valid_triangle = lambda a, b, c: a + b > c and a + c > b and b + c > a


 # Kiểm tra xem n có phải là bội số của 13 hoặc 19 hay không
is_multiple_of_13_or_19 = lambda n: print(f"{n} là bội số của 13 hoặc 19") if (n % 13 == 0 or n % 19 == 0) else print(f"{n} không là bội số của 13 hoặc 19")

# Ví dụ sử dụng:
is_multiple_of_13_or_19(38)  # Output: 38 là bội số của 13 hoặc 19
is_multiple_of_13_or_19(8)   # Output: 8 không là bội số của 13 hoặc 19
