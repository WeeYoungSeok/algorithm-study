import sys

# [문제 링크]
# https://www.acmicpc.net/problem/18258

# [문제 정보]
# 분류 : BOJ 18258 : 큐 2
# 난이도 : 실버 4

# [풀이 방법]
# 파이썬 라이브러리 deque 이용
# 요구조건에 맞게 분기를 나눔

input = sys.stdin.readline

from collections import deque

def solution():
    n = int(input())

    queue = deque()

    for _ in range(n):
        command = input().strip()
        if command == "pop":
            if not queue:
                print(-1)
            else:
                print(queue.popleft())
        elif command == "size":
            print(len(queue))
        elif command == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif command == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif command == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)
        else:
            queue.append(int(command.split(" ")[1]))
    return

if __name__ == "__main__":
    solution()