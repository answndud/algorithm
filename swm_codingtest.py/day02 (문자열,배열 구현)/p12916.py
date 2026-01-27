def solution(s):
    s = s.lower()
    if 'p' not in s and 'y' not in s:
        return True
    
    array_p = 0
    array_y = 0
    
    for i in s:
        if i == 'p':
            array_p += 1
        if i == 'y':
            array_y += 1
    if array_p == array_y:
        return True
    else:
        return False