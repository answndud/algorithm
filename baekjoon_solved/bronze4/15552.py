import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
    
# 입력받는게 int가 아니라 str인 경우 rstrip() 사용
# for i in range(sys.stdin.readline().rstrip()):