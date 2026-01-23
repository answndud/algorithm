current_h, current_m, current_s = map(int, input().split())
cooking_time = int(input())

# 현재 시각을 모두 '초' 단위로 변환
total_seconds = (current_h * 3600) + (current_m * 60) + current_s

finish_total_seconds = total_seconds + cooking_time

# % 24를 하는 이유: 24시가 넘어가면 0시부터 다시 시작해야 하므로 (예: 25시 -> 1시)
finish_h = (finish_total_seconds // 3600) % 24
finish_m = (finish_total_seconds % 3600) // 60
finish_s = finish_total_seconds % 60

print(finish_h, finish_m, finish_s)