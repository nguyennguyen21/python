s='''Chiều chiều trước bến Văn Lâu
Ai ngồi, ai câu, ai sầu, ai thảm
Ai thương, ai cảm, ai nhớ, ai trông 
Thuyền ai thấp thoáng ven sông
Đưa câu mái vẩy chạnh lòng nước non'''
# a
def dem_ki_tu_phan_biet(s):
    dem_ki_tu_in_hoa = 0
    dem_ki_tu_in_thuong = 0
    for ki_tu in s:
        if ki_tu.islower():
            dem_ki_tu_in_thuong += 1
        if ki_tu.isupper():
            dem_ki_tu_in_hoa += 1
    return dem_ki_tu_in_hoa , dem_ki_tu_in_thuong
dem_ki_tu_in_hoa , dem_ki_tu_in_thuong = dem_ki_tu_phan_biet(s)
#b
def dem_ki_tu(s):
    dem = 0
    for ki_tu in s:
        if ki_tu.isalpha():
             dem += 1
        return dem 
print(f'kí tự in hoa :{dem_ki_tu_in_hoa}')
print(f'kí tự in thường :{dem_ki_tu_in_thuong}')
print(dem_ki_tu(s))