DP = {0: 0, 1: 1}
def solution(n):
    if n in DP: return DP[n]
    else:
        DP[n] = solution(n - 1) + solution(n - 2)
        return DP[n]

'''
위 방법의 함정은 함수는 중첩으로 call할 때 부를 수 있는 횟수가 정해져 있음
RecursionError가 테스트케이스에서 뜰 수 있음

코드를 돌릴 때 메모리는 힙과 스택을 사용하는데
일반적으로 함수는 call될 때 스택 메모리를 사용함(크기는 작지만 빠르게 접근 가능)
스택 메모리 영역을 쓰는 함수는 많이 중첩해서 부르면 메모리 해제를 하지 못하고
계속 메모리 영역을 차지하게 돼서 에러가 남

오류없이 정석으로 풀기 위해 DP에 재귀함수를 쓰지 않고 써야함
'''
def solution2(n):
    DP = [0, 1]
    if n == 0 or n == 1: return DP[n] # 피보나치 수열의 맨 처음 두 자리를 넣고
    else:
        for i in range(2, n + 1): # 피보나치 수열을 리스트에 계속 쌓다가 n번째가 됐을 때
            DP.append(DP[-1] + DP[-2]) # 리스트의 마지막 item을 return
        return DP[-1]