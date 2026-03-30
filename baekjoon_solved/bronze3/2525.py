# 가장 깔끔한 방법은 전부 분으로 바꿨다가 다시 시/분으로 나누는 것이다.

import sys
input = sys.stdin.readline

h, m = map(int, input().split())
time = int(input())

total = (h * 60) + m + time 
total %= 24 * 60 # 24시간(1440분) 넘어가면 하루 기준으로 순환 (모듈로)

hour = total // 60
minute = total % 60

print(f"{hour} {minute}")