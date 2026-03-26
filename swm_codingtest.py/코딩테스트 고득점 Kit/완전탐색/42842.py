def solution(brown, yellow):
    for y in range(1, int(yellow ** 0.5) + 1):
        if yellow % y:
            continue
        x = yellow // y
        
        if 2 * x + 2 * y + 4 == brown:
            return [x + 2, y + 2]