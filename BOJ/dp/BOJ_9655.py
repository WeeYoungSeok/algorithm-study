import sys

# [문제 링크]
# https://www.acmicpc.net/problem/9655

# [문제 정보]
# 분류 : BOJ 9655 : 돌 게임
# 난이도 : 실버 5

# [풀이 방법]
# 1. (수학적 접근) 1개 또는 3개(홀수)만 가져갈 수 있으므로, 턴이 지날 때마다 홀/짝 상태가 바뀜.
#    - N이 홀수면 상근(SK) 승리, 짝수면 창영(CY) 승리
# 2. (DP 접근) dp[i] = i개의 돌을 다 가져가는 데 걸리는 최소 턴 수
#    - 점화식: dp[i] = min(dp[i-1], dp[i-3]) + 1

input = sys.stdin.readline

def solution():
    n = int(input())
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
    # solution_dp() # DP 버전
    solution()