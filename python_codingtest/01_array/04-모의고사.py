def solution(answers: list):
    patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
        
    scores = [0, 0, 0]
    
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    max_score = max(scores)
    # highest_scores = []
    # for i, score in enumerate(scores):
    #     if score == max_score:
    #         highest_scores.append(i + 1)
            
    highest_scores = [i + 1 for i, score in enumerate(scores) if score == max_score]
            
    return highest_scores


'''
- 하드코딩하는걸 지양해야 하지만 케이스가 적으면 ㄱㅊ
- 수포자들이 얻은 점수의 최댓값을 먼저 구하고 이 점수와 일치하는 수포자의 번호를 오름차순으로 반환하면 동점 조건을 해결할 수 있다
- 정답 패턴의 길이가 수포자의 답안 길이보다 긴 경우 계속 비교할 수 있도록 나머지 연산자 사용
- 시간복잡도는 O(N) 중첩루프여도 각자 루프 도는게 다르다
'''