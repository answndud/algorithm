a, b = map(int, input().split())
discount = a * b / 100      # 실수로 정확히 계산
final = a - discount

if final >= 100:
    print(0)
else:
    print(1)
    
# 할인액·할인 후 가격 계산할 땐 무조건 실수(/) 써라, // 쓰면 정확도 틀려서 무조건 틀린다.