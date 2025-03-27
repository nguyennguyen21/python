class contructor(object):
    def __init__(self,lenght,width):
        self.l = lenght
        self.w = width
    def rectangle_area(self):
        return self.l * self.w
    def rectangle_perimeter(self):
        return (self.l +self.w)*2
hcn = contructor(5,10)

# yêu cầu
# a
print (hcn.__dict__)
# b
# 
print(f"diện tích hình chữ nhật :{hcn.rectangle_area()}")
print(f"chu vi hình chữ nhật :{hcn.rectangle_perimeter()}")
# 
print(contructor.__name__)
print(hcn.rectangle_area.__name__)
print(hcn.rectangle_perimeter.__name__)
# hiển thị giá trị class đang có 
print (hcn.__dict__)

