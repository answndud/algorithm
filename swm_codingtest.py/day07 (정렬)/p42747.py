def solution(citations):
    citations.sort(reverse=True)
    for i, c in enumerate(citations):
        if c < i + 1:
            return i
    return len(citations)

"""
citations를 내림차순 정렬하면
i번째 논문은 i+1편 이상 인용됐는지만 확인하면 된다.
c < i+1 이 되는 순간이 H-index의 최대값이다.
"""

# def solution(citations):
#     answer = 0
#     while True:
#         count = 0
        
#         for i in citations:
#             if i >= answer:
#                 count += 1
                
#         if count >= answer:
#             answer += 1
            
#         else:
#             break

#     return answer - 1