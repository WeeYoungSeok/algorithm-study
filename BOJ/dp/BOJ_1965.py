import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1965

# [문제 정보]
# 분류 : BOJ 1965 : 상자넣기
# 난이도 : 실버 2

# [풀이 방법]

input = sys.stdin.readline

def solution():
    n = int(input())

    box = list(map(int, input().split()))
    dp = [1] * n

    for i in range(n):
        for j in range(i -1, -1, -1):
            if box[i] > box[j]:
                dp[i] = max(dp[j] + 1, dp[i])
     
    print(max(dp))
    return

if __name__ == "__main__":
    solution()