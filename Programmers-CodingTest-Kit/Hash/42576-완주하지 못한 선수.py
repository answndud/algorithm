'''
hash 문제인 이유: “동명이인을 포함한 이름의 등장 횟수를 빠르게 세야 하기 때문”
여기서 필요한 자료구조가 해시 기반 딕셔너리(hash map)

'''

def solution(participant, completion):
    answer = ''
    
    dic = {}
    
    for key in participant:
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 1
    
    for key in completion:
        dic[key] -= 1
        
    for key in dic:
        if dic[key] >= 1:
            answer = key
            break
    
    return answer


'''
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''

'''
from collections import Counter

def solution(participant, completion):
    result = Counter(participant) - Counter(completion)
    return list(result.keys())[0]
'''