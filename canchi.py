can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tị", "Ngọ", "Mùi"]

namAL = int(input("Nhập năm âm lịch: "))
can1 = namAL % 10
chi1 = namAL % 12

print(can[can1] + " " + chi[chi1])