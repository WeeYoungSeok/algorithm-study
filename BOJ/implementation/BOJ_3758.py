import sys
from collections import defaultdict

# [문제 링크]
# https://www.acmicpc.net/problem/3758

# [문제 정보]
# 분류 : BOJ 3758 : KCPC
# 난이도 : 실버 2

# [풀이 방법]


input = sys.stdin.readline

def solution():
    t = int(input())

    for _ in range(t):
        n, k, my_team, m = map(int, input().split())
        team_score = defaultdict(lambda: defaultdict(int))
        submit_count = [0] * (n + 1)
        last_submit_time = [0] * (n + 1)

        for i in range(m):
            team, p_num, score = map(int, input().split())
            submit_count[team] += 1
            last_submit_time[team] = i
            if team_score[team][p_num] < score:
                team_score[team][p_num] = score

        # [팀, 총스코어, 제출횟수, 마지막 제출 시간]
        result = []

        for i in range(1, n + 1):
            # if i not in team_score:
            #     result.append([i, 0, 10001, 10001])
            # else:
            #     hap = 0
            #     for k, v in team_score[i].items():
            #         hap += v
            #     result.append([i, hap, submit_count[i], last_submit_time[i]])

            total_score = sum(team_score[i].values())
            result.append([i, total_score, submit_count[i], last_submit_time[i]])
        
        result.sort(key=lambda x : (-x[1], x[2], x[3]))

        for i in range(len(result)):
            if result[i][0] == my_team:
                print(i + 1)
                break
    return

if __name__ == "__main__":
    solution()