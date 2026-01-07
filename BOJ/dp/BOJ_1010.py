import sys
import math

# [문제 링크]
# https://www.acmicpc.net/problem/1010

# [문제 정보]
# 분류 : BOJ 1010 : 다리 놓기
# 난이도 : 실버 5

# [풀이 방법]
# 많은(m)쪽에서 적은(n)쪽으로 뽑기만 하면 됨
# 많은쪽에서 적은쪽으로 연결할 때 여러가지의 경우의 수가 나오는데
# 그 중 다리가 꼬이지 않는 경우의 수는 한가지이므로
# mCn 공식을 쓰면 풀림

input = sys.stdin.readline

def solution():
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        # print(math.factorial(m) // (math.factorial(n) * math.factorial(m - n)))
        
        # 조합 공식 써도됨
        # m개 중에 n개를 뽑기만 하면 끝 (순서는 자동)
        print(math.comb(m, n))
    return

if __name__ == "__main__":
    solution()