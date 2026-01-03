import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/43105

# [문제 정보]
# 분류 : P 43105 : 정수 삼각형
# 난이도 : LV 3

# [풀이 방법]
# 2번째 줄의 삼각형부터 검사하면서 진행
# 해당 행의 왼쪽과 오른쪽 끝은 무조건 그 전 행의 양끝밖에 못 더함(분기 처리)
# 중간은 그 전 행의 양쪽이 있으므로 둘중 더한 값중 큰 값을 셋팅

input = sys.stdin.readline

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    
    return max(triangle[-1])

if __name__ == "__main__":
    solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])