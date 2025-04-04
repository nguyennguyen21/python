datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1),
[5, 12], {"class": 'V', "section": 'A'} , {3.14, 9, "python"}]
# a
# cách 1 sử dụng type(object)
print(type(datalist[0]))
print(type(datalist[1]))
print(type(datalist[2]))
print(type(datalist[3]))
print(type(datalist[4]))
print(type(datalist[5]))
print(type(datalist[6]))
print(type(datalist[7]))
print(type(datalist[8]))
# cách 2
Bool_int = isinstance(datalist[0],int)
print(Bool_int)
Bool_float = isinstance(datalist[1],float)
print(Bool_float)
Bool_complex = isinstance(datalist[2],complex)
print(Bool_complex)
Bool_boolen= isinstance(datalist[3],bool)
print(Bool_boolen)
Bool_str = isinstance(datalist[4],str)
print(Bool_str)
Bool_tuple = isinstance(datalist[5],tuple)
print(Bool_tuple)
Bool_list = isinstance(datalist[6],list)
print(Bool_list)
Bool_dictionary = isinstance(datalist[7],dict)
print(Bool_dictionary)
Bool_set = isinstance(datalist[8],set)
print(Bool_set)


# b
def check_List_type(List):
    for item in List:
        # dùng đ63 lấy dữ liệu các kiểu dữ liệu
        match item.__class__.__name__: 
            case 'int':
                print(f'{item} có kiểu int')
            case 'float':
                print(f'{item} có kiểu float')
            case 'complex':
                print(f'{item} có kiểu complex')
            case 'bool':
                print(f'{item} có kiểu bool')
            case 'list':
                print(f'{item} có kiểu list')
            case 'dict':
                print(f'{item} có kiểu dict')
            case 'str':
                print(f'{item} có kiểu str')
            case 'tuple':
                print(f'{item} có kiểu tuple')
            case 'set':
                print(f'{item} có kiểu set')
check_List_type(datalist)
#c
def sum_numeric_elements(lst):
    total = 0
    for item in lst:
        match item.__class__.__name__:
            case 'int' | 'float':  # Nếu là int hoặc float thì cộng vào tổng
                total += item
            case 'complex' | 'bool' | 'list' | 'tuple' | 'dict' | 'str' | 'set':
                pass  # Không cộng các kiểu này
            case _:
                print(f"{item}: Unknown")  # Nếu gặp kiểu lạ thì in ra Unknown
    return total

# Danh sách mẫu để kiểm tra
data = [100, 3.14, "Python", [1, 2, 3], (4, 5), {"key": "value"}, False, None, 50, 2.5]

# Gọi hàm tính tổng
result = sum_numeric_elements(data)

# In kết quả
print(f"Tổng các số int và float trong danh sách: {result}")
