S='Thành Phố Hồ Chí Minh'

def tach_chuoi(S,c,n):
    deanh_sach_tu = S.split(c)
    if len(deanh_sach_tu) <= n :
        return []
    duyet_tu_ccuoi_den_dau = []
    duyet_tu_ccuoi_den_dau.append(c.join(deanh_sach_tu[-(n+1):]))
    for i in range(n-1, 0, -1):
        duyet_tu_ccuoi_den_dau.insert(0, c.join(deanh_sach_tu[i-1:i+1]))
    
    return duyet_tu_ccuoi_den_dau
    
    
n = int(input('nhập số lượng cần phân tách :'))
c = input('nhập kí tự cần phân tách:')