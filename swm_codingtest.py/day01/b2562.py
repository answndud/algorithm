import sys

dic = {}
for i in range(9):
    n = int(sys.stdin.readline())
    dic[n] = i + 1
    
    
print(max(dic.keys()), end=" ")
print(dic[max(dic.keys())])