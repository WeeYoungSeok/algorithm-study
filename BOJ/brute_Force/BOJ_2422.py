import sys

# [문제 링크]
# https://www.acmicpc.net/problem/2422

# [문제 정보]
# 분류 : BOJ 2422 : 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
# 난이도 : 실버 4

# [풀이 방법]
# 아이스크림 조합 이중 배열을 만듦
# 조합하면 안되는 번호가 아이스크림 이중배열 번호와 같다고할때
# 해당 부분만 True로 바꿈
# 첫번째 아이스크림을 돌면서 두번째, 세번째까지 돌아서
# 조합이 가능한 아이스크림만 도출하면서 cnt를 증가해줌

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())

    bad_check = [[False] * (n + 1) for _ in range(n + 1)]
    cnt = 0

    for _ in range(m):
        i, j = map(int, input().split())
        bad_check[i][j] = True
        bad_check[j][i] = True

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if bad_check[i][j]:
                continue

            for k in range(j + 1, n + 1):
                if bad_check[i][k] or bad_check[j][k]:
                    continue
                cnt += 1

    print(cnt)
    return

if __name__ == "__main__":
    solution()