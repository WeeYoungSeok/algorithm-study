import sys

# [문제 링크]
# https://www.acmicpc.net/problem/14467

# [문제 정보]
# 분류 : 백준 14467번 : 소가 길을 건너는 이유
# 난이도 : 브론즈1

# [풀이 방법]
# 소들의 위치를 처음에 -1로 초기화
# 입력 받은 소의 위치가 -1이면 이동하지 않고 최초 위치로 고정
# 입력 받은 소의 위치가 -1이 아니면서 입력 받은 소의 위치랑 다르면 이동
# 이때 해당 소가 움직였다고 판단하여 caws_move의 숫자 증가 
# 위치가 같다면 caws_move 변동 x
# 모든 소의 위치 이동을 전부 더해줌

input = sys.stdin.readline

def solution():
    caws = [-1] * 11
    total_move = 0
    n = int(input())

    for _ in range(n):
        caw_num, move = map(int, input().split())
        if caws[caw_num - 1] != -1:
            caws[caw_num - 1] = move
        elif caws[caw_num - 1] != move:
            caws[caw_num - 1] = move
            total_move += 1

    print(total_move)
    return

if __name__ == "__main__":
    solution()