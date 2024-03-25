import datetime


class Xe:
    def __init__(self, bienso, hangsanxuat, namsanxuat = None, namluuhanh = 20):
        self.bien_so = bienso
        self.hang_san_xuat = hangsanxuat
        if namsanxuat is None:
            self.nam_san_xuat = datetime.datetime.now().year
        else:
            self.nam_san_xuat = namsanxuat
        self.nam_luu_hanh = namluuhanh
    @property
    def bienso(self):
        return self.bien_so
    @bienso.setter
    def bienso(self, value):
        if len(value) == 9 and value[:2].isdigit() and self.giatribienso(value):
            self.bien_so = value
        else:
            raise ValueError("Biển số xe không hợp lệ!")
    def giatribienso(self, bienso):
        return bienso[:2].isdigit()
    @property
    def nam_san_xuat(self):
        return self.nam_san_xuat
    
    @nam_san_xuat.setter
    def nam_san_xuat(self, value):
        namhientai = datetime.datetime.now().year
        if value > 1980 and value <= namhientai:
            self.namsanxuat = value
        else:
            raise ValueError("Năm sản xuất không hợp lệ!")
    def input(self):
        self.bienso = input("Nhập biển số xe: ")
        self.hangsanxuat = input("Nhập hãng sản xuất: ")
        self.namsanxuat = int(input("Nhập năm sản xuất: "))
    def output(self):
        print("Thông tin xe:")
        print(f"Biển số: {self.bienso}")
        print(f"Hãng sản xuất: {self.hangsanxuat}")
        print(f"Năm sản xuất: {self.namsanxuat}")
        print(f"Số năm lưu hành: {self.tinhsonamluuhanh()} năm")
        print("\n")
    def tinhsonamluuhanh(self):
        namhientai = datetime.datetime.now().year
        return namhientai - self.namsanxuat
    
dsxe = []
while True:
    n = int(input("Nhập số lượng xe: "))
    if(n>0):
        break
for i in range(n):
    print(f"Nhập thông tin cho xe thứ {i + 1}:")
    xe = Xe("", "")
    xe.input()
    dsxe.append(xe)
    print("\n")

print("\n=====================================\n")

max_namluuhanh = max(xe.tinhsonamluuhanh() for xe in dsxe)
print("\nThông tin xe có thời gian lưu hành dài nhất:")
for xe in dsxe:
    if xe.tinhsonamluuhanh() == max_namluuhanh:
        xe.output()

print("\n=====================================\n")

dsxe = [xe for xe in dsxe if not xe.bienso.startswith("79")]
print("\nDanh sách xe sau khi xóa các xe có biển số bắt đầu bằng '79':")
for xe in dsxe:
    xe.output()