a = int(input()) # meat temp
b = int(input()) # goal temp
c = int(input()) # 얼어 있는 고기를 1℃ 데우는 데 걸리는 시간 C
d = int(input()) # 얼어 있는 고기를 해동하는 데 걸리는 시간 D
e = int(input()) # 얼어 있지 않은 고기를 1℃ 데우는 데 걸리는 시간 E

if a < 0:
    print((abs(a) * c) + d + (b * e))
else:
    print((b - a) * e)