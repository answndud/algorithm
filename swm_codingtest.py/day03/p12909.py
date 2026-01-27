def solution(s):    
    arr = []
    
    for i in s:
        if i == '(':
            arr.append(i)
        else:
            if not arr:
                return False
            arr.pop()

    return len(arr) == 0