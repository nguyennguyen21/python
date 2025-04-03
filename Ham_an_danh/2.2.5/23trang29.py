fibonacci = lambda n: (lambda fib: [fib.append(fib[-1] + fib[-2]) for _ in range(n-1)] and fib[n])( [0, 1] )

n = int(input("Nhập số nguyên dương n: "))
print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")
