import sys
from collections import deque
import copy

# [문제 링크]
# https://www.acmicpc.net/problem/12919

# [문제 정보]
# 분류 : BOJ 12919 : A와 B 2
# 난이도 : 골드 5

# [풀이 방법]
# T에서 S로 한 글자씩 지워가는 역방향 브루트포스 탐색을 수행함
# 앞이 'B'인 경우와 뒤가 'A'인 경우를 모두 확인해야 하므로 재귀를 활용함
# 리스트 슬라이싱을 통해 원본을 보존하며 효율적으로 복사본을 생성함

input = sys.stdin.readline

def find(current_t: deque, s: deque):
    if current_t == s:
        return True
    if len(current_t) <= len(s) or (current_t[0] == "A" and current_t[-1] == "B"):
        return False
    
    if current_t[0] == "B":
        copy_t = copy.deepcopy(current_t)
        copy_t.popleft()
        copy_t.reverse()
        if find(copy_t, s):
            return True
    if current_t[-1] == "A":
        copy_t = copy.deepcopy(current_t)
        copy_t.pop()
        if find(copy_t, s):
            return True
        
    return False

def solution():
    s = deque(input().strip())
    t = deque(input().strip())
        
    if find(copy.deepcopy(t), s):
        print(1)
    else:
        print(0)
    return


def list_find(current_t: list, s: list):
    if current_t == s:
        return True
    if len(current_t) <= len(s) or (current_t[0] == "A" and current_t[-1] == "B"):
        return False
    
    if current_t[0] == "B":
        if list_find(current_t[1:][::-1], s):
            return True
    if current_t[-1] == "A":
        if list_find(current_t[:-1], s):
            return True
    return False

def list_solution():
    s = list(input().strip())
    t = list(input().strip())

    if list_find(t, s):
        print(1)
    else:
        print(0)
    return

if __name__ == "__main__":
    # solution()
    list_solution()