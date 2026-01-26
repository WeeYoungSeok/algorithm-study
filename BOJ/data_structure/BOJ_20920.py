import sys
from collections import defaultdict

# [문제 링크]
# https://www.acmicpc.net/problem/20920

# [문제 정보]
# 분류 : BOJ 20920 : 영단어 암기는 괴로워
# 난이도 : 실버 3

# [풀이 방법]
# 딕셔너리에 4글자 이상만 저장
# 정렬 lambda를 이용해 내림차순, 길이, 사전순으로 정렬

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())

    words = defaultdict(int)

    for _ in range(n):
        word = input().strip()

        if len(word) >= m:
            words[word] += 1

    for k, v in sorted(words.items(), key=lambda x : (-x[1], -len(x[0]), x[0])):
        print(k)
    return

if __name__ == "__main__":
    solution()