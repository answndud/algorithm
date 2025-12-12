s, k, h = map(int, input().split())
if s + k + h >= 100:
    print("OK")
else:
    dic = {s : "Soongsil", k : "Korea", h : "Hanyang"}
    print(dic[min(s, k, h)])