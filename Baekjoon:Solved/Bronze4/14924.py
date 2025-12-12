'''
파리가 얼마나 많은 횟수로 왔다 갔다 했는지는 중요하지 않습니다.
중요한 건 "파리가 비행한 시간"입니다.
파리가 비행한 시간 = 두 기차가 부딪힐 때까지 걸린 시간

두 단계만 계산하면 됩니다.
단계 1: 기차가 충돌할 때까지 걸린 시간(Time)구하기 두 기차가 서로를 향해 달려오므로, 
두 기차 사이의 거리는 두 기차 속도의 합만큼 빠르게 줄어듭니다.
time = total distance / sum two train speed = d / 2s

단계 2: 파리의 이동거리: 파리는 위에서 구한 시간 time동안 쉬지 않고 t의 속도로 날았습니다.
f = t * time

문제 대입
s = 50, t = 75, d= 200
time = 2, 즉 두시간 뒤에 기차는 부딪힙니다
f = 75 * 2 = 150마일
'''

s, t, d = map(int, input().split())
collision_time = d / (s * 2)
fly_distance = collision_time * t
print(int(fly_distance))