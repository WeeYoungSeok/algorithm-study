import sys

# [문제 링크]
# https://www.acmicpc.net/problem/18115

# [문제 정보]
# 분류 : BOJ 18115 : 카드 놓기
# 난이도 : 실버 3

# [풀이 방법]
# 카드는 항상 1 ~ n순이므로
# 기술을 역추적하여 1번은 맨 앞(left), 3번은 맨 뒤(right), 2번은 왼쪽에서 2번째에 배치

from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    commands = list(map(int, input().split()))
    commands.reverse()

    queue = deque()

    for i in range(n):
        if commands[i] == 1:
            queue.appendleft(i + 1)
        elif commands[i] == 2:
            prev = queue.popleft()
            queue.appendleft(i + 1)
            queue.appendleft(prev)
        else:
            queue.append(i + 1)

    print(*queue)
    return

if __name__ == "__main__":
    solution()