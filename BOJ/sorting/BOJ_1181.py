import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1181

# [문제 정보]
# 분류 : BOJ 1181 : 단어 정렬
# 난이도 : 실버 5

# [풀이 방법]
# 중복되지 않게 단어를 set으로 입력 받음
# list로 전환 후 sort의 lambda를 이용하여 길이순, 길이가 같다면 사전순으로 정렬
# 출력

input = sys.stdin.readline

def solution():
    n = int(input())

    words = set()

    for _ in range(n):
        words.add(input().strip())
    
    words = list(words)
    words.sort(key=lambda x:(len(x), x))
    print("\n".join(words))
    return

if __name__ == "__main__":
    solution()