import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/1012

# [문제 정보]
# 분류 : BOJ 1012 : 유기농 배추
# 난이도 : 실버 2

# [풀이 방법]
# 배추를 만나면 BFS, DFS로 상하좌우를 모두 검사하여
# 배추를 방문 처리 해줌
# 그때 흰지렁이 1마리 증가시켜줌
# 배추가 끊기면 다음 배추를 찾아 똑같이 진행

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(land, i, j):
    if i < 0 or i >= len(land) or j < 0 or j >= len(land[0]):
        return False
        
    if land[i][j] == 1:
        land[i][j] = 0
        dfs(land, i, j + 1)
        dfs(land, i, j - 1)
        dfs(land, i + 1, j)
        dfs(land, i - 1, j)
        return True

    return False

def solution():

    t = int(input())

    for _ in range(t):
        m, n, k = map(int, input().split())
        land = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(k):
            y, x = map(int, input().split())
            land[x][y] = 1
        worm = 0
            
        for i in range(n):
            for j in range(m):
                if dfs(land, i, j):
                    worm += 1
        print(worm)
    return


def bfs(land, x, y, n, m):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    land[x][y] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < m and land[nx][ny] == 1:
                land[nx][ny] = 0
                queue.append((nx, ny))

def solution_bfs():

    t = int(input())

    for _ in range(t):
        m, n, k = map(int, input().split())
        land = [[0 for _ in range(m)] for _ in range(n)]
        for _ in range(k):
            y, x = map(int, input().split())
            land[x][y] = 1
        worm = 0
            
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    bfs(land, i, j, n, m)
                    worm += 1
        print(worm)
    return

if __name__ == "__main__":
    # solution()
    solution_bfs()