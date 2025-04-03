def Nhapchuoi():
    S = input("Nhập một chuỗi (S): ")
    return S

def BienDoiChuoi(S):
    result = ""
    for i in range(len(S)):
        if i % 2 == 0:  # Vị trí lẻ (chỉ số bắt đầu từ 0)
            result += S[i].lower()
        else:  # Vị trí chẵn
            result += S[i].upper()
    return result

# Chạy chương trình
S = Nhapchuoi()
print("Chuỗi đã biến đổi:", BienDoiChuoi(S))
 