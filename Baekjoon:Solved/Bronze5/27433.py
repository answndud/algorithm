import math
print(math.factorial(int(input())))

## Using an Iterative Approach (Loop)
n = int(input())
# def factorial_iterative(n):
#     # if n < 0:
#     #     raise ValueError("Factorial is not defined for negative numbers")
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(factorial_iterative(n))
        
## Using a Recursive Approach
# n = int(input())
# def factorial_recursive(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers")
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial_recursive(n - 1)
# print(factorial_recursive(n))