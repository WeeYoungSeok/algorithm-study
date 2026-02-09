import sys

# [문제 링크]
# https://www.acmicpc.net/problem/17484

# [문제 정보]
# 분류 : BOJ 17474 : 진우의 달 여행 (Small)
# 난이도 : 실버 3

# [풀이 방법]
# 1. 3차원 DP 배열 생성: dp[행][열][이전방향] (방향: 0=왼쪽대각선, 1=수직, 2=오른쪽대각선)
# 2. 첫 번째 줄(0행)은 이전 방향 제한이 없으므로, 해당 위치의 연료값으로 초기화
# 3. 두 번째 줄부터 점화식 적용:
#    - 현재 칸으로 올 수 있는 '이전 위치'들의 값 중, '같은 방향'이 아닌 것들의 최솟값을 더함
#    - 예: 수직(1)으로 오려면, 이전 행의 왼쪽(0) 또는 오른쪽(2) 방향 값 중 작은 것을 선택
# 4. 마지막 행의 모든 값 중 최솟값을 출력

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    oil = []

    for _ in range(n):
        oil.append(list(map(int, input().split())))

    dp = [[[sys.maxsize] * 3 for _ in range(m)] for _ in range(n)]

    for j in range(m):
        dp[0][j][0] = oil[0][j]
        dp[0][j][1] = oil[0][j]
        dp[0][j][2] = oil[0][j]

    for i in range(1, n):
        for j in range(m):
            
            if j > 0:
                dp[i][j][0] = oil[i][j] + min(dp[i-1][j-1][1], dp[i-1][j-1][2])
            
            dp[i][j][1] = oil[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])
            
            if j < m - 1:
                dp[i][j][2] = oil[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1])

    min_val = sys.maxsize
    for j in range(m):
        min_val = min(min_val, min(dp[n-1][j]))
        
    print(min_val)

if __name__ == "__main__":
    solution()