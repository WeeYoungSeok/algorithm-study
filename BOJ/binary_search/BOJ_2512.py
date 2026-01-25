import sys

# [문제 링크]
# https://www.acmicpc.net/problem/2512

# [문제 정보]
# 분류 : BOJ 2512 : 예산
# 난이도 : 실버 2

# [풀이 방법]
# 정렬 후 현재 예산 // 남은 사람 수를 해서 그 평균 값보다 낮다면
# 일단 예산 처리
# 남은 예산은 남은 예산 // 남은 사람의 수로 해서 평균값으로 처리
# 해당 값이 max값

# [풀이 방법] : binary_search
# start, end를 0원, max금액으로 설정
# 중간값을 상한액으로 설정
# 상한액보다 작으면 그대로 더하고 크면 상한액 만큼 더함
# 총 예산보다 계산된 예산이 작거나 같다면
# 더 큰 상한액이 되나 확인
# 크다면 예산 초과니깐 상한액 중리기


input = sys.stdin.readline

def solution():
    n = int(input())

    budget_list = list(map(int, input().split()))
    budget = int(input())

    budget_list.sort()

    if budget >= sum(budget_list):
        print(max(budget_list))
    else:
        for b in budget_list:
            budget_avg = budget // n
            if budget_avg >= b:
                budget -= b
                n -= 1
        
        print(budget // n)
    return

def solution_binary_search():
    n = int(input())

    budget_list = list(map(int, input().split()))
    budget = int(input())

    if budget >= sum(budget_list):
        print(max(budget_list))
    else:
        start = 0
        end = max(budget_list)

        result = 0

        while start <= end:
            mid = (start + end) // 2

            current_sum = 0
            for b in budget_list:
                current_sum += min(b, mid)

            if current_sum <= budget:
                result = mid
                start = mid + 1
            else:
                end = mid - 1
        
        print(result)

if __name__ == "__main__":
    # solution()
    solution_binary_search()