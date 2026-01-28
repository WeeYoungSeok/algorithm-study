import sys

# [문제 링크]
# https://www.acmicpc.net/problem/25757

# [문제 정보]
# 분류 : BOJ 25757 : 임스와 함께하는 미니게임
# 난이도 : 실버 5

# [풀이 방법]
# set으로 중복 사람 제거
# 중복 제거된 사람 수 // 필요 인원 출력

input = sys.stdin.readline

def solution():
    n, game = map(str, input().strip().split())

    people = set()

    for _ in range(int(n)):
        people.add(input().strip())

    if game == "Y":
        print(len(people))
    elif game == "F":
        print(len(people) // 2)
    else:
        print(len(people) // 3)
    
    return

if __name__ == "__main__":
    solution()