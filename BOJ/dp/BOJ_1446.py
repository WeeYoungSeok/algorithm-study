import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1446

# [문제 정보]
# 분류 : BOJ 1446 : 지름길
# 난이도 : 실버 1

# [풀이 방법]
# 0km부터 고속도로 끝(D)까지 1km씩 전진하며 DP 테이블을 채움
# 기본적으로 현재 위치의 최소 거리는 '이전 칸의 거리 + 1'
# 만약 현재 위치에서 시작하는 지름길이 있다면 지름길 도착지의 DP 값을 비교하여 최솟값으로 갱신

input = sys.stdin.readline

def solution():
    n, d = map(int, input().split())

    shortcut = []
    dp = [x for x in range(d + 1)]

    for _ in range(n):
        shortcut.append(list(map(int, input().split())))
    
    for i in range(d + 1):
        if i > 0:
            dp[i] = min(dp[i], dp[i - 1] + 1)
        for j in range(n):
            if shortcut[j][0] == i:
                if shortcut[j][1] > d:
                    continue
                dp[shortcut[j][1]] = min(dp[shortcut[j][1]], dp[i] + shortcut[j][2])

    print(dp[-1])
    return

if __name__ == "__main__":
    solution()