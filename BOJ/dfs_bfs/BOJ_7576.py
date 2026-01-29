import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/7576

# [문제 정보]
# 분류 : BOJ 7576 : 토마토
# 난이도 : 골드 5

# [풀이 방법]
# 토마토가 있는 위치를 미리 전부 찾아 좌표를 저장
# 찾은 좌표를 큐에 넣어서 동시 출발 시작
# 토마토 리스트에서 0이 존재한다면 -1 출력
# 0이 없다면 토마토 리스트에서 max - 1 출력

input = sys.stdin.readline

def bfs(start_x_y, tomato):
    queue = deque()
    for s in start_x_y:
        queue.append((s[0], s[1]))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        nx, ny = queue.popleft()

        for k in range(4):
            cx = nx + dx[k]
            cy = ny + dy[k]

            if cx < 0 or cx >= len(tomato) or cy < 0 or cy >= len(tomato[0]):
                continue
            if tomato[cx][cy] == -1:
                continue

            if tomato[cx][cy] == 0:
                tomato[cx][cy] = tomato[nx][ny] + 1
                queue.append((cx, cy))
            
    return

def solution():
    m, n = map(int, input().split())

    tomato = []

    start_x_y = []

    for _ in range(n):
        tomato.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                start_x_y.append([i, j])
    
    bfs(start_x_y, tomato)
    
    if 0 in (s_num for row in tomato for s_num in row):
        print(-1)
    else:
        print(max(map(max, tomato)) - 1)
    return

if __name__ == "__main__":
    solution()