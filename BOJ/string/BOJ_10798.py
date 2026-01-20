import sys

# [문제 링크]
# https://www.acmicpc.net/problem/10798

# [문제 정보]
# 분류 : BOJ 10798 : 세로읽기
# 난이도 : 브론즈 1

# [풀이 방법]
# 문자열을 세로로 순회함
# 해당 인덱스가 자신의 최대 길이보다 작을때만 출력

input = sys.stdin.readline

def solution():
    words = []

    for _ in range(5):
        words.append(input().strip())

   

    for i in range(len(max(words, key=len))):
        for j in range(5):
            if i <= len(words[j]) -1:
                print(words[j][i], end="")
            else:
                continue

    return

if __name__ == "__main__":
    solution()