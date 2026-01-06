import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

# [문제 정보]
# 분류 : P 1844 : 게임 맵 최단거리
# 난이도 : LV 2

# [풀이 방법]
# 현재 위치를 큐에 등록
# 현재 위치에서 동,서,남,북을 방문
# 벽이 아니거나 이미 지나온 길이 아니라면
# 방문 등록해주고 큐에 추가
# 마지막 번지를 리턴할 때 만약 1이라면 못갔으므로 -1리턴
# 그게 아니라면 최단거리

from collections import deque

input = sys.stdin.readline

def solution(maps):
    queue = deque([(0, 0)])

    # 동서남북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        # 현재 위치를 꺼낸다
        x, y = queue.popleft()

        # 거기서 동서남북을 가본다.
        for d in range(4):
            # 지도 밖 검사
            if x + dy[d] < 0 or x + dy[d] >= len(maps) or y + dx[d] < 0 or y + dx[d] >= len(maps[0]):
                continue
            # 벽 검사
            if maps[x + dy[d]][y + dx[d]] == 0:
                continue
            if maps[x + dy[d]][y + dx[d]] == 1:
                # 방문 처리
                maps[x + dy[d]][y + dx[d]] = maps[x][y] + 1
                queue.append((x + dy[d], y + dx[d]))
    return maps[-1][-1] if maps[-1][-1] > 1 else -1