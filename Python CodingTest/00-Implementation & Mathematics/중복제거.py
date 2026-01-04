# li = ["Jeong", "Ihm","Kim", "Ihm", "Jeong", "Jeong"]

'''
apple_1.jpg apple_2.jpg apple_3.jpg computer_1.jpg computer_2.jpg computer_3.jpg computer_4.jpg dog_1 jpg dog_2.jpg penguin_1 jpg penguin_2.jpg penguin_3.jpg
'''
from glob import glob # 파일 탐색기

items = []
for file in glob("*.jpg"):
    name = file.split("_")[0]
    if name not in items:
        items.append(name)
    else:
        continue
print(items)

# set을 사용하면 더 쉽게 중복 제거 가능  


# 몇 번 등장했는지 확인
num_names = {}
for name in glob("*.jpg"):
    name = name.split("_")[0]
    if name not in num_names: # defualtdict로 간소화 가능 from collections import defaultdict
        num_names[name] = 0
    else:
        num_names[name] += 1
print(num_names)