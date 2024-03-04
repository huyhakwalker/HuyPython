dem100 = 0
dem20=0
dem5=0
p = 0
while True:
    n = int(input())
    p = n
    if(n > 0 and n % 5 == 0):
        break

dem100 = n // 100
n = n % 100
dem20 = n //20
n = n % 20
dem5 = n // 5
print("{} tờ 100 + {} tờ 20 + {} tờ 5" .format(dem100, dem20, dem5))
print("====================")
dem=0
for i in range (0, p+1, 100):
    for j in range (0, p+1, 20):
        for k in range (0,p+1, 5):
            if(i+j+k == p):
                dem = dem + 1
                print("{} tờ 100 + {} tờ 20 + {} tờ 5" .format(i//100,j//20,k//5))
print("Có {} cách".format(dem))               