import sys
from itertools import permutations

# [문제 링크]
# https://www.acmicpc.net/problem/18429

# [문제 정보]
# 분류 : BOJ 18429 : 근손실
# 난이도 : 실버 3

# [풀이 방법]
# N이 최대 8이므로 모든 기구 순서를 순열(Permutations)로 생성
# 매일의 중량 변화를 시뮬레이션하고 500 미만으로 떨어지지 않는 경우만 카운트

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())

    kit = list(map(int, input().split()))
    kit_case = permutations(kit)

    result = 0

    for case in kit_case:
        weight = 500
        is_possible = True
        for val in case:
            weight -= k
            weight += val
            if weight < 500:
                is_possible = False
                break
        if is_possible:
            result += 1
        
    print(result)
    return

if __name__ == "__main__":
    solution()