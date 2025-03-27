import math

class PTBac2(object):
    def __init__(self, hesoa, hesob, hesoc):
        self.a = hesoa
        self.b = hesob
        self.c = hesoc
        self.mydict = {'PTbac1': [], 'PTbac2': []}  

    def Tinh_nghiem_PTB1_(self):
        
        if self.a != 0:
            result = -self.b / self.a 
            self.mydict['PTbac1'].append(f"Phương trình có 1 nghiệm duy nhất: x = {result}")
            return result

        if self.a == 0 and self.b == 0:
            self.mydict['PTbac1'].append("Phương trình có vô số nghiệm")
            return None 
        
        if self.a == 0 and self.b != 0:
            self.mydict['PTbac1'].append("Phương trình vô nghiệm")
            return None 

    def Tinh_nghiem_PTB2_(self):
       
        if self.a == 0: 
            return self.Tinh_nghiem_PTB1_()


        D = self.b**2 - 4 * self.a * self.c
        
        if D > 0:
           
            x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            self.mydict['PTbac2'].append(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
            return x1, x2
        elif D == 0:
         
            x = -self.b / (2 * self.a)
            self.mydict['PTbac2'].append(f"Phương trình có 1 nghiệm kép: x = {x}")
            return x
        else:
          
            self.mydict['PTbac2'].append("Phương trình vô nghiệm (có nghiệm phức)")
            return None


pt1 = PTBac2(2, -6, 0)
print(f"Nghiệm PTBac1: {pt1.Tinh_nghiem_PTB1_()}")


pt2 = PTBac2(1, -3, 2)
print(f"Nghiệm PTBac2: {pt2.Tinh_nghiem_PTB2_()}")


print("kết quả  mydict:")
print(pt2.mydict)
