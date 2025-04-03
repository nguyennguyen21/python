# a. Chuỗi S có bắt đầu bằng ký tự ‘P’ (in hoa) hay không?
starts_with_P_1 = lambda S: S[0] == 'P' if S else False
starts_with_P_2 = lambda S: S.startswith('P')
starts_with_P_3 = lambda S: S.find('P') == 0

# b. Chuỗi S có bắt đầu bằng ký tự ‘P’ hoặc ‘p’ hay không?
starts_with_Pp_1 = lambda S: S[0] in 'Pp' if S else False
starts_with_Pp_2 = lambda S: S.startswith(('P', 'p'))
starts_with_Pp_3 = lambda S: S.find('P') == 0 or S.find('p') == 0

# c. Chuỗi S có bắt đầu bằng một nguyên âm hay không?
is_vowel = lambda c: c.lower() in 'aeiou'

# Cách 1: Chỉ sử dụng lệnh if
starts_with_vowel_1 = lambda S: S[0].lower() in 'aeiou' if S else False

# Cách 2: Sử dụng hàm đã có
starts_with_vowel_2 = lambda S: is_vowel(S[0]) if S else False

# d. Chuỗi S có phải là chuỗi palindrome hay không?
is_palindrome = lambda S: S == S[::-1]

# Nhập chuỗi từ người dùng
S = input("Nhập chuỗi S: ")

# Kiểm tra và in kết quả
print(f"Chuỗi bắt đầu bằng 'P' (cách 1): {starts_with_P_1(S)}")
print(f"Chuỗi bắt đầu bằng 'P' (cách 2): {starts_with_P_2(S)}")
print(f"Chuỗi bắt đầu bằng 'P' (cách 3): {starts_with_P_3(S)}")

print(f"Chuỗi bắt đầu bằng 'P' hoặc 'p' (cách 1): {starts_with_Pp_1(S)}")
print(f"Chuỗi bắt đầu bằng 'P' hoặc 'p' (cách 2): {starts_with_Pp_2(S)}")
print(f"Chuỗi bắt đầu bằng 'P' hoặc 'p' (cách 3): {starts_with_Pp_3(S)}")

print(f"Chuỗi bắt đầu bằng nguyên âm (cách 1): {starts_with_vowel_1(S)}")
print(f"Chuỗi bắt đầu bằng nguyên âm (cách 2): {starts_with_vowel_2(S)}")

print(f"Chuỗi là palindrome: {is_palindrome(S)}")
