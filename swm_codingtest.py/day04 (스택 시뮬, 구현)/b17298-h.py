import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and array[stack[-1]] < array[i]:
        answer[stack.pop()] = array[i]
    stack.append(i)
print(*answer)
    
    
'''
1. stack에는 현재 원소를 담고 인접한 두원소끼리만 비교한다.
2. 인접한 두 원소 중 오른 쪽이 클때 stack을 pop하여 answer를 업데이트한다.
3. 그 이후에 stack의 가장위에 있는 값이 현재 오른쪽 값보다 작은 지 확인하고, 작다면 pop 한다.

3번은 stack이 비거나 왼쪽의 값이 더 큰 값을 가질때 까지 반복한다.

stack에 들어가는건 슷자의 위치(인덱스). 그래야 나중에 anwer[index]에 답을 적을 수 있음


예시: [3, 5, 2, 7]
1. i=0 (숫자 3): 대기실에 3의 위치(0)를 넣습니다. stack = [0]

2. i=1 (숫자 5):
    대기실 맨 위 array[0](3)보다 5가 큽니다!

    3의 오큰수는 5입니다. answer[0] = 5 하고 3은 대기실에서 나갑니다(pop).

    이제 5의 위치(1)가 대기실에 들어갑니다. stack = [1]

3. i=2 (숫자 2):
    대기실 맨 위 array[1](5)보다 2가 작습니다.

    2는 5를 구출 못 합니다. 2의 위치(2)도 대기실로 들어갑니다. stack = [1, 2]

4. i=3 (숫자 7):
    대기실 맨 위 array[2](2)보다 7이 큽니다! answer[2] = 7, pop.

    그다음 대기자 array[1](5)보다도 7이 큽니다! answer[1] = 7, pop.

    7의 위치(3)가 대기실에 들어갑니다. stack = [3]
    
    
이중 반복문(for 안에 while)이라 느려 보일 수 있지만, 매우 빠름
모든 인덱스는 스택에 정확히 한 번 들어가고(push), 한 번 나옵니다(pop).
따라서 전체 연산 횟수는 대략 $2N$번에 불과하며, 시간 복잡도는 O(N)이 됩니다.
만약 단순하게 for문 두 개로 오른쪽을 매번 다 뒤졌다면 O(N^2)이 되어 시간 초과가 났을 거예요.
'''