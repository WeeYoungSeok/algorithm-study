import sys

# [문제 링크]
# https://www.acmicpc.net/problem/2012

# [문제 정보]
# 분류 : BOJ 2012 : 등수 매기기
# 난이도 : 실버 3

# [풀이 방법]
# 불만도의 합을 최소화하기 위해 예상 등수를 오름차순으로 정렬
# 정렬된 예상 등수에 1등부터 N등까지 순서대로 배정하여 차이의 절댓값을 합산

input = sys.stdin.readline

def solution():
    n = int(input())

    expec_ranks = []
    for _ in range(n):
        expec_ranks.append(int(input()))
    
    expec_ranks.sort()

    result = 0
    
    for i in range(n):
        result += abs((i + 1) - expec_ranks[i])
    
    print(result)
    return

if __name__ == "__main__":
    solution()