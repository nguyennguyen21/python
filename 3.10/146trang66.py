S = "python 3.10.1"
# dùng lambda
tong = sum(map(lambda x: int(x), filter(lambda ch: ch.isdigit(), S)))
print("Tổng các ký số là:", tong)
# không dùng lambda
tong_chu_so = sum(int(char) for char in S if char.isdigit())
print(tong_chu_so)