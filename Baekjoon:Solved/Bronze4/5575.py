for i in range(3):
    array = list(map(int, input().split()))
    start = (array[0] * 3600) + (array[1] * 60) + (array[2])
    finish = (array[3] * 3600) + (array[4] * 60) + (array[5])
    total = finish - start
    print((total // 3600), (total % 3600 // 60), (total % 3600 % 60))