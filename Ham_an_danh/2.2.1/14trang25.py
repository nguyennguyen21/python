solve_linear = lambda a, b: -b / a if a != 0 else ("Vô nghiệm" if b != 0 else "Vô số nghiệm")

# Ví dụ kiểm tra
print(solve_linear(2, 3))  # Kết quả: -1.5
print(solve_linear(0, 3))  # Kết quả: "Vô nghiệm"
print(solve_linear(0, 0))  # Kết quả: "Vô số nghiệm"
