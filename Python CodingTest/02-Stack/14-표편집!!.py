def solution(n, k, cmd):
    # 1. 삭제된 행들의 정보를 순서대로 저장할 스택 (복구 'Z' 명령을 위해 사용)
    deleted = []
    
    # 2. 양방향 연결 리스트를 배열로 구현
    # up[i]는 i번 행의 '바로 위' 살아있는 행 번호 저장
    # down[i]는 i번 행의 '바로 아래' 살아있는 행 번호 저장
    # n+2, n+1 크기로 설정하여 가장자리(첫 행/끝 행) 예외 처리를 위한 더미 공간 확보
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    
    # 3. 인덱스 매칭을 위해 현재 위치 k를 1 증가 (1~n 범위를 실제 데이터로 사용)
    # 0번과 n+1번은 리스트의 시작과 끝을 나타내는 '더미(Sentinel) 노드' 역할
    k += 1
    
    # 4. 주어진 명령어 배열을 순차적으로 순회
    for cmd_i in cmd:
        # 5. 'C' (현재 선택된 행 삭제) 처리
        if cmd_i.startswith("C"):
            deleted.append(k) # 나중에 복구하기 위해 현재 번호를 스택에 저장
            
            # 연결 끊기: 위쪽 행의 '아래'를 나의 아래로, 아래쪽 행의 '위'를 나의 위로 연결
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            
            # 삭제 후 커서 이동: 만약 현재가 마지막 행이면 위로, 아니면 아래 행 선택
            # n < down[k]는 현재 행이 마지막 행임을 의미 (더미 노드인 n+1에 도달했을 때)
            k = up[k] if n < down[k] else down[k]
    
        # 6. 'Z' (가장 최근에 삭제된 행 복원) 처리
        elif cmd_i.startswith("Z"):
            restore = deleted.pop() # 스택에서 가장 최근 삭제 데이터를 꺼냄
            
            # 연결 복구: 내 위쪽 행의 '아래'를 다시 나로, 내 아래쪽 행의 '위'를 다시 나로 설정
            # 이 작업이 가능한 이유는 삭제 시 up/down 배열의 해당 인덱스 값은 그대로 남아있기 때문
            down[up[restore]] = restore
            up[down[restore]] = restore
            
        # 7. 'U X' 또는 'D X' (커서 이동) 처리
        else:
            action, num = cmd_i.split()
            if action == "U":
                # 위로 X칸 이동: 연결 리스트를 타고 up 방향으로 이동
                for _ in range(int(num)):
                    k = up[k]
            else:
                # 아래로 X칸 이동: 연결 리스트를 타고 down 방향으로 이동
                for _ in range(int(num)):
                    k = down[k]

    # 8. 최종 결과 생성: 초기 상태 'O'에서 삭제된 인덱스만 'X'로 변경
    answer = ["O"] * n
    for i in deleted:
        # 1-based 인덱스를 다시 0-based로 보정
        answer[i - 1] = "X"

    return "".join(answer)

'''
solution2가 뛰어난 이유
- 가독성: up, down 리스트 두 개를 관리하는 대신 하나의 딕셔너리에 [prev, next]를 묶어 관리하므로 구조가 명확합니다.
- 유연성: 복구 시 (prev, node, nxt) 정보를 통째로 스택에 넣기 때문에 주변 노드를 찾는 연산이 더 단순해집니다. 
  메모리 deleted 리스트에 인덱스만 담는 대신 튜플을 담아도 파이썬의 동적 메모리 관리 덕분에 효율적으로 동작합니다.
'''

def solution2(n, k, cmd):
    # 각 노드의 [이전, 다음] 노드 번호를 저장하는 딕셔너리
    # 더미 노드 없이 0 ~ n-1 범위만 깔끔하게 사용
    linked_list = {i: [i - 1, i + 1] for i in range(n)}
    # 첫 행의 이전은 -1, 마지막 행의 다음은 -1로 설정 (경계 처리)
    linked_list[0][0] = -1
    linked_list[n - 1][1] = -1
    
    stack = []
    curr = k
    
    for c in cmd:
        if c == 'C':
            prev, nxt = linked_list[curr]
            stack.append((prev, curr, nxt)) # 복구를 위해 주변 정보 함께 저장
            
            if nxt == -1: # 마지막 행 삭제 시
                curr = prev
            else:
                curr = nxt
            
            # 연결 끊기
            if prev != -1: linked_list[prev][1] = nxt
            if nxt != -1: linked_list[nxt][0] = prev
                
        elif c == 'Z':
            prev, node, nxt = stack.pop()
            # 복구 시 주변 노드들에게 다시 연결
            if prev != -1: linked_list[prev][1] = node
            if nxt != -1: linked_list[nxt][0] = node
            
        else:
            action, val = c.split()
            val = int(val)
            # 0번(이전), 1번(다음) 인덱스를 이용해 빠르게 이동
            move_idx = 0 if action == 'U' else 1
            for _ in range(val):
                curr = linked_list[curr][move_idx]

    # 결과 문자열 조립
    result = ['O'] * n
    for _, node, _ in stack:
        result[node] = 'X'
        
    return "".join(result)