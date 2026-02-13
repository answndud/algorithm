def solution(sizes):
    max_length = []
    min_length = []
    answer = 0
    
    for i in sizes:
        max_length.append(max(i))
        min_length.append(min(i))
    
    return (max(max_length) * max(min_length))