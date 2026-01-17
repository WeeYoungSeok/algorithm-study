import sys

# [문제 링크]
# https://www.acmicpc.net/problem/11399

# [문제 정보]
# 분류 : BOJ 11399 : ATM
# 난이도 : 실버 4

# [풀이 방법]
# sort로 정렬 한 뒤
# 현재 사람 걸린 시간 = 이전 사람까지 걸린 시간 + 나
# 모든 값 합쳐서 출력

input = sys.stdin.readline

def solution():
    n = int(input())

    people = list(map(int, input().split()))

    people.sort()
    hap = [0] * (n + 1)
    hap[1] = people[0]

    for i in range(2, n + 1):
        hap[i] = hap[i - 1] + people[i - 1]

    print(sum(hap))
    return

def solution_clean():
    n = int(input())

    people = list(map(int, input().split()))

    people.sort()
    hap = 0
    result = 0

    for p in people:
        hap += p
        result += hap

    print(result)
    return

if __name__ == "__main__":
    # solution()
    solution_clean()