import sys

# [문제 링크]
# https://www.acmicpc.net/problem/2304

# [문제 정보]
# 분류 : BOJ 2304 : 창고 다각형
# 난이도 : 실버 2

# [풀이 방법]
# 기둥 정보를 리스트(storage)에 저장 (인덱스: 위치, 값: 높이)
# 전체 기둥 중 가장 높은 높이(max_h)를 찾고, 그 높이를 가진 첫 번째와 마지막 인덱스를 구함
# 최고점 구간(first_max_idx ~ last_max_idx)의 면적을 먼저 계산
# 왼쪽 끝에서부터 첫 번째 최고점까지 이동하며, '현재까지의 최댓값'을 면적에 계속 누적
# 오른쪽 끝에서부터 마지막 최고점까지 거꾸로 이동하며, '현재까지의 최댓값'을 면적에 계속 누적

input = sys.stdin.readline

def solution():
    n = int(input())

    storage = [0] * 1001

    for _ in range(n):
        l, h = map(int, input().split())

        storage[l] = h

    area = 0
    max_h = max(storage)
    max_indices = [i for i, x in enumerate(storage) if x == max_h]
    # 가장 높은 기둥 찾기
    first_max_idx = max_indices[0]
    last_max_idx = max_indices[-1]

    area += (last_max_idx - first_max_idx + 1) * max_h

    '''왼쪽, 오른쪽에서 끝까지 가다가 max에서 탈출할 필요가 있을까?
    # 왼쪽에서 오기
    left_current_max_h = 0
    for i in range(len(storage)):
        if storage[i] == max_h:
            break
        else:
            if left_current_max_h < storage[i]:
                left_current_max_h = storage[i]
            area += left_current_max_h
    
    # 오른쪽에서 오기
    right_current_max_h = 0
    for i in range(len(storage) -1, -1, -1):
        if storage[i] == max_h:
            break
        else:
            if right_current_max_h < storage[i]:
                right_current_max_h = storage[i]
            area += right_current_max_h
    '''

    # 이렇게 왼쪽에서 갈때 처음 만나는 최대값 index까지만
    # 왼쪽에서 오기
    left_current_max_h = 0
    for i in range(first_max_idx):
        # 여기서 더 클린하게
        # if left_current_max_h < storage[i]:
        #     left_current_max_h = storage[i]
        left_current_max_h = max(left_current_max_h, storage[i])
        area += left_current_max_h
    
    # 오른쪽에서 갈때 처음 만나는 최대값 index까지만
    # 오른쪽에서 오기
    right_current_max_h = 0
    for i in range(len(storage) -1, last_max_idx, -1):
        # 여기도 더 클린하게
        # if right_current_max_h < storage[i]:
        #     right_current_max_h = storage[i]
        right_current_max_h = max(right_current_max_h, storage[i])
        area += right_current_max_h

    print(area)
    return

if __name__ == "__main__":
    solution()