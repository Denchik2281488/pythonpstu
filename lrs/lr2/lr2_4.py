class Dot():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def __add__(self,num):
        if isinstance(num,int):
            self.x = self.x +num
            self.y = self.y +num
        elif isinstance(num,Dot):
            self.x = self.x+num.x
            self.y = self.y+num.y

    def __truediv__(self,num):
        self.x = self.x / num
        self.y = self.y / num

    def __mul__(self,num):
        self.x = self.x * num
        self.y = self.y * num
d1 = Dot(45,23)
d2 = Dot(1000,500)
d1*5
print(d1.x, ' ', d1.y)