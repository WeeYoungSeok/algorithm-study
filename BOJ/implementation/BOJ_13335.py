import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/13335

# [문제 정보]
# 분류 : BOJ 13335 : 트럭
# 난이도 : 실버 1

# [풀이 방법]
# 다리 길이(w)만큼 0으로 채워진 deque를 생성
# 매 초마다 다리 맨 앞의 원소를 제거하고 다음 트럭이 진입 가능한지 확인
# 진입 가능하면 트럭을 추가하고 불가능하면 0을 추가하여 다리 길이를 유지
# 모든 트럭이 진입한 뒤 마지막 트럭이 빠져나가는 시간(w)을 더해줌

input = sys.stdin.readline

def solution():
    n, w, l = map(int, input().split())

    truck = list(map(int, input().split()))
    bridge = [0] * w

    result = 0
    idx = 0

    while idx < n:
        sum_weight = sum(bridge)
        # 트럭 바로 태우기
        if sum_weight == 0:
            bridge[-1] = truck[idx]
            idx += 1
            result += 1
        else:
            # 만약 다음 트럭이 탈 수 있다면 한칸 밀고 맨 밑에 태우기
            if sum_weight + truck[idx] <= l:
                bridge = bridge[1:] + [truck[idx]]
                idx += 1
                result += 1
            else:
                # 다음 트럭이 탈 수 없다면 한칸씩 앞으로 이동
                while sum_weight + truck[idx] > l:
                    sum_weight -= bridge[0]

                    for i in range(1, w):
                        bridge[i - 1] = bridge[i]
                    bridge[-1] = 0
                    result += 1

                # 이동된 후에 탈 수 있으므로 다음 트럭을 태움
                bridge[-1] = truck[idx]
                idx += 1
        
            
    # 마지막 트럭이 지나가는 시간만큼 더해줌
    print(result + w)
    return

def solution_clean():
    n, w, l = map(int, input().split())
    trucks = list(map(int, input().split()))
    
    # 1. 다리를 0으로 가득 찬 리스트로 초기화 (길이 w 유지)
    bridge = [0] * w
    curr_weight = 0 # 다리 위 현재 총 무게를 실시간으로 관리
    time = 0
    idx = 0

    # 2. 모든 트럭이 다리에 '진입'할 때까지만 반복
    while idx < n:
        time += 1
        
        # [STEP 1] 다리의 맨 앞 칸에서 트럭(혹은 0)이 나감
        # 리스트의 pop(0)은 맨 앞 원소를 빼내고 뒤의 원소들을 당겨줌
        leaving_truck = bridge.pop(0)
        curr_weight -= leaving_truck

        # [STEP 2] 다음 트럭이 다리에 올라올 수 있는지 판단
        if curr_weight + trucks[idx] <= l:
            # 진입 가능: 트럭을 올리고 무게와 인덱스 갱신
            bridge.append(trucks[idx])
            curr_weight += trucks[idx]
            idx += 1
        else:
            # 진입 불가능: 다리 길이를 유지하기 위해 0을 추가 (트럭들이 한 칸 전진함)
            bridge.append(0)

    # 3. 마지막 트럭이 들어온 순간 루프가 끝나므로
    # 그 트럭이 다리를 완전히 빠져나가는 시간(다리 길이 w)을 더해줌
    print(time + w)
    return

def solution_queue():
    n, w, l = map(int, input().split())
    trucks = list(map(int, input().split()))
    
    # 1. 다리를 0으로 가득 찬 리스트로 초기화 (길이 w 유지)
    bridge = deque([0] * w)
    curr_weight = 0 # 다리 위 현재 총 무게를 실시간으로 관리
    time = 0
    idx = 0
    
    while idx < n:
        time += 1

        leaving_truck = bridge.popleft()
        curr_weight -= leaving_truck

        if curr_weight + trucks[idx] <= l:
            bridge.append(trucks[idx])
            curr_weight += trucks[idx]
            idx += 1
        else:
            bridge.append(0)
    
    print(time + w)
    return

if __name__ == "__main__":
    # solution()
    # solution_clean()
    solution_queue()