import sys

# [문제 링크]
# https://www.acmicpc.net/problem/16171

# [문제 정보]
# 분류 : BOJ 16171 : 나는 친구가 적다 (Small)
# 난이도 : 브론즈 2

# [풀이 방법]
# s 문자열에서 숫자를 제거
# k가 s에 포함된다면 1 아니라면 0

input = sys.stdin.readline

def solution():
    s = input().strip()
    k = input().strip()

    s = ''.join(char for char in s if not char.isnumeric())

    if k in s:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    solution()