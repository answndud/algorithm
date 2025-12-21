def solution(board, moves):
    # 각 열에 대한 스택 생성
    lanes = [[] for _ in range(len(board[0]))]
    
    # board를 역순으로 탐색하며, 각 열의 인형을 lanes에 추가
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])
                
    # 인형을 담을 bucket 생성
    bucket = []
    
    # 사라진 인형의 총 개수를 저장할 변수
    answer = 0
    
    # moves를 순회하며 각 열에서 인형을 뽑아 bucket에 추가
    for m in moves:
        if lanes[m - 1]: # 해당 열에 인형이 있는 경우
            doll = lanes[m - 1].pop()
            
            if bucket and bucket[-1] == doll:
                bucket.pop()
                answer += 2
            else:
                bucket.append(doll)
    return answer

# board: [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves: [1,5,3,5,1,2,1,4]
# result: 4
'''
1. 매 move마다 "같은 열에서 맨 위를 뽑는다"
2. 맨 위를 계속 뽑는다 → 스택
3. 열마다 독립적으로 동작한다 → 열 단위 구조
4. 그럼 board를 열 스택(lanes)으로 바꾸자
5. pop() 한 번으로 해결

---

이 문제에서 막히는 지점은
“왜 board를 lanes(열 스택)로 바꾸는 생각을 해야 하는가”이다.

1. 문제 문장에서 반드시 멈춰야 할 핵심 표현

* “같은 열에서”
* “가장 위에 있는 인형을 집는다”
* 이 동작을 moves 만큼 반복한다

→ 즉, 같은 열에서 ‘맨 위’를 계속 뽑는다.

2. 여기서 스스로 던져야 할 질문

* 매번 위에서부터 쭉 훑는 게 최선인가?
* 한 번에 빠르게 뽑을 수는 없을까?

3. 문제를 자료구조 언어로 번역

* 같은 열 = 독립적인 구조
* 맨 위만 사용 = LIFO
  → 각 열은 스택이다.

4. 그래서 나오는 핵심 아이디어

* board는 보기용 구조
* 실행은 “열마다 스택”이 편하다
  → board를 열 단위 스택(lanes)으로 변환하자.

5. lanes의 조건

* pop() 한 번이 “맨 위 인형”이어야 한다
* 그러려면 리스트는 [바닥, … , 맨위] 순서여야 한다

6. 왜 아래에서 위로 읽는가

* board는 위가 index 0, 아래가 index n-1
* 바닥 인형을 먼저 append하고
* 위 인형을 나중에 append하면
  → 리스트 끝 = 맨 위 인형
  → pop()이 곧 “집기”가 된다

7. 사고 흐름 한 줄 요약 (시험용)

* “같은 열에서 맨 위를 계속 뽑는다”
  → “열마다 스택”
  → “pop() 한 번으로 처리”
  → “그래서 lanes 전처리”

8. 이 생각이 떠오르면 코드 구조는 자동

* board → lanes 전처리
* moves 순회하며 lanes[m-1].pop()
* bucket 스택으로 연속 제거 처리

이 문제의 핵심은 구현이 아니라
‘문장을 자료구조 행동으로 번역하는 것’이다.
'''