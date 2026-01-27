import sys
input = sys.stdin.readline

array = list(map(str, input().split()))
array_to_int = int(''.join(array))
if array_to_int == 12345678:
    print("ascending")
elif array_to_int == 87654321:
    print("descending")
else:
    print("mixed")
