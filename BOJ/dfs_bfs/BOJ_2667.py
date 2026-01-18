import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/2667

# [문제 정보]
# 분류 : BOJ 2667 : 단지번호붙이기
# 난이도 : 실버 1

# [풀이 방법]
# `bfs`를 이용하여 품
# 집을 만나면 상하좌우를 검사하여 집을 방문처리
# 방문 처리를 하면서 집의 개수 += 1
# 하나의 단지가 끝나면 단지도 += 1
# 집의 개수를 리스트에 담아 마지막에 sort처리

input = sys.stdin.readline

def bfs(x, y, n, m, maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    maps[x][y] = 0
    queue = deque()
    queue.append((x, y))
    count = 1

    while queue:
        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny))
                count += 1 
    return count

def solution():
    n = int(input())

    maps = []

    for _ in range(n):
        maps.append(list(map(int, input().strip())))
    
    building = 0
    home_num = []

    for i in range(n):
        for j in range(len(maps[0])):
            if maps[i][j] == 1:
                home_num.append(bfs(i, j, n, len(maps[0]), maps))
                building += 1
    
    print(building)
    home_num.sort()
    for home in home_num:
        print(home)
    return

if __name__ == "__main__":
    solution()