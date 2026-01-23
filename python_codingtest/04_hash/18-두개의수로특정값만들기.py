# def solution(arr: list, target: int) -> bool:
#     # arr: [1, 2, 3, 4, 8], target: 6, return: True
    
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             n = i + j
#             if n == target:
#                 return True
#     return False

# print(solution([2,3,5,9], 10))


# 다음은 계수 정렬 알고리즘을 사용해 배열에서 문제에서 요구한 target을 찾는 함수 구현

def count_sort(arr, k):
    hashtable = [0] * (k + 1)
    for num in arr:
        if num <= k:
            hashtable[num] = 1
    return hashtable

def solution(arr, target):
    hashtable = count_sort(arr, target)
    
    for num in arr:
        complement = target - num
        if (
            complement != num
            and complement >= 0
            and complement <= target
            and hashtable[complement] == 1
        ):
            return True
    return False


print(solution([2,3,5,9], 10))