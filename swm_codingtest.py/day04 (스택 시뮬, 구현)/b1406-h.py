import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

for _ in range(int(input())):
    command = list(input().split())
    if command[0] == 'L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(command[1])
# left.extend(reversed(right)) 
answer = left + right[::-1]
print(''.join(answer))

'''
보통 커서 구현할 때 list.insert(), list.remove(), list.pop()을 구현하기 쉽움. 하지만 리스트이 중간 값을 넣거나 빼는 작업은 O(N)이고 
명령어 개수가 최대 500000개이므로 매번 O(N) 작업을 하면 전체 시간 복잡도는 O(N^2)이 되어 시간 초과하게 됨.

커서를 기준으로 왼쪽과 오른쪽 리스트를 만들고 
커서를 왼쪽으로 움직이는 L은 왼쪽 스택에서 하나 빼서 오른쪽에 넣으면 됨
커서를 오른쪽으로 움직이는건 오른쪽 스택에서 빼서 왼쪽에 넣으면 됨(오른쪽도 스택 형식으로 사용하는 대신 마지막에 reverse 해야됨)

모든 작업이 각 스택의 맨 뒤에서만 일어나기 때문에 각 명령어당 O(1) 시간 복잡도 소요
'''