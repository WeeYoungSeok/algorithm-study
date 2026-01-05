import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

# [문제 정보]
# 분류 : P 12909 : 올바른 괄호
# 난이도 : LV 2

# [풀이 방법]
# s를 순회하면서 ( 면 무조건 넣어준다.
# ) 를 만났을 때 스택에서 맨 위에 괄호를 꺼냈을 때
# 비어있거나 ( 가 아니라면 잘못된 괄호다.
# 마지막에 stack이 비어있지 않다면 닫힌 괄호가 남아있으므로 해당 사항도 False다

# 더 나은 풀이
# ( 면 넣어주고
# ) 면 스택이 비어있다면 False
# 비어있지 않다면 무조건 pop을 하고
# 마지막에 stack의 크기로만 True False를 다루면 된다.
input = sys.stdin.readline

def solution(s):
    stack = []

    for p in s:
        if p == "(":
            stack.append(p)
        else:
            # if stack:
            #     if stack.pop() != "(":
            #         answer = False
            #         break
            # else:
            #     answer = False
            #     break
            # 애초에 해당 부분은 ( 인지 검사할 필요가 없음
            # 무조건 ) 가 들어오므로
            # 만약 스택에서 뺄것이 없다면 False다
            # 만약 스택이 안비어있다면 그냥 무조건 꺼낸다
            if not stack:
                return False
            stack.pop()

    # return False if stack else answer
    # 해당 부분도 stack의 크기만 알면 됨
    return len(stack) == 0

if __name__ == "__main__":
    solution("(()(")