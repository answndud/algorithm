def solution(clothes):
    dic = {}
    
    # 종류별 개수를 직접 기록
    for name, kind in clothes:
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1

    # 각 종류별 (개수 + 1) 을 모두 곱해준다
    answer = 1
    for cnt in dic.values():
        answer *= (cnt + 1)

    # 아무것도 안 입는 경우(전부 선택 안 함) 제거
    return answer - 1