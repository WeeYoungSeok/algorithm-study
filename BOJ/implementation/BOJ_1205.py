import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1205

# [문제 정보]
# 분류 : BOJ 1205 : 등수 구하기
# 난이도 : 실버 4

# [풀이 방법]
# 자신보다 점수가 높은 인원을 추출
# 자신이랑 점수가 같은 인월을 추출
# 높은 인원 + 같은 인원이 p보다 크거나 같으면 자신이 들어갈 수 없으므로 -1
# 들어갈 수 있다면 높은 인원 + 1이 자기의 등수

input = sys.stdin.readline

def solution():
    n, score, p = map(int, input().split())

    over_person = 0
    scores = list(map(int, input().split()))
    same_person = scores.count(score)

    for s in scores:
        if s > score:
            over_person += 1
        elif s == score:
            break
    
    if over_person + same_person >= p:
        print(-1)
    else:
        print(over_person + 1)

    return

if __name__ == "__main__":
    solution()