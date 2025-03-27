class PTBac1(object):
    def __init__(self, a, b):  
        self.a = a
        self.b = b

    def PTB1_vo_nghiem(self):

        if self.a == 0 and self.b != 0:
            return True
        return False  

    def PTB1_co_nghiem(self):

        if self.a != 0:
            print("Phương trình có 1 nghiệm duy nhất")
            return -self.b / self.a


        if self.a == 0 and self.b == 0:
            print("Phương trình có vô số nghiệm")
            return None  

        
        if self.a == 0 and self.b != 0:
            print("Phương trình vô nghiệm")
            return None  



pt = PTBac1(0, 5)


if pt.PTB1_vo_nghiem():
    print("Phương trình vô nghiệm.")


co_nghiem = pt.PTB1_co_nghiem()
if co_nghiem is not None:
    print(f"Giải phương trình là: {co_nghiem}")
