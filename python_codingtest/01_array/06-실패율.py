'''
실패율을 구하는 코드 작성
실패율: 스테이지에 도달했으나 클리어하지 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
전체 스테이지 수: N
게임을 이용하는 사용자가 멈춰있는 스테이비 번호가 담긴 배열: stages
실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열 반환해라

'''
def solution(N: int, stages: list): # n: 5, stages: [2,1,2,6,2,4,3,3]
    # 스테이지별 도전자 수를 구함
    challenger = [0] * (N + 2)
    for stage in stages:
        challenger[stage] += 1
        
    # 스테이지별 실패한 사용자 수 계산
    fails = { }
    total = len(stages)
    
    # 각 스테이지를 순회하며, 실패율 계산
    for i in range(1, N + 1):
        if challenger[i] == 0: # 도전한 사람이 없는 경우, 실패율 0
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total # 실패율
            total -= challenger[i] # 다음 스테이지 실패율 구하기 위해 현재 스테이지 인원 뺌
    
    # 실패율이 높은 스테이지부터 내림차순으로 정렬
    result = sorted(fails, key= lambda x : fails[x], reverse=True)
    return result
            
'''
challenger 리스트의 크기를 N + 2로 정한 이유?
N번째 스테이지를 클리어한 사용자는 stage가 N + 1, 그러면 challenger 배열에서 N + 1 위치에 데이터를 저장해야 하는데 배열의 인덱스는 0부터 시작한다. 
값 자체를 인덱스로 활용할 수 있어서 더 편리하다

그리고 challengers값을 활용해서 실패율을 구한다.
해당 스테이지에 있는 사용자가 0이면 실패율은 0이 되므로 간단하다.

사용자가 있다면 실패율 로직을 통해 구하고 total을 사용자 수만큼 줄인다.

** sorted()를 사용하면 Dictionary도 List 형식으로 바뀐다. **

스테이지별로 실패율 계산할 때는 O(N)
람다식으로 정렬할 때 O(NlogN)
즉, O(M + NlogN)
'''