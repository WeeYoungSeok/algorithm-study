import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/1189

# [문제 정보]
# 분류 : BOJ 1189 : 컴백홈
# 난이도 : 실버 1

# [풀이 방법]


input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, dist, r, c, k, maps, check):
    if x == 0 and y == c -1:
        return 1 if dist == k else 0
    
    count = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 범위 넘어가면 안됨
        if nx >= 0 and nx < r and ny >= 0 and ny < c and maps[nx][ny] != -1 and not check[nx][ny]:
            check[nx][ny] = True
            count += dfs(nx, ny, dist + 1, r, c, k, maps, check)
            check[nx][ny] = False

    return count

def solution():
    r, c, k = map(int, input().split())

    maps = [[0 for _ in range(c)] for _ in range(r)]
    check = [[False for _ in range(c)] for _ in range(r)]

    for i in range(r):
        row = input().strip()
        for j in range(len(row)):
            if row[j] == "T":
                maps[i][j] = -1
    
    # 출발지점 방문처리
    check[r -1][0] = True
    print(dfs(r-1, 0, 1, r, c, k, maps, check))
    return

if __name__ == "__main__":
    solution()