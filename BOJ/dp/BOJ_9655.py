import sys

# [문제 링크]
# https://www.acmicpc.net/problem/9655

# [문제 정보]
# 분류 : BOJ 9655 : 돌 게임
# 난이도 : 실버 5

# [풀이 방법]
# 홀수턴은 전자가 무조건 이김
# 짝수턴은 후자가 무조건 이김

input = sys.stdin.readline

def solution():
    n = int(input())

    # dp = [0] * (n + 1)

    # for i in range(1, n + 1):
    #     if i % 2 == 1:
    #         dp[i] = 1
    #     else:
    #         dp[i] = 0
    # print('SK' if dp[n] == 1 else 'CY')

    print('SK' if n % 2 == 1 else 'CY')
    return

# dp 풀이
def solution_dp():
    n = int(input())
    
    # dp[i] = 돌이 i개일 때 최소 턴 횟수
    dp = [0] * 1001 
    
    dp[1] = 1 # 상근 승 (1개 가져감)
    dp[2] = 2 # 창영 승 (1, 1 가져감)
    dp[3] = 1 # 상근 승 (3개 한번에 가져감)
    
    for i in range(4, n + 1):
        # 1개를 가져가거나 3개를 가져간 경우 중 더 짧은 턴 + 1
        dp[i] = min(dp[i-1], dp[i-3]) + 1
        
    if dp[n] % 2 == 1:
        print("SK") # 턴 횟수가 홀수면 먼저 시작한 상근 승
    else:
        print("CY") # 턴 횟수가 짝수면 나중에 시작한 창영 승
    return

if __name__ == "__main__":
    solution()