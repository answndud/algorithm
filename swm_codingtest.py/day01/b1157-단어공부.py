import sys
from collections import defaultdict

s = str(sys.stdin.readline().strip()).upper()
dic = defaultdict(int)
for i in s:
    dic[i] += 1
    
max_value = max(dic.values())
max_keys = [k for k, v in dic.items() if v == max_value]
if len(max_keys) >= 2:
    print("?")
else:
    print(max_keys[0])
    
    
'''
max_key = max(data, key=lambda k: data[k])
max_val = data[max_key]
count = list(data.values()).count(max_val)
print("?" if count > 1 else max_key)
'''