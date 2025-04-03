def Nhapchuoi():
    S = input('nhập 1 chuỗi:')
    return S

def kiemtrachuoi(S):
   for do_ki_tu in range(len(S)):
       if S[do_ki_tu] == S[len(S)-do_ki_tu-1]:
              return True
   return False
def kiemtrachuoidoixung_join(S):
    reversed_S = ''.join(reversed(S))
    return S == reversed_S
def is_palindrome(S):
    s = s.lower().replace(" ", "")
    reversed_s = s[::-1]
    if s == reversed_s:
        return True
    else:
        return False
# Hàm kiểm tra chuỗi đối xứng
def is_palindrome(s):
    # Chuẩn hóa chuỗi: chuyển thành chữ thường và loại bỏ khoảng trắng
    s = s.lower().replace(" ", "")
    
    # Đảo từng ký tự trong chuỗi để tạo chuỗi Y
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s  # Thêm ký tự vào đầu chuỗi đảo
    
    # Kiểm tra nếu chuỗi ban đầu và chuỗi đảo ngược là giống nhau
    if s == reversed_s:
        return True
    else:
        return False

# Nhập chuỗi từ người dùng
input_str = input("Nhập một chuỗi: ")

# Kiểm tra chuỗi có đối xứng hay không
if is_palindrome(input_str):
    print("Chuỗi đối xứng (palindrome).")
else:
    print("Chuỗi không đối xứng.")

S = Nhapchuoi()

if kiemtrachuoi(S) :
    print('chuỗi đối xứng')
else:
    print("không phải chuỗi đối xứng")

if kiemtrachuoidoixung_join(S):
    print('chuỗi đối xứng')
else:
    print("không phải chuỗi đối xứng")