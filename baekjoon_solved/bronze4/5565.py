total_price = int(input())

price_stack = 0
for _ in range(9):
    price = int(input())
    price_stack += price
    
print(total_price - price_stack)