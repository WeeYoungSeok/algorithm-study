import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1965

# [문제 정보]
# 분류 : BOJ 1965 : 상자넣기
# 난이도 : 실버 2

# [풀이 방법]
# dp 테이블을 1로 초기화 (각 상자 자신만 선택했을 때 최소 1개는 담을 수 있음)
# 이중 반복문을 돌며 현재 상자(i)와 이전 상자들(j)을 비교
# 현재 상자가 이전 상자보다 크다면(box[i] > box[j]), j번째 상자 뒤에 i를 붙이는 경우를 고려
# j번째 상자까지의 기록(dp[j])에 나를 추가(+1)한 값과 현재 내 기록(dp[i]) 중 최댓값을 저장
# 마지막 상자가 가장 긴 수열의 끝이라는 보장이 없으므로 전체 dp 리스트 중 max값을 출력

input = sys.stdin.readline

def solution():
    n = int(input())

    box = list(map(int, input().split()))
    dp = [1] * n

    for i in range(n):
        for j in range(i -1, -1, -1):
            if box[i] > box[j]:
                dp[i] = max(dp[j] + 1, dp[i])
     
    print(max(dp))
    return

if __name__ == "__main__":
    solution()