import math
class PhanSo:
    # lưu ý phải truyền vào tham số ở tử  =0 và mẫu = 1 không thì kết quả sẽ sai và trả giá trị là flase và kết thúc chương trình ngay lập tức
    def __init__(phanso,tu_so = 0,mau_so =1):
        phanso.tu = tu_so 
        phanso.mau = mau_so 
    
    def NhapPhanSo(phanso):
        phanso.tu = int(input("nhập tử số :"))
        phanso.mau = int(input("nhập mẫu số :"))
        return phanso.tu,phanso.mau
    def rutgon_phan_so(phanso):
        gcd = math.gcd(phanso.tu,phanso.mau)
        # lấy ước lượng chung của tử và mẫu
        phanso.tu //= gcd
        phanso.mau //= gcd
        print(f"Phân số rút gọn: {phanso.tu}/{phanso.mau}")
        return PhanSo(phanso.tu,phanso.mau)
    def cong(phanso,phan_so_khac):
        tu = phanso.tu * phan_so_khac.mau + phan_so_khac.tu * phanso.mau
        mau = phanso.mau * phan_so_khac.mau
        return PhanSo(tu,mau)
      
    def tru(phanso,phan_so_khac):
        tu = phanso.tu * phan_so_khac.mau - phan_so_khac.tu * phanso.mau
        mau = phanso.mau * phan_so_khac.mau
        return PhanSo(tu,mau)
    def nhan(phanso,phan_so_khac):
        tu = phanso.tu *  phan_so_khac.tu 
        mau = phanso.mau * phan_so_khac.mau
        return PhanSo(tu,mau)
    def __str__(phanso):
        return f"{phanso.tu}/{phanso.mau}"
    
    def HamXuatKetqua(phanso):

        print()
        print(f"{phanso.tu / phanso. mau}")
phanso1 = PhanSo()
phanso1.NhapPhanSo()
phanso2 = PhanSo()
phanso2.NhapPhanSo()
phanso1.rutgon_phan_so()
phanso2.rutgon_phan_so()
sum = phanso1.cong(phanso2)
tru = phanso1.tru(phanso2)
nhan = phanso1.nhan(phanso2)
print(sum)
print(tru)
print(nhan)

