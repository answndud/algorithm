vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    text = input()
    if text == "#":
        break
    result = 0
    for i in text:
        if i in vowels:
            result += 1
    print(result)