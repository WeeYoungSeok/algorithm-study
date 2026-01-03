import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/42898

# [문제 정보]
# 분류 : P 42898 : 등굣길
# 난이도 : Level 3

# [풀이 방법]
# dp의 테이블을 이전에서 온 가짓수를 더하면 된다.
# 집에서 출발시에 대각으로는 못가니 아래 오른쪽으로만 갈 수 있다.
# 해당 지점에서 왼쪽, 위쪽에서의 가짓 수를 서로 더 해주면 된다.
# 현재 지점이 웅덩이라면 패스
# 이전 지점이 웅덩이라면 패스

input = sys.stdin.readline

def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    # dp = []

    # for _ in range(n):
    #     dp.append([0] * m)

    for p in puddles:
        dp[p[1] - 1][p[0] - 1] = -1

    dp[0][0] = 1

    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if dp[i][j] == -1:
                continue
            if j - 1 >= 0 and dp[i][j - 1] != -1:
                dp[i][j] += dp[i][j - 1]
            if i - 1 >= 0 and dp[i - 1][j] != -1:
                dp[i][j] += dp[i - 1][j]
    
    return dp[-1][-1] % 1000000007

if __name__ == "__main__":
    solution(4, 3, [[2, 2]])