import sys
from collections import defaultdict

# [문제 링크]
# https://www.acmicpc.net/problem/3758

# [문제 정보]
# 분류 : BOJ 3758 : KCPC
# 난이도 : 실버 2

# [풀이 방법]
# 각 팀의 문제별 점수를 저장하기 위해 defaultdict(lambda: defaultdict(int))를 사용
#  - 키가 없어도 자동으로 생성되며 기본값 0을 보장하여 예외 처리를 줄임
# 로그를 순회하며 다음을 수행
#  - 해당 팀의 제출 횟수 증가
#  - 해당 팀의 마지막 제출 시간 갱신
#  - 해당 문제의 점수가 기존 점수보다 높을 경우 갱신 (최댓값 유지)
# 모든 로그 처리 후 팀별 총점을 계산
# [팀ID, 총점, 제출횟수, 마지막제출시간] 리스트를 생성
# 정렬 기준(key)을 설정하여 정렬: (-총점, 제출횟수, 마지막제출시간)
# 정렬된 리스트에서 내 팀(my_team)의 인덱스를 찾아 등수(index + 1)를 출력

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