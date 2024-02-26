from my_lib.snt import snt
from my_lib.snt import psnt
while True:
    n = int(input("Nhập n: "))
    if(n>0 and n<=1000):
        break
print("==========================")    
print(f"{n} là số nguyên tố" if snt(n) else f"{n} không là số nguyên tố")
print("==========================")
psnt(n)
