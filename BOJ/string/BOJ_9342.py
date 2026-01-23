import sys
import re

# [문제 링크]
# https://www.acmicpc.net/problem/9342

# [문제 정보]
# 분류 : BOJ 9342 : 염색체
# 난이도 : 실버 3

# [풀이 방법]
# 파이썬 라이브러리중 re를 이용해 정규식 패턴 이용

# [풀이 방법]
# 문제에 조건에 맞게 첫 부분부터 차례대로 조건을 추가해 출력

input = sys.stdin.readline

def solution_regx():
    t = int(input())
    
    pattern = re.compile("^[A-F]?A+F+C+[A-F]?$")

    for _ in range(t):
        word = input().strip()
        
        if pattern.fullmatch(word):
            print("Infected!")
        else:
            print("Good")

def solution():
    t = int(input())
    valid_chars = set("ABCDEF")

    for _ in range(t):
        word = input().strip()
        
        if set(word) - valid_chars:
            print("Good")
            continue

        n = len(word)
        idx = 0

        if idx < n and word[idx] != "A":
            idx += 1
        
        if idx >= n or word[idx] != "A":
            print("Good")
            continue

        while idx < n and word[idx] == "A":
            idx += 1

        if idx >= n or word[idx] != "F":
            print("Good")
            continue

        while idx < n and word[idx] == "F":
            idx += 1

        if idx >= n or word[idx] != "C":
            print("Good")
            continue

        while idx < n and word[idx] == "C":
            idx += 1
            
        if idx == n:
            print("Infected!")
        elif idx == n - 1:
            print("Infected!")
        else:
            print("Good")

if __name__ == "__main__":
    solution()
    # solution_regx()