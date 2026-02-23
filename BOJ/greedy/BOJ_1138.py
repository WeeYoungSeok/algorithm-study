import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1138

# [문제 정보]
# 분류 : BOJ 1138 : 한 줄로 서기
# 난이도 : 실버 2

# [풀이 방법]
# 키 1부터 N까지 순서대로 배치 (작은 사람부터 배치하면 뒤에 올 사람은 무조건 나보다 크다)
# 각 사람마다 "왼쪽에 나보다 큰 사람이 몇 명 있는지(p[i])" 정보를 확인
# 결과 리스트(result)를 순회하며 '비어있는 칸(0)'의 개수를 셈
# 빈칸의 개수가 p[i]와 같아지는 순간 그 빈칸이 바로 해당 사람이 앉아야 할 자리

input = sys.stdin.readline

def solution():
    n = int(input())
    p = list(map(int, input().split()))

    result = [0] * n

    for i in range(n):
        count = 0
        for j in range(n):
            if result[j] == 0:
                if count == p[i]:
                    result[j] = i + 1
                    break
                count += 1
            
    print(*result)
    return

if __name__ == "__main__":
    solution()