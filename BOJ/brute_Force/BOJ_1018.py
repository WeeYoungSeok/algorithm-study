import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1018

# [문제 정보]
# 분류 : BOJ 1018 : 체스판 다시 칠하기
# 난이도 : 실버 4

# [풀이 방법]
# W로 시작하는 B로 시작하는 체스판을 만듦
# 그 이후 현재 시점부터 가로로 +7, 세로로 +7을 잘라서 비교
# 두 체스판중 적게 바뀐 count를 리턴
# 전체에서 1칸씩 우, 하로 이동하면서 비교하여 가장 작은 값을 출력

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())

    chess = []

    min_change = 33

    for _ in range(n):
        chess.append(list(input().strip()))

    start_w = []
    start_b = []

    for i in range(8):
        row_w = []  
        row_b = []
        for j in range(8):
            if (i + j) % 2 == 0:
                row_w.append("W")
                row_b.append("B")
            else:
                row_w.append("B")
                row_b.append("W")
        start_w.append(row_w)
        start_b.append(row_b)

    def change_count(i, j):
        start_w_cnt = 0
        start_b_cnt = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if chess[x][y] != start_w[x - i][y - j]:
                    start_w_cnt += 1
                if chess[x][y] != start_b[x - i][y - j]:
                    start_b_cnt += 1
               
        return min(start_w_cnt, start_b_cnt)
    # 마지막 위치 -7
    for i in range(n - 7):
        for j in range(m - 7):
            # +7까지만 검사
            cnt = change_count(i, j)
            if cnt < min_change:
                min_change = cnt
    print(min_change)
    return

if __name__ == "__main__":
    solution()