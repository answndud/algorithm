def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0, 0, 0]
    
    for i, a in enumerate(answers):
        for idx, p in enumerate(patterns):
            if a == p[i % len(p)]:
                scores[idx] += 1
    max_score = max(scores)
    return [i + 1 for i, s in enumerate(scores) if s == max_score]
            

# dfsdflsdfsd
'''
1.	각 수포자의 패턴을 정의
2.	answers와 비교하여 정답 개수 계산
3.	최대 정답 개수를 가진 사람 찾기
4.	동점 처리

단순 문자열/리스트 비교 문제이며
문제 크기가 작아 O(N) 완전 탐색으로 충분

i % len(pattern)으로 순환 패턴을 구현
'''