import sys

# [문제 링크]
# https://www.acmicpc.net/problem/20053

# [문제 정보]
# 분류 : 백준 20053번 : 최소, 최대 2
# 난이도 : 브론즈3

# [풀이 방법]

input = sys.stdin.readline

def solution():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        print(min(nums), max(nums))

if __name__ == "__main__":
    solution()