import sys

# [문제 링크]
# https://www.acmicpc.net/problem/10655

# [문제 정보]
# 분류 : BOJ 10655 : 마라톤 1
# 난이도 : 실버 3

# [풀이 방법]
# 1번부터 N번까지의 전체 맨해튼 거리를 먼저 구함
# 2번부터 N-1번까지 각 체크포인트를 하나씩 건너뛰었을 때 줄어드는 거리를 계산함
# (전체 거리 - 기존 경로 거리 + 지름길 거리)의 최솟값을 출력함

input = sys.stdin.readline

def solution():
    n = int(input())
    check_points = []
    
    for _ in range(n):
        check_points.append(list(map(int, input().split())))
    
    sum_distance = 0

    for i in range(n - 1):
        sum_distance += abs(check_points[i][0] - check_points[i + 1][0]) + abs(check_points[i][1] - check_points[i + 1][1]) 

    result = float("inf")

    for i in range(1, n - 1):
        distance = 0
        # 해당 지점에서 이전 지점까지의 거리
        distance -= abs(check_points[i - 1][0] - check_points[i][0]) + abs(check_points[i - 1][1] - check_points[i][1])
        # 해당 지점에서 다음 지점까지의 거리
        distance -= abs(check_points[i + 1][0] - check_points[i][0]) + abs(check_points[i + 1][1] - check_points[i][1])
        # 해당 지점 이전 ~ 해당 지점 다음까지의 거리
        distance += abs(check_points[i + 1][0] - check_points[i - 1][0]) + abs(check_points[i + 1][1] - check_points[i - 1][1])
        result = min(sum_distance + distance, result)

    print(result)
    return

if __name__ == "__main__":
    solution()