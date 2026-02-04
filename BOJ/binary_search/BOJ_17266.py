import sys

# [문제 링크]
# https://www.acmicpc.net/problem/17266

# [문제 정보]
# 분류 : BOJ 17266 : 어두운 굴다리
# 난이도 : 실버 4

# [풀이 방법]
# 이분 탐색으로 높이를 이등분하여 진행
# 이전에 끝에 비춘 곳보다 이번에 새롭게 왼쪽에 비춘 곳이 크다면 사이사이가 비어있음
# 그렇다면 높이를 다시 조정
# 사이사이가 다 메꿔졌다면 제일 마지막 지점까지 빛을 비추는지 확인
# 전부다 메꿔졌어도 높이를 줄여서 최소의 높이로 만듦

input = sys.stdin.readline

def binary_search(n, lamp_x):
    start = 1
    end = n
    result = n

    while start <= end:
        is_possible = True
        mid = (start + end) // 2

        prev_end_light_x = 0

        for lamp in lamp_x:
            if prev_end_light_x < lamp - mid:
                is_possible = False
                break
            
            prev_end_light_x = lamp + mid
        
        if not is_possible or prev_end_light_x < n:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
                
    return result
            

    

def solution():
    n = int(input())
    m = int(input())
    lamp_x = list(map(int, input().split()))

    print(binary_search(n, lamp_x))
    return

if __name__ == "__main__":
    solution()