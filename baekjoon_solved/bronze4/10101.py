'''
세 각의 크기가 모두 60이면, Equilateral
세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
세 각의 합이 180이 아닌 경우에는 Error

총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.
문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.
'''
a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
  print("Error")
elif a == b == c:
  print("Equilateral")
elif a == b or a == c or b == c:
  print("Isosceles")
else:
  print("Scalene")