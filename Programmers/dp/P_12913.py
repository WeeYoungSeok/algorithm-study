import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/12913

# [문제 정보]
# 분류 : P 12931 : 땅따먹기
# 난이도 : LV 2

# [풀이 방법]
# dp 테이블을 land와 똑같게 만든다.
# dp의 첫 줄을 land와 같게 만든다.
# 마지막 행을 제외하면서 돈다.
# 해당 전 행의 열을 검사하면서 자신의 열과 같지 않다면 dp에 저장할때
# 최대값을 저장한다.
# 이 방법은 엄~~~~~청 비효율적임 O(n) x 4 x 4임
# 굳이 저렇게 안하고 밑에 O(n) X 4 방법이 훨씬 효율적이다.

input = sys.stdin.readline

# O(n) X 4 X 4 
# def solution(land):
#     dp = []

#     for _ in land:
#         inner = [0] * len(land[0])
#         dp.append(inner)
#     dp[0] = land[0]

#     for i in range(len(land) - 1):
#         for j in range(len(land[i])):
#             for k in range(len(land[i])):
#                 if j != k:
#                     # 해당방법 처럼 바꿀수 있음
#                     # dp[i + 1][k] = max(dp[i + 1][k], land[i + 1][k] + dp[i][j])
#                     if dp[i + 1][k] < land[i + 1][k] + dp[i][j]:
#                         dp[i + 1][k] = land[i + 1][k] + dp[i][j]
                        
    
#     return max(dp[-1])

# O(n) X 4 방식
def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    return max(land[-1])

if __name__ == "__main__":
    solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])