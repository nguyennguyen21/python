# Định nghĩa hàm lambda_in_function
def lambda_in_function(n):
    return lambda x: x * n

# Lấy hàm lambda với n = 15
lambda_func = lambda_in_function(15)

# Thực hiện nhân với các giá trị x từ 2 đến 10
for x in range(2, 11):
    print(f"{x} * 15 = {lambda_func(x)}")
