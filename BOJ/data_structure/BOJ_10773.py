import sys

# [문제 링크]
# https://www.acmicpc.net/problem/10773

# [문제 정보]
# 분류 : BOJ 10773 : 제로
# 난이도 : 실버 4

# [풀이 방법]
# 정수를 입력받아 0이면 pop, 아니라면 append
# 정수가 0일 경우 지울 수 있는 수가 보장됨

input = sys.stdin.readline

def solution():
    k = int(input())

    money = []
    
    for _ in range(k):
        num = int(input())
        if num == 0:
            money.pop()
        else:
            money.append(num)
    print(sum(money))
    return

if __name__ == "__main__":
    solution()