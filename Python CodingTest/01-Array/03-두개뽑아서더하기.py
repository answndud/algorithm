def solution(numbers: list):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result.append(numbers[i] + numbers[j])
    return sorted(set(result))
print(solution([2, 1, 3, 4, 1]))