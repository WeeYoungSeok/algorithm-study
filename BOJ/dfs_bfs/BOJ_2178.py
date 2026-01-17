import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/2178

# [문제 정보]
# 분류 : BOJ 2178 : 미로 탐색
# 난이도 : 실버 1

# [풀이 방법]
# 최단거리 문제이므로 BFS로 접근
# 상하좌우를 검사하여 벽이거나 벽 밖이면 continue
# 갈수있는 곳을 만났다면 왔던 곳에서 + 1
# 도착 보장이 있으므로 마지막 인덱스 출력

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())

    maps = []
    result = 0

    for _ in range(n):
        maps.append(list(map(int, input().strip())))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            result = maps[-1][-1]
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                continue

            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
            
    print(result)
    return

if __name__ == "__main__":
    solution()