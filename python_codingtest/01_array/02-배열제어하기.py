def solution(arr):
    return sorted(list(set(arr), reverse=True))

print(solution([4,2,5]))