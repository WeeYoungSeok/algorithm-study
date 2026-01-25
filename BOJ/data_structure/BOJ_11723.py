import sys
from collections import defaultdict

# [문제 링크]
# https://www.acmicpc.net/problem/11723

# [문제 정보]
# 분류 : BOJ 11723 : 집합
# 난이도 : 실버5

# [풀이 방법]
# 문제 조건에 맞게 dict로 조건문을 이용해 품

input = sys.stdin.readline

def solution():
    s = {}

    m = int(input())

    for _ in range(m):
        cal = list(input().strip().split())

        if "add" in cal:
            if int(cal[1]) not in s:
                s[int(cal[1])] = 1
        elif "remove" in cal:
            if int(cal[1]) in s:
                del s[int(cal[1])]
        elif "check" in cal:
            if int(cal[1]) in s:
                print(1)
            else:
                print(0)
        elif "toggle" in cal:
            if int(cal[1]) in s:
                del s[int(cal[1])]
            else:
                s[int(cal[1])] = 1
        elif "all" in cal:
            for i in range(1, 21):
                s[i] = 1
        else:
            s = {}
            
    return

if __name__ == "__main__":
    solution()