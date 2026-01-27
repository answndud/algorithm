'''
idea
- 1부터 N중에 하나를 선택한 뒤
- 다음 1 ~ N 선택할 때 이미 선택한 값이 아닌 경우만
- M개를 선택할 경우 프린트
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
check = [False] * (N + 1)

def recur(num):
    if num == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N + 1):
        if check[i] == False:
            check[i] = True
            result.append(i)
            recur(num + 1)
            check[i] = False
            result.pop()

recur(0)