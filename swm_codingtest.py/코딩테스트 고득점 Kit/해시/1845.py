def solution(nums):
    nums_set = set(nums)
    limit_num = len(nums) // 2
    
    if len(nums_set) >= limit_num:
        return limit_num
    else:
        return len(nums_set)