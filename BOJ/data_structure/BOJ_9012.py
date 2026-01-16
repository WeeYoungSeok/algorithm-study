import sys

# [문제 링크]
# https://www.acmicpc.net/problem/9012

# [문제 정보]
# 분류 : BOJ 9012 : 괄호
# 난이도 : 실버 4

# [풀이 방법]

input = sys.stdin.readline

def solution():
    t = int(input())

    for _ in range(t):
        s = input().strip()
        paren_stack = []

        for paren in s:
            if paren != "(":
                if not paren_stack:
                    paren_stack.append(paren)
                    break
                paren_stack.pop()
            else:
                paren_stack.append(paren)

        print("NO" if paren_stack else "YES")
    return

def solution_clean():
    t = int(input())

    for _ in range(t):
        s = input().strip()
        paren_stack = []
        is_vps = True

        for paren in s:
            # 선 부정보단 선 긍정으로 짜자
            if paren == "(":
                paren_stack.append(paren)
            else:
                if not paren_stack:
                    is_vps = not is_vps
                    break
                paren_stack.pop()

        print("YES" if is_vps and not paren_stack else "NO")
    return

if __name__ == "__main__":
    # solution()
    solution_clean()