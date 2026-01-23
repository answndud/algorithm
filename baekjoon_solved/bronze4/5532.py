l = int(input()) # 방학은 총 L일이다.
a = int(input()) # 국어는 총 A페이지 풀어야 한다.
b = int(input()) # 수학은 총 B페이지 풀어야 한다.
c = int(input()) # 하루에 국어를 최대 C페이지 풀 수 있다. 
d = int(input()) # 하루에 수학을 최대 D페이지 풀 수 있다.

if a % c == 0:
    korean = a // c
else:
    korean = (a // c) + 1
    
if b % d == 0:
    math = b // d
else:
    math = (b // d) + 1
    
print(l - max(korean, math))