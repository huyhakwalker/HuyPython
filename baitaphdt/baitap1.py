import math

class diemtoado:
    def __init__(self, x = 0,y = 0):
        self.x = x
        self.y = y
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def printtd(self):
        print("({}; {})".format(self.x, self.y))

n = int(input("Nhập số tọa độ: "))
point_list = []

for i in range (n):
    print("Nhập điểm thứ: {}".format(i+1))
    x = int(input("x = "))
    y = int(input("y = "))
    p = diemtoado(x,y)
    point_list.append(p)


max_d = point_list[0].distance()
max_p = point_list[0]

for p in point_list:
    p.printtd()
    if(p.distance() > max_d):
        max_d = p.distance()
        max_p = p
max_p.printtd()

    