p = int(input())

if(p==0):
    print("27000")
if(p<=200):
    a = p
    a = a*120
    if(a<27000):
        print(27000)
elif(p<=400):
    b = p-200
    b = b * 80 + 200 * 120
    if(b>27000):
        print(b)
    else:
        print(27000)
elif(p<=43200):
    c = p-400
    c = c * 40 + 200 * 80 + 200* 120
    print(c)