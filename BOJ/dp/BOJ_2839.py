import sys

# [문제 링크]
# https://www.acmicpc.net/problem/2839

# [문제 정보]
# 분류 : BOJ 2839 : 설탕 배달
# 난이도 : 실버 4

# [풀이 방법]
# bottom-up 방식으로 초기 세팅을 한다.
# min을 이용할 때는 dp의 값이 나올 수 없는 큰 수로 세팅한다.
# 6kg부터 돌아서 -3kg, -5kg중 작은 값을 선택하여 봉지 수 +1
# 5001보다 크면 -1 출력

input = sys.stdin.readline

# 내가 푼 더러운 식....
def solution():
    n = int(input())
    dp = [-1] * (n + 1)
    
    dp[3] = 1
    if n >= 5: 
        dp[5] = 1

    for i in range(6, n + 1):
        if dp[i - 3] != -1 and dp[i - 5] != -1:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1
        elif dp[i - 3] == -1 and dp[i - 5] == -1:
            dp[i] = -1
        else:
            if dp[i - 3] == -1:
                dp[i] = dp[i - 5] + 1
            elif dp[i - 5] == -1:
                dp[i] = dp[i - 3] + 1
    
    print(dp[n])
    return

# min을 쓸 경우에는 아주 큰 값을 넣자
def solution_v2():
    n = int(input())
    dp = [5001] * (n + 1)
    
    dp[3] = 1
    if n >= 5: 
        dp[5] = 1

    for i in range(6, n + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    
    print(-1 if dp[n] >= 5001 else dp[n])
    return

if __name__ == "__main__":
    solution_v2()