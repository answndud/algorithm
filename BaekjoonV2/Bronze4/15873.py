x = input()

if len(x) == 2:
    print(sum(map(int, [x[0], x[1]])))
elif len(x) == 4:
    print(20)
else:
    if int(x[-1]) == 0:		#문자열의 맨 마지막이 0, 즉 B가 10이다
        print(int(x[0]) + 10)
    else:			#중간이 0, 즉 A가 10이다
        print(int(x[-1]) + 10)