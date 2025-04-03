def Nhapchuoi():
    S = input("Nhập một chuỗi (S): ")
    return S
# a
def Dao_chu(S):
    if len(S) > 4 : 
        return S[::-1]
    else:
        return S
# b
def ki_tu_thuong_va_hoa(S):
    chu_hoa = sum(1 for c in S if c.isupper())
    chu_thuong = sum(1 for c in S if c.islower())
    if chu_hoa >=chu_thuong  :
       return S.lower()
    else:
      return  S.upper()
        
        
S = Nhapchuoi()
print(Dao_chu(S))

print(ki_tu_thuong_va_hoa(S))
