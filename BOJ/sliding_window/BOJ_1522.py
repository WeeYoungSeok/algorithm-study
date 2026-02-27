import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1522

# [문제 정보]
# 분류 : BOJ 1522 : 문자열 교환
# 난이도 : 실버 1

# [풀이 방법]
# 전체 a의 개수를 파악하여 윈도우의 크기를 결정함
# 원형 처리를 위해 문자열을 두 번 이어 붙여서 계산 범위를 확보함
# 모든 인덱스를 순회하며 윈도우 내의 b 개수를 세고 그중 최소값을 찾음

input = sys.stdin.readline

def solution():
    words = list(input().strip())
    result = 1001

    a_count = words.count("a")

    start = 0
    end = a_count
    is_end = False
    while start < len(words):
        if end == len(words) or is_end:
            if not is_end:
                end = 0
                is_end = True
            result = min(result, (words[start:] + words[:end]).count("b"))
            end += 1
            start += 1 
            continue
        else:
            result = min(words[start : end].count("b"), result)
        start += 1
        end += 1
        

    print(result)
    return

def clean_solution():
    words = list(input().strip())
    n = len(words)
    a_count = words.count("a")
    words = words + words[:a_count - 1]

    result = 1001

    for i in range(n):
        result = min(result, words[i:i + a_count].count("b"))
    
    print(result)

if __name__ == "__main__":
    # solution()
    clean_solution()