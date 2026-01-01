import sys

# [문제 링크]
# https://www.acmicpc.net/problem/21918

# [문제 정보]
# 분류 : 백준 21918번 : 전구
# 난이도 : 브론즈2

# [풀이 방법]
# if문으로 명령어를 제어하여 리스트를 변경

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    for _ in range(m):
        a, b, c = map(int, input().split())
        
        if a == 1:
            s[b - 1] = c
        elif a == 2:
            for x in range(b - 1, c):
                s[x] = 1 - s[x]
        elif a == 3:
            for x in range(b - 1, c):
                s[x] = 0
        else:
            for x in range(b - 1, c):
                s[x] = 1

    print(" ".join(map(str, s)))
    return

if __name__ == "__main__":
    solution()