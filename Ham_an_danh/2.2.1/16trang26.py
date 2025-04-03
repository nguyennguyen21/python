import math

# a. Tổng S = 1 + 2 + ... + n
sum_n = lambda n: sum(range(1, n + 1))

# b. Tổng S = 1/2 + 1/3 + ... + 1/(n+1)
sum_fraction = lambda n: sum(1 / i for i in range(2, n + 2))

# c. Tích P = 1 × 3 × 5 × ... × (2n - 1)
product_odd = lambda n: math.prod(range(1, 2 * n, 2))

# d. Tổng S = 1/2 + 3/4 + 5/6 + ... + (2n+1)/(2n+2)
sum_fraction_odd = lambda n: sum((2 * i + 1) / (2 * i + 2) for i in range(n))

# e. S = 1 - 1/(1+2) + 1/(1+2+3) - ... + (-1)^(n+1) / (1+2+...+n)
sum_alternating_fraction = lambda n: sum((-1) ** (i + 1) / sum(range(1, i + 1)) for i in range(1, n + 1))

# f. Tổng S = 1² + 2² + 3² + ... + n²
sum_squares = lambda n: sum(i * i for i in range(1, n + 1))

# f'. Tổng S = 1*2 + 2*3 + 3*4 + ... + n(n+1)
sum_product = lambda n: sum(i * (i + 1) for i in range(1, n + 1))

# g. S = -x² + x⁴ - ... + (-1)^n * x^(2n)
sum_power_alternating = lambda n, x: sum((-1) ** i * x ** (2 * i) for i in range(1, n + 1))

# h. S = x/1+2 + x²/(1+2+3) + ... + xⁿ/(1+2+...+n)
sum_x_fraction = lambda n, x: sum((x ** i) / sum(range(1, i + 1)) for i in range(1, n + 1))
