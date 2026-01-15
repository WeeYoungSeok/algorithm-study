import sys

# [문제 링크]
# https://www.acmicpc.net/problem/14501

# [문제 정보]
# 분류 : BOJ 14501 : 퇴사
# 난이도 : 실버 3

# [풀이 방법]
# dp는 해당 일에 일했을때 최대 금액
# dp의 크기는 퇴사일까지 설정 (indexOutOfRange 예방)
# 해당일에 일을 못하면 다음날의 금액 선정
# 해당일에 일을 할 수 있을때
# 해당일을 쉰다면 다음날 금액, 안쉰다면 해당일 금액 + 해당일 상담 걸리는 시간의 금액 중 max

input = sys.stdin.readline

def solution():
    n = int(input())

    dp = [0] * (n + 1)

    counsel = []
    for _ in range(n):
        counsel.append(list(map(int, input().split())))
    
    for i in range(n - 1, -1, -1):
        # 이 날은 일을 못함
        if i + counsel[i][0] > n:
            dp[i] = dp[i + 1]
        else:
            dp[i] = max(dp[i + 1], counsel[i][1] + dp[i + counsel[i][0]])
    print(max(dp))
    return

if __name__ == "__main__":
    solution()