def solution(operations):
    import heapq
    
    min_heap = []
    max_heap = []
    visited = {}
    idx = 0

    for op in operations:
        command, val = op.split()
        val = int(val)

        if command == "I":
            heapq.heappush(min_heap, (val, idx))
            heapq.heappush(max_heap, (-val, idx))
            visited[idx] = True
            idx += 1

        else:  # "D"
            if val == 1:  # delete max
                while max_heap and not visited.get(max_heap[0][1], False):
                    heapq.heappop(max_heap)

                if max_heap:
                    _, rid = heapq.heappop(max_heap)
                    visited[rid] = False

            elif val == -1:  # delete min
                while min_heap and not visited.get(min_heap[0][1], False):
                    heapq.heappop(min_heap)

                if min_heap:
                    _, rid = heapq.heappop(min_heap)
                    visited[rid] = False

    # clean up
    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)
    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]

    max_val = -max_heap[0][0]
    min_val = min_heap[0][0]
    return [max_val, min_val]

# def solution(operations):
#     arr = []
    
#     for op in operations:
#         cmd, num = op.split()
#         num = int(num)
        
#         if cmd == "I":
#             arr.append(num)
        
#         elif arr:  # 삭제인데 비어있지 않을 때만
#             if num == 1:
#                 arr.remove(max(arr))
#             else:
#                 arr.remove(min(arr))
    
#     return [max(arr), min(arr)] if arr else [0, 0]