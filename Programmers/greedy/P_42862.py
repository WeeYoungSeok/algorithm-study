import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# [문제 정보]
# 분류 : P 42862 : 체육복
# 난이도 : LV 1

# [풀이 방법]
# 여분이 있는 사람이 체육복을 잃어버릴 수 있는 특수 조건을 위해
# 요소를 서로의 리스트에서 제거
# 여분이 있는 사람이 앞번호부터 빌려줘야 최대한 많이 빌려줄 수 있음
# 잃어버린 사람 1, 3 여분있는 사람 2, 4
# 이렇게 될때 2번이 3번한테 빌려주게 되면 1번은 2번한테 빌릴 수 없음

input = sys.stdin.readline

def solution(n, lost, reserve):
    answer = n

    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))
    
    real_lost.sort()
    real_reserve.sort()
    
    for r in real_reserve:
        if r - 1 in real_lost:
            real_lost.remove(r - 1)
        elif r + 1 in real_lost:
            real_lost.remove(r + 1)
    return answer - len(real_lost)