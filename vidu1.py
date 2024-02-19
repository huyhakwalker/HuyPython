s = """
Trăm năm trong cõi người ta
Chữ tài chữ mệnh khéo là ghét nhau
Trải qua một cuộc bể dâu
Những điều trông thấy mà đau đớn lòng
Lạ gì bỉ sắc tư phong
Trời xanh quen thói má hồng đánh ghen
"""

words = s.split()
word_count = {}
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
print(word_count)