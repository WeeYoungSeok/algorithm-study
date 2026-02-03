import sys
from collections import defaultdict

# [문제 링크]
# https://www.acmicpc.net/problem/9017

# [문제 정보]
# 분류 : BOJ 9017 : 크로스 컨트리
# 난이도 : 실버 3

# [나의 풀이]
# [풀이 방법]
# 팀의 인원 수를 dictionary로 저장
# 6명이 안되는 팀원 제외한 팀의 등수 리스트를 갱신
# 등수 리스트를 돌면서 상위 4명의 합산 점수와 5번째 선수의 idx를 저장
# [[팀, 4명 합산, 5번째 선수 idx], ...]를 4명 합산 작은, 5번째 선수 idx 작은순으로 정렬
# 0번지의 0번지를 출력

# [클린 코드]
# [풀이 방법]
# 팀의 인원 수를 dictionary로 저장
# 등수의 리스트를 돌면서 6명이 이상인 팀만 새로운 dictionary에 저장
# 저장 형태 {팀 : [등수1, 등수2, 등수3...]}
# 해당 dictionary를 돌면서 4명 합산, 5번째 선수의 등수를 저장
# 나의 풀이 방법과 동일한 sort방식을 이용
# 0번지의 0번지를 출력

input = sys.stdin.readline

def get_counts(seq): 
    counts = {}
    for x in seq:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def solution():
    t = int(input())

    for _ in range(t):
        n = int(input())

        teams = list(map(int, input().split()))

        teams_dict = get_counts(teams)
        # remove 함수는 시간 복잡도가 O(N)이므로 느림
        # for k, v in teams_dict.items():
        #     if v < 6:
        #         while k in teams:
        #             teams.remove(k)

        # 리스트 컴프리헨션으로 새로운 리스트 생성
        teams = [x for x in teams if teams_dict[x] >= 6]
        scores = []

        for k, v in teams_dict.items():
            if v >= 6:
                score = [k]
                score_sum = 0
                five_idx_count = 0
                five_idx = 0
                for i in range(len(teams)):
                    if teams[i] == k:
                        if five_idx_count < 4:
                            score_sum += (i + 1)   
                        if five_idx_count < 5:
                            five_idx = i
                        five_idx_count += 1
                score.append(score_sum)
                score.append(five_idx)
                scores.append(score)

        # lambda sort 구현
        # winner = 0
        # min_score = sys.maxsize
        # five_idx = 0
        # for i in range(len(scores)):
        #     if min_score > scores[i][1]:
        #         min_score = scores[i][1]
        #         five_idx = scores[i][2]
        #         winner = scores[i][0]
        #     elif min_score == scores[i][1]:
        #         if five_idx > scores[i][2]:
        #             winner = scores[i][0]
        #             five_idx = scores[i][2]
        scores.sort(key=lambda x: (x[1], x[2]))
        print(scores[0][0])
                        
    return

def solution_clean():
    t = int(input())

    for _ in range(t):
        n = int(input())

        teams = list(map(int, input().split()))

        # 1. 각 팀의 인원수 세기
        counts = defaultdict(int)
        for team in teams:
            counts[team] += 1
        
        team_ranks = defaultdict(list)
        rank = 1 

        for team in teams:
            if counts[team] >= 6:
                team_ranks[team].append(rank)
                rank += 1
        
        winner_teams = []

        for team, ranks in team_ranks.items():
            score_sum = sum(ranks[:4])
            fifth_score = ranks[4]
            winner_teams.append((team, score_sum, fifth_score))

        winner_teams.sort(key=lambda x: (x[1], x[2]))
        print(winner_teams[0][0]) 
    return

if __name__ == "__main__":
    solution()
    # solution_clean()