import sys

# [문제 링크]
# https://www.acmicpc.net/problem/7568

# [문제 정보]
# 분류 : BOJ 7568 : 덩치
# 난이도 : 실버 5

# [풀이 방법]
# 자신보다 큰 명수 + 1이 자신의 등수이므로 rank 리스트 값 1, 크기 n으로 초기화
# 리스트를 이중 for문으로 돌면서 자신보다 큰 사람 만나면 rank[i] += 1
# 출력

input = sys.stdin.readline

def solution():
    n = int(input())
    people = []
    rank = []

    for _ in range(n):
        people.append(list(map(int, input().split())))
    
    for i in range(n):
        over_cnt = 1
        for j in range(i + 1, n):
            if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
                over_cnt += 1
        for k in range(i - 1, -1, -1):
            if people[i][0] < people[k][0] and people[i][1] < people[k][1]:
                over_cnt += 1
        rank.append(over_cnt)
    print(" ".join(map(str, rank)))
    return


def solution_my_clean():
    n = int(input())
    people = []
    rank = [1] * n

    for _ in range(n):
        people.append(list(map(int, input().split())))
    
    for i in range(n):
        for other in people:
            if people[i][0] < other[0] and people[i][1] < other[1]:
                rank[i] += 1
    print(*rank)
    return

if __name__ == "__main__":
    # solution()
    solution_my_clean()