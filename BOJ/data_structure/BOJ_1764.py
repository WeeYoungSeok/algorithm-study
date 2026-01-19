import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1764

# [문제 정보]
# 분류 : BOJ 1764 : 듣보잡
# 난이도 : 실버 4

# [풀이 방법]

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())

    n_set = set()
    m_set = set()

    for _ in range(n):
        n_set.add(input().strip())

    for _ in range(m):
        m_set.add(input().strip())
    
    intersection = list(n_set & m_set)
    intersection.sort()

    print(len(intersection))
    for name in intersection:
        print(name)
    return

if __name__ == "__main__":
    solution()