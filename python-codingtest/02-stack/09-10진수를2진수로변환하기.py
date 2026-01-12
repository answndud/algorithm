def solution(d: int):
    stack = []
    while d > 0:
        remainder = d % 2
        stack.append(str(remainder))
        d //= 2
    binary = ""
    while stack:
        binary += stack.pop()
    return binary

'''
+= 연산자는 기존 문자열을 수정하는 것이 아니라, 새로운 문자열 객체를 생성하고 변수가 이 새로운 객체를 참조하도록 재할당

성능 문제: 이 작업이 루프에서 반복될 경우, 매번 새로운 객체를 만들고 복사하는 비용이 발생하므로, 
특히 문자열 길이가 길어질수록 성능이 저하될 수 있습니다. 
(이것이 문자열을 효율적으로 다루기 위해 join()을 사용하는 주요 이유입니다.)
'''


def solution2(d: int) -> str:
    if d == 0:
        return "0"
        
    stack = []
    while d > 0:
        remainder = d % 2
        stack.append(str(remainder))
        d //= 2
        
    #    stack의 요소를 역순으로 꺼내지 않고,
    #    stack에 저장된 상태 그대로 (현재는 역순) join()을 사용하여 연결한 후,
    #    [::-1]로 문자열 자체를 뒤집습니다.
    #    이렇게 하면 pop() 연산을 반복하는 루프가 필요 없어집니다.
    
    # join()으로 stack의 모든 요소를 하나의 문자열로 연결
    # [::-1] 슬라이싱으로 문자열을 뒤집어 정순 2진수로 만듦
    binary = "".join(stack)[::-1] 
    
    return binary