import sys

# [문제 링크]
# https://www.acmicpc.net/problem/21921

# [문제 정보]
# 분류 : BOJ 21921 : 블로그
# 난이도 : 실버 3

# [풀이 방법]
# 방문자 수를 누적합으로 미리 계산
# x일 동안의 방문자 수를 추출해야하니 끝 인덱스부터 end[i] - end[i - x]로 x일 동안의 방문자 수를 모두 추출
# max값과 max값의 count를 출력
# max값이 0이라면 SAD 출력

input = sys.stdin.readline

def solution():
    n, x = map(int, input().split())

    visit_nums = list(map(int, input().split()))

    prefix_sum = [0]

    for i in range(len(visit_nums)):
        prefix_sum.append(prefix_sum[i] + visit_nums[i])

    result = []

    for i in range(n, -1, -1):
        if i - x >= 0:
            result.append(prefix_sum[i] - prefix_sum[i - x])
        else:
            break

    if max(result) == 0:
        print("SAD")
    else:
        print(max(result))
        print(result.count(max(result)))

    return

def solution_sliding_window():
    n, x = map(int, input().split())

    visit_nums = list(map(int, input().split()))

    # 1. 초기 윈도우 (첫 X일간의 합)
    current_sum = sum(visit_nums[:x])

    max_visit = current_sum
    max_count = 1

    for i in range(x, n):
        current_sum += visit_nums[i]
        current_sum -= visit_nums[i - x]

        if current_sum > max_visit:
            max_visit = current_sum
            max_count = 1
        elif current_sum == max_visit:
            max_count += 1
    
    if max_visit == 0:
        print("SAD")
    else:
        print(max_visit)
        print(max_count)

    return

if __name__ == "__main__":
    # solution()
    solution_sliding_window()