import sys
n, m, k = map(int, sys.stdin.readline().split())

find_n = k // m
find_m = k % m

print(find_n, find_m)