# def to_nbase(num, n):
#     chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     mod_digit = {i : chars[i] for i in range(len(chars))}
#     s = ""
#     while num != 0:
#         s = mod_digit[num % n] + s
#         num //= n
#     return s

def to_nbase(num: int, n: int) -> str:
    # num이 0인 경우 특별 처리 (원래 코드는 "" 빈 문자열을 반환하므로 '0'으로 수정)
    if num == 0:
        return '0'
    
    # 0~9와 A~Z까지의 문자들을 모아놓은 문자열 (진법 표현에 사용할 문자들)
    # 인덱스 0~35에 해당하는 문자를 바로 꺼내 쓸 수 있음
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    s = "" # 변환 결과를 저장할 문자열 (초기값은 빈 문자열)

    while num != 0:
        # 현재 num을 n으로 나눈 나머지를 구함 (가장 낮은 자리 숫자)
        # chars[나머지]로 해당하는 문자를 가져옴 (예: 나머지 10 -> 'A')
        # 결과를 문자열의 앞에 붙여서 높은 자리부터 쌓아감
        s = chars[num % n] + s
        
        # num을 n으로 나눈 몫으로 업데이트 (다음 자리 계산을 위해)
        num //= n
    return s

if __name__ == "__main__":
    test_cases = [
        (0, 10),     # '0'
        (10, 2),     # '1010'
        (255, 16),   # 'FF'
        (123, 8),    # '173'
        (35, 36),    # 'Z'
        (1000000, 5) # '11000000' (5진법)
    ]
    
    for num, base in test_cases:
        print(f"{num}(10) → {base}진법: {to_nbase(num, base)}")
        
        
'''
파이썬 내장 제공 라이브러리
16진법: hex()
8진법: oct()
2진법: bin()
'''