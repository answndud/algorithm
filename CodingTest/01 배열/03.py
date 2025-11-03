# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    # 두 수를 선택하는 모든 겨웅의 수를 반복문으로 구함
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # 두 수를 더한 결과를 새로운 배열에 추가
            answer.append(numbers[i] + numbers[j])
    # 중복된 값 제거, 오름차순 정렬
    answer = sorted(set(answer))
    return answer