n, a, b = map(int, input().split())
if a == b:
    print("Anything")
elif a < b:
    print("Bus")
else:
    print("Subway")
    
# 전제조건에서 n이 b보다 작으니 n은 신경쓸 필요가 없음