import math


class cCircle:
    def __init__(self,r):
        self.radius = r
    def circle_area(self):
        area = (self.radius**2) * math.pi
        return area
    def circle_perimeter(self):
        peri = self.radius*2 * math.pi
        return peri

rad = float(input('Nhap vao ban kinh duong tron : '))
ht = cCircle(rad)
print(f'Dien tich hinh tron la : {ht.circle_area()}')
print(f'Dien tich hinh tron la : {ht.circle_perimeter()}')