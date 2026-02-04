def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse=True)
    return str(int(''.join(numbers)))


'''
Q. 왜 x*3 인가?
A. numbers는 최대 1000 이하 → 최대 3자리 수, 3번 반복하면 비교 기준이 길어져서 문제 요구 정렬 기준과 일치함

Q: str(int(''.join(numbers))) 왜 join()한걸 다시 int로 그리고 다시 str로 캐스팅하는거야?
A: 결과가 "0000" 같은 형태가 되는 걸 막기 위해서입니다
'''