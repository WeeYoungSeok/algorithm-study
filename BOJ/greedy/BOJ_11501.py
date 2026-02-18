import sys

# [문제 링크]
# https://www.acmicpc.net/problem/11501

# [문제 정보]
# 분류 : BOJ 11501 : 주식
# 난이도 : 실버 2

# [풀이 방법]
# 가장 마지막날을 주식 최고가로 가정하고 시작
# 마지막 전날부터 거꾸로 순회하면서 현재 최고가보다 작다면 무조건 매입 (최고가일 때 팔거라서)
# 매입할떄 이익금액에 최고가 - 현재 매입가를 더해줌
# 현재 최고가보다 높다면 최고가 갱신
# 최종적으로 이익 출력

input = sys.stdin.readline

def solution():
    t = int(input())

    for _ in range(t):
        n = int(input())
        
        days = list(map(int, input().split()))
        max_stock = days[-1]
        total_stock = 0

        for i in range(n - 2, -1 ,-1):
            if max_stock >= days[i]:
                total_stock += max_stock - days[i]
            else:
                max_stock = days[i]
        print(total_stock)
            
    return

if __name__ == "__main__":
    solution()