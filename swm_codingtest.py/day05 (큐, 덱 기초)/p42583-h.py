from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0
    
    while bridge:
        time += 1
        exited_truck = bridge.popleft()
        current_weight -= exited_truck
        
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                new_truck = truck_weights.popleft()
                bridge.append(new_truck)
                current_weight += new_truck
            else:
                bridge.append(0)
    
    return time


'''
1. 문제 핵심 포인트
- 다리의 길이: 트럭이 다리를 건너는 데 걸리는 시간입니다. 길이가 2라면 트럭이 올라가고 나서 2초 뒤에 완전히 빠져나옵니다.
- 다리의 하중: 현재 다리 위에 올라가 있는 트럭들의 무게 합이 weight를 넘으면 안 됩니다.
- 큐의 역할: 다리를 bridge_length만큼의 길이를 가진 큐로 만듭니다. 트럭이 없는 빈 공간은 0으로 채워줍니다.

2. 생각의 흐름: 시뮬레이션 하기
다리 길이가 2이고 견딜 수 있는 무게가 10인 상황에서 무게가 [7, 4, 5, 6]인 트럭이 온다고 가정해 봅시다.
1) 초기 상태: 다리 큐를 [0, 0]으로 만듭니다. (길이 2)
2) 1초: 다리에서 0 하나가 나가고, 첫 번째 트럭 7이 올라옵니다. → [0, 7] (총 무게 7)
3) 2초: 다리에서 0이 나가고, 다음 트럭 4가 올라오려 합니다. 하지만 7 + 4 > 10이므로 못 올라옵니다. 대신 0을 넣습니다. → [7, 0] (총 무게 7)
4) 3초: 다리에서 7이 드디어 나갑니다. 이제 4가 올라올 수 있습니다. → [0, 4] (총 무게 4)
'''
