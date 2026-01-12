stack = []
max_size = 10

def isFull(stack):
    return len(stack) == max_size

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    if isFull(stack):
        print("stack is full")
    else:
        stack.append(item)
        print("data has been pushed")
        
def pop(stack):
    if isEmpty(stack):
        print("stack is empty")
        return None
    else:
        stack.pop()
        
# 파이썬의 리스트는 크기를 동적관리하기 때문에 isFull, isEmpty는 필요없다