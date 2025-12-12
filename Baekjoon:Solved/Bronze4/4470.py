import sys

for i in range(int(sys.stdin.readline())):
    text = sys.stdin.readline().rstrip()
    print(f"{i + 1}. {text}")