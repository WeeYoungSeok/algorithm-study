import sys
import heapq
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/13549

# [문제 정보]
# 분류 : BOJ 13549 : 숨바꼭질 3
# 난이도 : 골드 5

# [풀이 방법]
# 가중치가 0인 순간이동은 deque의 왼쪽에, 가중치가 1인 이동은 오른쪽에 넣음
# 이를 통해 우선순위 큐 없이도 거리순 정렬 상태를 유지하며 최단 거리를 탐색함

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())

    queue = deque()
    queue.append(n)

    times = [100001] * 100001
    times[n] = 0

    while queue:
        # front에서 먼저 처리
        pop_num = queue.popleft()
        if pop_num == k:
            print(times[k])
            return
        
        telpo = pop_num * 2
        front_move = pop_num + 1
        back_move = pop_num - 1

        if telpo <= 100000 and times[telpo] > times[pop_num]:
            # 순간이동을 먼저 가중치가 0이므로 왼쪽에 삽입
            queue.appendleft(pop_num * 2)
            times[telpo] = times[pop_num]
        
        # 양쪽 걷기 
        # if 0 <= front_move <= 100000:
        #     # -1 +1은 1초가 걸리므로 오른쪽에 삽입
        #     if times[front_move] > times[pop_num] + 1:
        #         queue.append(pop_num + 1)
        #         times[front_move] = times[pop_num] + 1
        # if 0 <= back_move <= 100000:
        #     if times[back_move] > times[pop_num] + 1:
        #         queue.append(pop_num - 1)
        #         times[back_move] = times[pop_num] + 1
        for move in [back_move, front_move]:
            if move >= 0 and move < 100001 and times[move] > times[pop_num] + 1:
                times[move] = times[pop_num] + 1
                queue.append(move)

    return

def dijkstra_solution():
    n, k = map(int, input().split())

    dist = [float("inf")] * 100001
    dist[n] = 0

    pq = []
    heapq.heappush(pq, (0, n))

    while pq:
        time, curr = heapq.heappop(pq)

        if dist[curr] < time:
            continue

        if curr == k:
            print(time)
            return
        
        # 순간이동
        telpo = curr * 2
        if telpo < 100001 and dist[telpo] > time:
            dist[telpo] = time
            heapq.heappush(pq, (time, curr * 2))
        
        # 걷기
        for move in [curr - 1, curr + 1]:
            if move >= 0 and move < 100001 and dist[move] > time + 1:
                dist[move] = time + 1
                heapq.heappush(pq, (time + 1, move))
    
    return

if __name__ == "__main__":
    solution()
    dijkstra_solution()