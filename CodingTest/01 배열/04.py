# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3

''' 실패 '''
# def solution(answers):
#     answer = []
    
#     n1 = [1,2,3,4,5]
#     n2 = [2,1,2,3,2,4,2,5]
#     n3 = [3,3,1,1,2,2,4,4,5,5]
    
    
#     dic = {'a' : 0, 'b' : 0, 'c' : 0}
    
#     for i in range(len(answers)):
#         if answers[i] == n1[i]:
#             dic[a] += 1
#         if answers[i] == n2[i]:
#             dic[b] += 1
#         if answers[i] == n3[i]:
#             dic[c] += 1
#     max_grade = max(dic.values())
#     return answer


def solution(answers):
    
    # 수포자들 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 수포자들의 점수를 저장할 리스트
    scores = [0] * 3
    
    # 각 수포자의 패턴과 정답이 얼마나 일치하는지 확인
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]: # 정답패턴의 길이가 답안 길이보다 긴 경우 정답 패턴의 처음데이터와 다시 비교할 수 있도록 나머지 연산자 사용
                scores[j] += 1
    # 가장 높은 점수 저장
    max_score = max(scores)
    
    # 가장 높은 점수를 가진 수포자들의 번호를 찾아서 리스트에 담음
    answer = []
    for i, score in enumerate(scores):
        if score == max_score:
            answer.append(i + 1)
    
    return answer