import sys

# [문제 링크]
# https://www.acmicpc.net/problem/14916

# [문제 정보]
# 분류 : BOJ 14916 : 거스름돈
# 난이도 : 실버5

# [풀이 방법]
# 5원으로 거슬러줄 수 있냐 없냐를 나눠서 분기 처리
# 5원으로 거슬러줄 수 없을때 규칙이 생겨서 규칙을 적용

input = sys.stdin.readline

def solution():
    n = int(input())
    coin = 0
    while n > 0:
        if n == 1 or n == 3:
            break
        # 최소 개수
        if n % 5 == 0:
            coin += n // 5
            n = 0
        # 5원으로만 거슬러 줄 수 없다면?
        else:
            if n % 5 == 1 or n % 5 == 3:
                coin += (n // 5) - 1
                n = (n % 5) + 5
            else:
                coin += n // 5
                n = n % 5
            coin += (n // 2)
            n = (n % 2)

    if coin == 0:
        print(-1)
    else:
        print(coin)
    return


# 1년전 나의 코드 이게 더 좋고 가독성도 좋음

# [풀이 방법]
# 5원으로 거슬러줄 수 있냐 없냐를 나눠서 분기 처리
# 5원으로 거슬러줄 수 없을때 2원만 한번 빼고 다시 5원으로만 확인

def solution():
    n = int(input())
    coin = 0
    while n > 0:
        if n % 5 == 0:
            coin += n // 5
            break
        else:
            n -= 2
            coin += 1

    if n < 0:
        print(-1)
    else:
        print(coin)
    return

if __name__ == "__main__":
    solution()