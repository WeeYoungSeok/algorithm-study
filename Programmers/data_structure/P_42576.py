import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# [문제 정보]
# 분류 : P 42576 : 완주하지 못한 선수
# 난이도 : LV 1

# [풀이 방법]
# 참여자, 완주자를 dic으로 전환
# 완주자를 순회하면서 참여자에서 -1
# 참여자중에 가장 큰 값 리턴

# [다른 풀이 방법]
# 참여자만 dic으로 전환
# 완주자 리스트를 돌면서 참여자에서 -1
# 참여자중 value가 1인 값 리턴

# [Counter 풀이]
# 두 리스트를 Counter 함수로 dic으로 전환
# 두 Counter 빼기 가능
# key하나 출력

input = sys.stdin.readline

def solution(participant, completion):
    dic_participant = {}
    dic_completion = {}

    for k in participant:
        if k not in dic_participant:
            dic_participant[k] = 1
        else:
            dic_participant[k] += 1

    for k in completion:
        if k not in dic_completion:
            dic_completion[k] = 1
        else:
            dic_completion[k] += 1    

    for k in dic_completion:
        if k in dic_participant:
            dic_participant[k] -= dic_completion[k]
    
    return max(dic_participant, key = dic_participant.get)


# 클린 코드
def solution(participant, completion):
    dic_participant = {}

    for k in participant:
        if k not in dic_participant:
            dic_participant[k] = 1
        else:
            dic_participant[k] += 1    

    for c in completion:
        dic_participant[c] -= 1

    for key in dic_participant:
        if dic_participant[key] > 0:
            return key
        
# Counter 함수 이용
from collections import Counter

def solution(participant, completion):
    dic_participant = Counter(participant)
    dic_completion = Counter(completion)

    answer = dic_participant - dic_completion

    return list(answer.keys())[0]
    

if __name__ == "__main__":
    solution( ["a", "a", "b", "b", "c"], ["a", "a", "b", "c"])