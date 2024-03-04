from my_lib.snt import snt
from my_lib.snt import psnt
from my_lib.snt import fsnt
while True:
    n = int(input("Nhập n: "))
    if(n>0 and n<=1000):
        break
print("\n==========================\n")    
print(f"{n} là số nguyên tố" if snt(n) else f"{n} không là số nguyên tố")
print("\n==========================\n")
psnt(n)
print("\n==========================\n")
fsnt(n+1)