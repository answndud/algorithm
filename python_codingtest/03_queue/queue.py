# queue = []

# queue.append(1)
# queue.append(2)
# queue.append(3)

# first_item = queue.pop(0)
# print(first_item)

# queue.append(4)
# queue.append(5)

# first_item = queue.pop(0)
# print(first_item)

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

first_item = queue.popleft()
print(first_item)

queue.append(4)
queue.append(5)

first_item = queue.popleft()
print(first_item)


'''
list보다 deque를 사용하는게 성능이 훨씬 우수하다.

'''