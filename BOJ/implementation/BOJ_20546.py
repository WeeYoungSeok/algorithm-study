import sys

# [문제 링크]
# https://www.acmicpc.net/problem/20546

# [문제 정보]
# 분류 : BOJ 20546번 : 기적의 매매법
# 난이도 : 실버5

# [풀이 방법]
# 준현, 성민의 현재돈, 주식의 개수 리스트 생성
# 준현은 현재 돈이 주가보다 많다면 무조건 매수
# 성민은 처음날은 지나가고 다음날부터 주가를 전날 주가와 비교하여
# 3일 '연속'으로 오르거나 내리면 매수 or 매도 진행
# 마지막에 비교

input = sys.stdin.readline

def solution():
    money = int(input())
    bnp = [money, 0]
    timing = [money, 0]

    max_sqe = 0
    min_sqe = 0

    stock = list(map(int, input().split()))
    for i in range(len(stock)):
        if bnp[0] >= stock[i]:
                bnp[1] += (bnp[0] // stock[i])
                bnp[0] %= stock[i]
        if i > 0:
            if stock[i] < stock[i - 1]:
                max_sqe = 0
                if min_sqe < 2:
                    min_sqe += 1
                else:
                    if timing[0] >= stock[i]:
                        timing[1] += (timing[0] // stock[i])
                        timing[0] %= stock[i]
            elif stock[i] > stock[i - 1]:
                min_sqe = 0
                if max_sqe < 2:
                    max_sqe += 1
                else:
                    if timing[1] != 0:
                        timing[0] += timing[1] * stock[i]
                        timing[1] = 0

    if (bnp[1] * stock[-1]) + bnp[0] > (timing[1] * stock[-1]) + timing[0]:
        print("BNP")
    elif (bnp[1] * stock[-1]) + bnp[0] < (timing[1] * stock[-1]) + timing[0]:
        print("TIMING")
    else:
        print("SAMESAME")
    return

if __name__ == "__main__":
    solution()