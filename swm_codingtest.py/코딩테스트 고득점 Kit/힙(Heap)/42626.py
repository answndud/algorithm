import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while True:
        if scoville[0] >= K:
            return count
        if len(scoville) < 2:
            return -1
        
        least = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new_scoville = least + (second * 2)
        heapq.heappush(scoville, new_scoville)
        count += 1