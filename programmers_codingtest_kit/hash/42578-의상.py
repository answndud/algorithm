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
    for i in dic.values():
        answer *= (i + 1)

    # 아무것도 안 입는 경우(전부 선택 안 함) 제거
    return answer - 1

'''
1) 경우의 수 공식 각 종류마다 선택지는 (입기 + 안 입기) 즉 (옷 개수 + 1) 모든 종류에 대해 이를 곱하면 전체 조합 수가 된다.
2) 하지만 문제 조건은 “최소 한 개 이상의 옷은 입어야 함” 따라서 전부 안 입는 1가지 경우를 빼야 한다. 
3) 라이브러리 없이 딕셔너리로 카운팅 직접 딕셔너리로 카운팅하면 불필요한 import 없이 해결 가능하다.
'''