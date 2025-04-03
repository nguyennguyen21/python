import random

# Hàm ẩn danh kiểm tra và yêu cầu nhập số nguyên dương
get_positive_number = lambda x: int(input("Nhập số nguyên dương: ")) if x == 0 else int(input("Chỉ nhận số >0. Yêu cầu nhập lại.\nNhập số nguyên dương: "))

# Chạy vòng lặp while để yêu cầu người dùng nhập số nguyên dương
while True:
    # Nhập số với tham số x = 0 khi lần đầu
    number = get_positive_number(0)
    
    # Kiểm tra nếu nhập đúng số nguyên dương
    if number > 0:
        break  # Nếu đúng, thoát khỏi vòng lặp
    else:
        # Nếu nhập sai, yêu cầu nhập lại
        get_positive_number(1)

# In ra n số ngẫu nhiên từ -100 đến +200
random_numbers = [random.randint(-100, 200) for _ in range(number)]
print(" ".join(map(str, random_numbers)))
