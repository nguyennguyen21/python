import math

# a) Số thân thiện (Friendly number)
is_friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

# b) Số chính phương (Perfect Square)
is_perfect_square = lambda n: int(math.sqrt(n))**2 == n

# c) Số đồng nhất (Uniform number)
is_uniform = lambda n: all(digit == str(n)[0] for digit in str(n))

# d) Số hoàn thiện (Perfect number)
is_perfect_number = lambda n: sum([i for i in range(1, n) if n % i == 0]) == n

# e) Số phong phú (Abundant number)
is_abundant = lambda n: sum([i for i in range(1, n) if n % i == 0]) > n

# f) Số tăng dần (Increasing number)
is_increasing = lambda n: all(int(str(n)[i]) <= int(str(n)[i+1]) for i in range(len(str(n)) - 1))

# g) Số Armstrong
is_armstrong = lambda n: n == sum([int(digit)**len(str(n)) for digit in str(n)])

# h) Số nguyên tố (Prime number)
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# i) Số Palindrome
is_palindrome = lambda n: str(n) == str(n)[::-1]

# j) Số nguyên tố Palindrome
is_prime_palindrome = lambda n: is_prime(n) and is_palindrome(n)

# k) Số lộc phát (Lucky number)
is_lucky = lambda n: all(digit in '68' for digit in str(n))

# l) Số lộc phát Palindrome
is_lucky_palindrome = lambda n: is_lucky(n) and is_palindrome(n)

# In các số thỏa mãn yêu cầu trong khoảng từ 1 đến 1 triệu
for n in range(1, 1000001):
    if is_friendly(n):
        print(f"{n} là số thân thiện")
    if is_perfect_square(n):
        print(f"{n} là số chính phương")
    if is_uniform(n):
        print(f"{n} là số đồng nhất")
    if is_perfect_number(n):
        print(f"{n} là số hoàn thiện")
    if is_abundant(n):
        print(f"{n} là số phong phú")
    if is_increasing(n):
        print(f"{n} là số tăng dần")
    if is_armstrong(n):
        print(f"{n} là số Armstrong")
    if is_prime(n):
        print(f"{n} là số nguyên tố")
    if is_palindrome(n):
        print(f"{n} là số Palindrome")
    if is_prime_palindrome(n):
        print(f"{n} là số nguyên tố Palindrome")
    if is_lucky(n):
        print(f"{n} là số lộc phát")
    if is_lucky_palindrome(n):
        print(f"{n} là số lộc phát Palindrome")
