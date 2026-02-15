import sys

# [문제 링크]
# https://www.acmicpc.net/problem/20310

# [문제 정보]
# 분류 : BOJ 20310 : 타노스
# 난이도 : 실버 3

# [풀이 방법]
# 1. 일반적인 그리디 풀이 (solution)
#    - 문자열에 포함된 1과 0의 개수 절반을 구함
#    - 1은 앞에서부터 지우고(remove), 0은 뒤에서부터 지움
#    - 리스트 삭제 연산으로 인해 O(N^2) 시간 복잡도를 가짐
#
# 2. 시간 복잡도 최적화 풀이 (solution_boolean_marking)
#    - visited 배열을 생성하여 모든 인덱스를 True로 초기화
#    - 앞에서부터 '1'을 찾아 False로 마킹하고, 뒤에서부터 '0'을 찾아 False로 마킹
#    - 마지막에 visited가 True인 문자들만 모아서 출력
#    - 리스트 요소 삭제 없이 순회만 하므로 O(N)으로 해결 가능

input = sys.stdin.readline

def solution():
    s = list(input().strip())

    one_count = s.count("1") // 2
    zero_count = s.count("0") // 2

    # 앞에서부터 1 지우기
    while one_count > 0:
        s.remove("1")
        one_count -= 1

    # 뒤에서부터 0 지우기
    start = len(s) - 1
    while zero_count > 0:
        if s[start] == "0":
            del s[start]
            zero_count -= 1
        start -= 1
    print("".join(s))
    return

def solution_boolean_marking():
    s = list(input().strip())
    n = len(s)
    
    # 1. visited 배열 생성 (일단 다 True로 살려둠)
    # True: 출력할 놈 / False: 지울 놈
    visited = [True] * n 
    
    # 지워야 할 개수 구하기
    k_one = s.count('1') // 2
    k_zero = s.count('0') // 2

    # 2. 앞에서부터 '1' 지우기 (스티커 붙이기)
    cnt = 0
    for i in range(n):
        if cnt == k_one: # 지울 목표 채웠으면 그만
            break
            
        if s[i] == '1':
            visited[i] = False # "너 삭제!" 마킹
            cnt += 1

    # 3. 뒤에서부터 '0' 지우기 (스티커 붙이기)
    cnt = 0
    for i in range(n - 1, -1, -1): # 역순 탐색
        if cnt == k_zero:
            break
            
        if s[i] == '0':
            visited[i] = False # "너 삭제!" 마킹
            cnt += 1

    # 4. visited가 True인 애들만 출력
    answer = []
    for i in range(n):
        if visited[i]: # 살아남은 애들만
            answer.append(s[i])
            
    print("".join(answer))

if __name__ == "__main__":
    # solution()
    solution_boolean_marking()