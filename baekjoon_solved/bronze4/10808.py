# dic = {
#     'a' : 0,
#     'b' : 0,
#     'c' : 0,
#     'd' : 0,
#     'e' : 0,
#     'f' : 0,
#     'g' : 0,
#     'h' : 0,
#     'i' : 0,
#     'j' : 0,
#     'k' : 0,
#     'l' : 0,
#     'm' : 0,
#     'n' : 0,
#     'o' : 0,
#     'p' : 0,
#     'q' : 0,
#     'r' : 0,
#     's' : 0,
#     't' : 0,
#     'u' : 0,
#     'v' : 0,
#     'w' : 0,
#     'x' : 0,
#     'y' : 0,
#     'z' : 0
# }

# s = str(input())
# for i in s:
#     p = int(dic[i])
#     dic[i] = p + 1
# print(*dic.values())

# 아스키 코드 사용
inputString = input()
countArray = [0] * 26
for str in inputString:
  countArray[ord(str) - 97] += 1
print(*countArray)

# count 사용
# inputString = input()
# countArray = [0] * 26
# for str in inputString:
#   countArray[ord(str) - 97] = inputString.count(str)
# print(*countArray)