def solution(s):
    answer = 0
    n = len(s)
    for i in range(n):
        stack = []
        for j in range(n):
            # 괄호문자열을 회전시키면서 참조
            c = s[(i + j) % n]
            if c == "(" or c == "[" or c == "{": # 열린 괄호 푸시
                stack.append(c)
            else:
                if not stack: # 짝이 맞지 않는 경우
                    break
                # 닫힌 괄호는 스택의 top과 짝이 맞는지 비교
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    break
        else: # for문이 break에 의해 끝나지 않고 끝까지 수행된 경우
            if not stack:
                answer += 1
    return answer

def solution2(s):
    count = 0
    for i in range(len(s)):
        stack = []
        for j in s:
            if not stack:
                stack.append(j)
                continue
            if stack[-1] == "[" and j == "]":
                stack.pop()
            elif stack[-1] == "{" and j == "}":
                stack.pop()
            elif stack[-1] == "(" and j == ")":
                stack.pop()
            else:
                if j in (']', '}', ')'): # ex) stack 맨 위에는 (가 있는데, j로 ]가 들어온 경우. 
                    break 
                stack.append(j)
        s = s[1:] + s[0]
        if not stack:
            count += 1
    return count

'''
스택을 활용한 괄호 문제는 로직을 통째로 외우기보다 **'스택의 본질'**만 기억하면 내일이 아니라 한 달 뒤에도 풀 수 있습니다.

---

### ## 괄호 문제 해결의 3원칙 (The Stack Rule)

1. **여는 괄호:** 나중에 짝을 만나야 하니 일단 **스택에 넣는다.**
2. **닫는 괄호:** 스택 맨 위(top)를 보고 **짝이 맞으면 빼고(pop), 안 맞으면 즉시 끝낸다(break).**
3. **마무리:** 모든 검사가 끝났을 때 **스택이 깨끗하게 비어 있어야 정답**이다.

---

### ## 코드로 기억하는 '흐름도'

머릿속에 아래 시나리오만 그려보세요.

* **스택이 비었나?** → 일단 넣고 다음으로 (`continue`)
* **짝이 맞는가?**
* `(` 와 `)` 만나면? → **팡! 사라짐 (`pop`)**
* `[` 와 `]` 만나면? → **팡! 사라짐 (`pop`)**


* **둘 다 아닌데(else) 닫는 괄호(`]`, `}`, `)`)가 왔나?** * → "가망 없음, 탈출!" (`break`)
* **그 외 상황(여는 괄호가 또 들어옴)인가?**
* → "다음에 짝 찾자, 일단 쌓아!" (`append`)



---

### ## 한 눈에 보는 체크리스트 (복습용)

| 상황 | 동작 | 이유 |
| --- | --- | --- |
| **비어있는 스택** | `append` | 비교할 대상이 없음 |
| **짝이 맞음** | `pop` | 완벽한 쌍을 이루어 제거됨 |
| **닫는 괄호인데 짝 안 맞음** | **`break`** | **이미 틀린 문자열 (핵심!)** |
| **여는 괄호 들어옴** | `append` | 짝을 기다리는 대기열에 추가 |

---

### ## 팁: 왜 `if not stack`으로 끝내나요?

문자열이 `(((` 처럼 여는 괄호만 잔뜩 있어도 `break`에 걸리지 않고 `for`문이 끝납니다. 하지만 이 경우 스택에는 `['(', '(', '(']`가 남아있겠죠? 그래서 마지막에 **"스택이 비었니?"**라고 물어보는 것이 최종 관문이 됩니다.

이 로직은 괄호 문제뿐만 아니라 **'짝 맞추기'** 성격의 모든 알고리즘 문제에 똑같이 적용됩니다.

내일 다시 보셨을 때 이 **'팡! 사라지는 짝 맞추기'** 이미지만 떠올려 보세요. 바로 코딩하실 수 있을 거예요! 더 궁금한 점이 생기면 언제든 물어봐 주세요.
'''
