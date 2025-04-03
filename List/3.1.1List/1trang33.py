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



# b

