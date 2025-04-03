def NhapSoNuyenDuong():
    n = int(input("nhập số nguyên dương:"))
    while True:
        if n > 0:
            return n
        else:
            print("nhập lại số nguyên dương")
def thuc_hien(n):
    result = []
    for i in range(1,n+1):
        if '5' in str(i):
            result.append(i)
    return result
n = NhapSoNuyenDuong()
result = thuc_hien(n)
print(','.join(map(str,result)))    
            

















