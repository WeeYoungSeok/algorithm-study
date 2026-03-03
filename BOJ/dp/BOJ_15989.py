import sys

# [문제 링크]
# https://www.acmicpc.net/problem/15989

# [문제 정보]
# 분류 : BOJ 15989 : 1, 2, 3 더하기 4
# 난이도 : 골드 5

# [풀이 방법]
# 1, 2, 3을 순차적으로 허용하면서 이전의 조합 결과(DP)를 누적
# 숫자를 고정된 순서로 추가하기 때문에 순서만 다른 중복 조합이 생기지 않음

input = sys.stdin.readline

def solution():
    t = int(input())

    # 1로 만들 수 있는 가지는 1가지이므로 미리 채우기
    dp = [1] * 10001

    for i in range(2, 10001):
        dp[i] = dp[i] + dp[i - 2]

    for i in range(3, 10001):
        dp[i] = dp[i] + dp[i - 3]
    
    for _ in range(t):
        print(dp[int(input())])
    return

if __name__ == "__main__":
    solution()