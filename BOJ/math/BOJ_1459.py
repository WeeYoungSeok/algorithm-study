import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1459

# [문제 정보]
# 분류 : BOJ 1459 : 걷기
# 난이도 : 실버 3

# [풀이 방법]
# 가로/세로로만 가는 경우, 대각선과 가로/세로를 섞는 경우, 대각선으로만 지그재그로 가는 경우를 모두 비교함
# X, Y가 최대 10억이므로 반복문이 아닌 수식으로 한 번에 최솟값을 도출함

input = sys.stdin.readline

def solution():
    x, y, w, s = map(int, input().split())
    diagonal = (max(x, y) - 1) * s + w if (x + y) % 2 else max(x, y) * s

    print(min((x + y) * w, (min(x, y) * s) + (abs(x - y) * w), diagonal))
    
    return

if __name__ == "__main__":
    solution()