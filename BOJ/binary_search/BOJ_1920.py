import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1920

# [문제 정보]
# 분류 : BOJ 1920 : 수 찾기
# 난이도 : 실버 4

# [풀이 방법]
# 이중 for문을 돌면 10만 x 10만이여서 시간 초과
# 이분탐색을 이용하여 접근
# 파이썬의 set을 이용하면 더 빠르게 풀기 가능

input = sys.stdin.readline

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

def solution():
    n = int(input())
    n_list = list(map(int, input().split()))
    n_list.sort()

    m = int(input())
    m_list = list(map(int, input().split()))
    
    for num in m_list:
        print(binary_search(num, n_list))
    return

def solution_set():
    n = int(input())
    n_set = set(map(int, input().split())) 

    m = int(input())
    m_list = list(map(int, input().split()))

    for num in m_list:
        if num in n_set:  
            print(1)
        else:
            print(0)
    return

if __name__ == "__main__":
    # solution()
    solution_set()