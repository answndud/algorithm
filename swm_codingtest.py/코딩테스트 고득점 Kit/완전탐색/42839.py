from itertools import permutations
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    candidates = set()

    # 모든 길이의 순열 생성
    for k in range(1, len(numbers) + 1):
        for p in permutations(numbers, k):
            num = int("".join(p))
            candidates.add(num)

    # 소수 개수 세기
    return sum(1 for num in candidates if is_prime(num))