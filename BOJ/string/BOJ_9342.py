import sys
import re

# [문제 링크]
# https://www.acmicpc.net/problem/9342

# [문제 정보]
# 분류 : BOJ 9342 : 염색체
# 난이도 : 실버 3

# [풀이 방법]
# 파이썬 라이브러리중 re를 이용해 정규식 패턴 이용

input = sys.stdin.readline

def solution():
    t = int(input())
    
    pattern = re.compile('^[A-F]?A+F+C+[A-F]?$')

    for _ in range(t):
        word = input().strip()
        
        if pattern.fullmatch(word):
            print("Infected!")
        else:
            print("Good")

if __name__ == "__main__":
    solution()