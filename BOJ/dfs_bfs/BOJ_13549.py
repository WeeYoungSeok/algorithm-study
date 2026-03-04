import sys
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
        if pop_num > 100000:
            continue
        telpo = pop_num * 2
        front_move = pop_num + 1
        back_move = pop_num - 1

        if 0 <= telpo <= 100000:
            # 순간이동을 먼저 가중치가 0이므로 왼쪽에 삽입
            if telpo != pop_num:
                if times[telpo] > times[pop_num]:
                    queue.appendleft(pop_num * 2)
                    times[telpo] = times[pop_num]
        
        if 0 <= front_move <= 100000:
            # -1 +1은 1초가 걸리므로 오른쪽에 삽입
            if times[front_move] > times[pop_num] + 1:
                queue.append(pop_num + 1)
                times[front_move] = times[pop_num] + 1
        if 0 <= back_move <= 100000:
            if times[back_move] > times[pop_num] + 1:
                queue.append(pop_num - 1)
                times[back_move] = times[pop_num] + 1

    print(times[k])

    return

if __name__ == "__main__":
    solution()