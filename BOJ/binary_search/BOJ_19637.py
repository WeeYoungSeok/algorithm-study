import sys
from bisect import bisect_left

# [문제 링크]
# https://www.acmicpc.net/problem/19637

# [문제 정보]
# 분류 : BOJ 19637 : IF문 좀 대신 써줘
# 난이도 : 실버 3

# [풀이 방법]
# 입력 데이터가 비내림차순(오름차순)으로 주어지므로 이분 탐색을 사용
# 칭호 이름(title)과 전투력 상한값(score)을 각각 별도의 리스트에 저장
# 캐릭터의 전투력이 주어질 때마다 이분 탐색을 통해 해당 점수가 들어갈 위치를 찾음
# 가장 먼저 입력된 칭호를 출력해야 하므로 bisect_left를 사용

input = sys.stdin.readline

def solution_bisect_left():
    n, m = map(int, input().split())
    title = []
    score = []

    for _ in range(n):
        t, s = map(str, input().strip().split())
        
        title.append(t)
        score.append(int(s))
    
    for _ in range(m):
        s = int(input())
        print(title[bisect_left(score, s)])
        
    return

def solution_binary_search():
    n, m = map(int, input().split())
    title = []
    score = []

    for _ in range(n):
        t, s = map(str, input().strip().split())
        
        title.append(t)
        score.append(int(s))
    
    for _ in range(m):
        s = int(input())
        
        start = 0
        end = n - 1

        # bisect_left 직접 구현
        while start < end:
            mid = (start + end) // 2

            if s <= score[mid]:
                end = mid
            else:
                start = mid + 1
        print(title[start])
    return

if __name__ == "__main__":
    # solution_bisect_left()
    solution_binary_search()