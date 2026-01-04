def nbase_to_dec(s: str, n: int) -> int:
    """
    n진법 문자열 s를 10진법 정수로 변환합니다.
    
    Parameters:
        s (str): n진법으로 표현된 숫자 문자열 (예: 'FF', '1010')
        n (int): 진법 (2 ≤ n ≤ 36)
    
    Returns:
        int: 10진법 정수
    
    예시:
        nbase_to_dec('FF', 16)  -> 255
        nbase_to_dec('1010', 2) -> 10
        nbase_to_dec('Z', 36)   -> 35
    """
    # 진법에 사용할 문자 매핑 (인덱스 → 값)
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit_value = {char: idx for idx, char in enumerate(chars)}
    
    # 입력 문자열이 빈 문자열이거나 진법 범위 오류 체크
    if not s:
        return 0
    
    if n < 2 or n > 36:
        raise ValueError("진법 n은 2 이상 36 이하만 지원합니다.")
    
    result = 0
    for char in s.upper():  # 대소문자 구분 없게 .upper() 처리
        if char not in digit_value:
            raise ValueError(f"유효하지 않은 문자 '{char}'가 포함되어 있습니다. (진법 {n}에 맞지 않음)")
        value = digit_value[char]
        if value >= n:  # 해당 진법에서 사용할 수 없는 숫자/문자인지 체크
            raise ValueError(f"'{char}'는 {n}진법에서 사용할 수 없는 문자입니다.")
        
        # result = result * n + 현재 자리 값
        result = result * n + value
    
    return result


def nbase_to_dec2(num, n):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mod_dict = {chars[i] : i for i in range(len(chars))}
    digits = []
    for i, c in enumerate(num[::-1]):
        digits.append(mod_dict[c] * n ** i)
    print(digits)
    return sum(digits)


def nbase_to_dec3(num, n):
    print(int("num", n)) # n은 현재 진수

# 테스트 코드
if __name__ == "__main__":
    test_cases = [
        ('0', 10),      # 0
        ('1010', 2),    # 10
        ('FF', 16),     # 255
        ('173', 8),     # 123
        ('Z', 36),      # 35
        ('ff', 16),     # 255 (소문자도 허용)
    ]
    
    for num_str, base in test_cases:
        print(f"{num_str} ({base}진법) → {nbase_to_dec(num_str, base)}")