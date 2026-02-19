import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/1406

# [문제 정보]
# 분류 : BOJ 1406 : 에디터
# 난이도 : 실버 2

# [풀이 방법]
# 커서를 기준으로 문자열을 left와 right 두 개의 deque로 나눔
# L (왼쪽 이동): left의 마지막 요소를 빼서 right의 앞부분에 넣음
# D (오른쪽 이동): right의 첫 요소를 빼서 left의 마지막에 넣음
# B (삭제): left의 마지막 요소를 삭제
# P x (추가): left의 마지막에 x를 추가
# 모든 연산은 deque의 append/pop을 사용하므로 O(1)에 처리

input = sys.stdin.readline

def solution():
    left_word = deque(list(input().strip()))
    right_word = deque([])
    n = int(input())

    for _ in range(n):
        command = list(input().strip().split())
        
        if len(command) == 2:
            left_word.append(command[1])
        else:
            if command[0] == "L":
                if len(left_word) > 0:
                    right_word.appendleft(left_word.pop())
            elif command[0] == "D":
                if len(right_word) > 0:
                    left_word.append(right_word.popleft())
            else:
                if len(left_word) > 0:
                    left_word.pop()
    print("".join(left_word + right_word))
    return

if __name__ == "__main__":
    solution()