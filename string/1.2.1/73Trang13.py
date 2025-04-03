def Nhapchuoi():
    S = input("nhập một chuỗi (S):")
    return S

# a
def PhanLoaiChu(S):
    print(S.lower())
    print(S.upper())
    print(S.capitalize())
    print(S.swapcase())
    print(S.title())
    
 


# b.	Cho nhập tiếp 1 ký tự (ch). Đếm xem trong S có bao nhiêu ký tự ch. Yêu cầu thực hiện bằng 2 cách:
def dem(S, ch):
    # Cách 1: Dùng vòng lặp for và if
    count1 = 0
    for i in S:
        if i == ch:
            count1 += 1

    # Cách 2: Dùng phương thức count() của chuỗi
    count2 = S.count(ch)

    return count1, count2

# c Đếm số lượng ký tự và ký số
def dem_ky_tu_va_ky_so(S):
    count_char = 0  # Đếm ký tự
    count_digit = 0  # Đếm ký số
    for i in S:
        if i.isalpha():  # Kiểm tra nếu là chữ cái
            count_char += 1
        elif i.isdigit():  # Kiểm tra nếu là chữ số
            count_digit += 1
    return count_char, count_digit

# d Đếm số lượng ký tự in hoa, ký tự thường, ký số và ký tự khác
def dem_cac_loai_ky_tu(S):
    count_upper = 0  # Chữ in hoa
    count_lower = 0  # Chữ thường
    count_digit = 0  # Chữ số
    count_other = 0  # Ký tự khác (dấu câu, khoảng trắng,...)

    for i in S:
        if i.isupper():
            count_upper += 1
        elif i.islower():
            count_lower += 1
        elif i.isdigit():
            count_digit += 1
        else:
            count_other += 1
    return count_upper, count_lower, count_digit, count_other

# e Đếm nguyên âm và phụ âm
def dem_nguyen_am_phu_am(S):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    count_vowel = sum(1 for i in S if i in vowels)  # Đếm nguyên âm
    count_consonant = sum(1 for i in S if i in consonants)  # Đếm phụ âm

    return count_vowel, count_consonant

# chương trình chhính
S = Nhapchuoi()
# c
char_count, digit_count = dem_ky_tu_va_ky_so(S)
print(f"Số ký tự chữ cái: {char_count}")
print(f"Số ký tự số: {digit_count}")

# d
upper_count, lower_count, digit_count, other_count = dem_cac_loai_ky_tu(S)
print(f"Số ký tự in hoa: {upper_count}")
print(f"Số ký tự thường: {lower_count}")
print(f"Số ký tự số: {digit_count}")
print(f"Số ký tự loại khác: {other_count}")

# e
vowel_count, consonant_count = dem_nguyen_am_phu_am(S)
print(f"Số nguyên âm: {vowel_count}")
print(f"Số phụ âm: {consonant_count}")

ch = input("Nhập ký tự cần đếm trong chuỗi: ")




count1, count2 = dem(S, ch)
print(PhanLoaiChu(S))
print(dem(S))             
