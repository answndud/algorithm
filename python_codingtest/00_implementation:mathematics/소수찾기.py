def is_prime(num):
    if num == 1: return False
    for i in range(2, num):
        if num % i == 0: return False
    return True

def is_prime2(num):
    if num == 1: return False
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0: return False
    return True


print(is_prime(13))
print(is_prime2(13))