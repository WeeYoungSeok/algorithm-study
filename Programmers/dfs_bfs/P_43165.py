import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# [문제 정보]
# 분류 : P 43615 : 타겟 넘버
# 난이도 : LV 2

# [풀이 방법]
# 현재 index의 숫자를 +, -로 갈림길을 나눈다
# 다음 숫자와 +, -를 재귀적으로 호출한다.
# 마지막 숫자까지 다 검사해봤으면
# target과 같은지 확인한다.

input = sys.stdin.readline

def solution(numbers, target):

    def dfs(now_num, index):
        # 인덱스가 넘쳤다면
        if index == len(numbers):
            # 현재 숫자와 타겟 숫자가 같다면
            if now_num == target:
                return 1
            else:
                return 0
                
        else:
            return dfs(now_num + numbers[index], index + 1, target) + dfs(now_num - numbers[index], index + 1, target)     
    
    return dfs(0, 0)