 # Nhập số nguyên dương n
n = int(input("Nhập số nguyên dương n: "))

# a. Tổng bình phương của các số nguyên dương nhỏ hơn n
sum_squares_comp = sum([x*x for x in range(1, n)])  # List Comprehension
sum_squares_lambda = sum(map(lambda x: x*x, range(1, n)))  # Anonymous Function

print("a. Tổng bình phương của các số nguyên dương nhỏ hơn n:")
print("   - List Comprehension:", sum_squares_comp)
print("   - Anonymous Function:", sum_squares_lambda)

# b. Tổng bình phương của các số lẻ nhỏ hơn n
sum_odd_squares_comp = sum([x*x for x in range(1, n) if x % 2 == 1])  # List Comprehension
sum_odd_squares_lambda = sum(map(lambda x: x*x, filter(lambda x: x % 2 == 1, range(1, n))))  # Anonymous Function

print("\nb. Tổng bình phương của các số lẻ nhỏ hơn n:")
print("   - List Comprehension:", sum_odd_squares_comp)
print("   - Anonymous Function:", sum_odd_squares_lambda)

# c. Tổng bình phương của các số nguyên dương từ 1 đến k sao cho k*k <= n
sum_limit_squares_comp = sum([x*x for x in range(1, n) if x*x <= n])  # List Comprehension
sum_limit_squares_lambda = sum(map(lambda x: x*x, filter(lambda x: x*x <= n, range(1, n))))  # Anonymous Function

print("\nc. Tổng bình phương của các số nguyên dương từ 1 đến k sao cho k*k <= n:")
print("   - List Comprehension:", sum_limit_squares_comp)
print("   - Anonymous Function:", sum_limit_squares_lambda)
