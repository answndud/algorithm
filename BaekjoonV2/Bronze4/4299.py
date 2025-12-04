import sys

s, d = map(int, sys.stdin.readline().split())

# 합(S)이 차(D)보다 크거나 같아야 한다. (S >= D, 즉 점수가 음수가 되지 않도록)
# (합 + 차)가 짝수여야 한다. (S+D) % 2 == 0, 즉 각 점수가 정수여야 한다.
if s >= d and (s + d) % 2 == 0:
    # 파이썬에서 나눗셈 결과가 정수임을 확신할 수 있을 때 // 연산자를 사용합니다.
    score_a = (s + d) // 2
    score_b = (s - d) // 2
    
    # 문제 분석에서 score_A가 항상 score_B보다 크거나 같도록 계산했기 때문에, 
    # score_A를 먼저 출력
    print(score_a, score_b)
else:
    print(-1)
    
    
'''
합(Sum): a + b = s
차(Difference): a - b = d

a구하기: (a + b) + (a - b) = s + d, 2a = s + d, a = (s + d) / 2
b구하기: (a + b) - (a - b) = s - d, 2b = s - d, b = (s - d) / 2

s와 d는 음이 아닌 정수, s + d는 항상 0 이상. 즉, a는 항상 0 이상.
a, b가 정수이려면 s + d, s - d가 모두 짝수여야 함
'''