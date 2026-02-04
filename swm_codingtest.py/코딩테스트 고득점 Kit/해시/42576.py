def solution(participant, completion):
    dic = {}
    for k in participant:
        if k in dic:
            dic[k] += 1
        else:
            dic[k] = 1
    
    for k in completion:
        dic[k] = 1
    
    for k in dic:
        if dic[k] >= 1:
            return k