import sys
from collections import defaultdict

# [문제 링크]
# https://www.acmicpc.net/problem/22233

# [문제 정보]
# 분류 : BOJ 22233 : 가희와 키워드
# 난이도 : 실버 3

# [풀이 방법]

# [dictionary]
# 딕셔너리에 메모장 키워드 저장 (1로 저장)
# 메모장의 키워드 총 개수를 저장
# 블로그에 쓴 키워드를 딕셔너리 벨류의 값이 1이라면 을 0으로 수정
# 수정과 동시에 총 개수 -1

# [set]
# 메모장의 키워드를 set에 저장
# 블로그에 쓴 키워드를 discard를 통해 삭제 (없으면 무시)
# len으로 개수 출력

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())

    memo = defaultdict(int)

    for _ in range(n):
        memo[input().strip()] = 1
    
    memo_sum = sum(memo.values())

    for _ in range(m):
        keyword = list(input().strip().split(","))
        for k in keyword:
            if memo[k] == 1:
                memo[k] = 0
                memo_sum -= 1
        print(memo_sum)
    return

def solution_set():
    n, m = map(int, input().split())

    memo = set()

    for _ in range(n):
        memo.add(input().strip())
    
    for _ in range(m):
        keyword = list(input().strip().split(","))
        for k in keyword:
            memo.discard(k)
        print(len(memo))
    return

if __name__ == "__main__":
    # solution()
    solution_set()