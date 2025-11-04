# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    # 스테이지별 도전자 수를 구함
    chanllenger = [0] * (N + 2)
    for stage in stages:
        chanllenger[stage] += 1
        
    # 스테이지별 실패한 사용자 수 계산
    fails = {}
    total = len(stages)
    
    # 각 스테이지를 순회하며, 실패율 계산
    for i in range(1, N + 1):
        if chanllenger[i] == 0: # 도전한 사람 없으면 실패율 0
            fails[i] = 0
        else:
            fails[i] = chanllenger[i] / total # 실패율
            total -= chanllenger[i] # 도전자 수 줄이기
    
    # 실패율 높은 스테이지부터 내림차순 정렬 (딕셔너리의 value 기준으로 정렬)
    answer = sorted(fails, key=lambda x: fails[x], reverse=True)
    
    return answer

'''
리스트의 크리를 N + 2로 정한 이유:
N번째 스테이지를 클리어한 사용자는 stage가 N+1. 그러면 challenger 배열에서 N+1 위치에 데이터를 저장해야 하는데
배열의 인덱스는 0부터 시작하므로 N+1 인덱스에 데이터를 저장하려면 N+2 크기의 배열이 필요
0번째 인덱스를 사용하지 않지만 실보다 득이 큼. 값 자체를 인덱스로 활용할 수 있기 때문

시간 복잡도:
N은 스테이지의 개수, M은 stages의 길이. challenger 배열을 초기화하고, 
각 스테이지 도전자 수를 계산할 때 시간 복잡도는 O(N + M)
스테이지 별로 실패율을 계산할 때 O(N)
실패율 기준으로 스테이지 정렬할 때 O(NlogN)
모두 고려하면 O(2*N + M + NlogN) => O(M + NlogN)
'''