import sys

# [문제 링크]
# https://www.acmicpc.net/problem/19941

# [문제 정보]
# 분류 : BOJ 19941 : 햄버거 분배
# 난이도 : 실버 3

# [풀이 방법]
# 햄버거와 사람 리스트를 순회하면서 사람을 만났을 때
# 그 사람을 기준으로 k만큼 왼쪽부터 우측까지 순회
# 왼쪽부터 햄버거를 먹는게 가장 이득이므로 햄버거를 찾자마자 count += 1해주고 break
# count 출력

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    h_p = list(input().strip())
    count = 0

    for i in range(n):
        if h_p[i] == "P":
            ''' 왼쪽 오른쪽을 따로 찾는 코드는 복잡함
            left_idx = -1
            right_idx = -1
            for j in range(1, k + 1):
                if i - j >= 0 and h_p[i - j] == "H":
                    left_idx = i - j
            if left_idx == -1:
                for j in range(1, k + 1):
                    if i + j < len(h_p) and h_p[i + j] == "H":
                        right_idx = i + j
                        break
            if left_idx > -1:
                h_p[left_idx] = "O"
                count += 1
            elif left_idx == -1 and right_idx > -1:
                h_p[right_idx] = "O"
                count += 1
            '''

            # 왼쪽 오른쪽을 동시에 찾자
            for j in range(i - k, i + k + 1):
                if (j >= 0 and j < n) and h_p[j] == "H":
                    h_p[j] = "O"
                    count += 1
                    break      

    print(count)
    return

def solution_clean():
    n, k = map(int, input().split())
    h_p = list(input().strip())
    count = 0

    for i in range(len(h_p)):
        if h_p[i] == "P":
            start = max(i - k, 0)
            end = min(i + k + 1, n)

            for j in range(start, end):
                if h_p[j] == "H":
                    h_p[j] = "O"
                    count += 1
                    break

    print(count)
    return

if __name__ == "__main__":
    solution()
    # solution_clean()