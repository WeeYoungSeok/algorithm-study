import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/2615

# [문제 정보]
# 분류 : BOJ 2615 : 오목
# 난이도 : 골드 5

# [풀이 방법]
# 바둑돌을 만나면 우, 하, 오른 아래 대각, 왼 아래 대각으로 돌을 찾는다
# 만약 내가 시작점이 아니라면 continue
# 이동하다 끊기면 break
# 5번을 이동해서 5개를 찾았다면 다음돌까지만 확인
# 다음돌이 나랑 같지 않다면 오목 완성

input = sys.stdin.readline

def concave(baduk, i, j):

    # 우, 하, 오른 아래, 왼 아래
    dx = [0, 1, 1, -1]
    dy = [1, 0, 1, 1]

    
    for k in range(4):
        # 내가 시작점인지 확인
        cx = i - dx[k]
        cy = j - dy[k]
        if cx >= 0 and cx < 19 and cy >= 0 and cy < 19:
            if baduk[cx][cy] == baduk[i][j]:
                continue

        cnt = 1
        nx = i
        ny = j
        for _ in range(4):
            nx += dx[k]
            ny += dy[k]
            if nx >= 0 and nx < 19 and ny >= 0 and ny < 19 and baduk[nx][ny] == baduk[i][j]:
                cnt += 1
            else:
                break
        if cnt == 5:
            # 다음 한칸 더 확인
            nx += dx[k]
            ny += dy[k]
            # 6번째가 판 밖이거나, 다른 색이면 -> 진짜 5목 (정답!)
            if not (nx >= 0 and nx < 19 and ny >= 0 and ny < 19 and baduk[nx][ny] == baduk[i][j]):
                return True
    return False


def solution():
    baduk = []

    for _ in range(19):
        baduk.append(list(map(int, input().split())))

    is_win = False
    for i in range(19):
        for j in range(19):
            if baduk[i][j] == 1 or baduk[i][j] == 2:
                if concave(baduk, i, j):
                    is_win = True
                    print(baduk[i][j])
                    print(i + 1, j + 1)
                    break
        if is_win:
            break

    if not is_win:
        print(0)
    return

if __name__ == "__main__":
    solution()