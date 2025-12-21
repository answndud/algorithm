'''
1. 각 시점 i에 대해 **“처음으로 가격이 떨어지는 시점”**을 찾는 문제다.
2. i마다 뒤를 보면 O(N²) → 아직 안 떨어진 인덱스만 스택에 보관한다.
3. 새 가격이 들어올 때, 스택 top 가격보다 작으면 그 인덱스는 지금 떨어진 것 → pop하며 시간 계산.
4. while을 써도 각 인덱스는 push 1번, pop 1번이라 전체는 O(N).
5. 끝까지 남은 인덱스들은 마지막까지 버틴 시간(n − 1 − i) 로 처리한다.
'''


def solution(prices):
    n = len(prices)
    answer = [0] * n # 가격이 떨어지지 않은 기간을 저장할 배열
    
    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            # 가격이 떨어졌으므로 이전 가격의 기간 계산
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    # 스택에 남아있는 가격들은 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    return answer

'''
i 이후의 시점들을 보면서
prices[i]보다 작은 값이 처음 나오는 시점 j를 찾는다. 그러면 답은 j - i
끝까지 그런 값이 없으면, 답은 마지막 인덱스 - i (끝까지 버틴 시간)

각 i가 떨어지는 순간을 미리 찾으려 하지 말고,
새 가격을 보면서 이 새 가격 때문에 떨어지는 과거 인덱스들을 처리

즉, 현재 가격 p가 들어오면:
이전에 봤던 가격들 중 아직 안 떨어진 것들(미해결)을 가지고 있다가
현재 가격 p가 더 작으면 그 이전 가격들은 “지금에서야 떨어졌음”이 확정됩니다.

스택에는 인덱스를 넣습니다. 의미는:
stack 안의 인덱스들은 “아직 가격이 떨어진 적이 없는 시점들”이다.
즉, 답을 아직 못 정한 후보들입니다.

## 핵심 규칙 (while이 왜 필요한가)
현재 시점 i, 현재 가격 p를 봤을 때:
스택 top 인덱스 j의 가격이 prices[j]
만약 prices[j] > p 라면?
그러면 j는 i에서 처음으로 떨어진 것입니다.
왜 “처음”이냐면, j가 스택에 남아 있었다는 건 지금까지는 한 번도 떨어진 적이 없다는 뜻이기 때문입니다.

그래서:
answer[j] = i - j
그리고 j는 이제 해결됐으니 스택에서 제거(pop)
그런데 이게 top 하나만이 아닐 수 있습니다.
현재 p가 충분히 작으면 스택 위에 쌓인 여러 인덱스의 가격보다 작을 수 있으니, 떨어지는 애들 다 처리할 때까지 반복해야 해서 while입니다.

왜 O(N)인가 (진짜 중요한 부분)
겉으로 보면 while이 있어서 느려 보이지만, 핵심은:
각 인덱스는 스택에 딱 1번 들어감(push)
각 인덱스는 스택에서 딱 1번 나옴(pop)
즉, while이 여러 번 돌아도 전체 pop 횟수는 최대 N번입니다.
전체 연산이: push N번 pop N번 → 합쳐서 O(N)
'''
def solution2(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] # 아직 값이 떨어지지 않은 인덱스들
    
    for i, p in enumerate(prices):
        # 현재 가격이 더 낮아지면, 스택에 있던 과거 시점들이 "지금" 떨어진 것이 확정
        while stack and prices[stack[-1]] > p:
            j = stack.pop() # 현재 가격보다 큰 값의 인덱스 값
            answer[j] = i - j
        stack.append(i)
    
    # 끝까지 안떨어진 애들은 마지막까지 버틴 시간으로 answer 채우기
    while stack:
        j = stack.pop()
        answer[j] = n - j - 1

    return answer