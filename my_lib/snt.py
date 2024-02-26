def snt(n):
    dem = 0
    for i in range (1, n+1):
        if(n%i==0):
            dem+=1
    if(dem==2):
        return True
    else:
        return False
def psnt(n):
    for i in range (2,n+1):
        if(snt(i)):
            print(i, end=" ")