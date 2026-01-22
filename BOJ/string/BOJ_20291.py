import sys
from collections import defaultdict

# [문제 링크]
# https://www.acmicpc.net/problem/20291

# [문제 정보]
# 분류 : BOJ 20291 : 파일 정리
# 난이도 : 실버 3

# [풀이 방법]
# 확장자를 딕셔너리에 저장
# 키 값을 사전순으로 sort 후 출력

input = sys.stdin.readline

def solution():
    n = int(input())
    
    words = {}
    
    for _ in range(n):
        file_name, extension = input().strip().split(".")
        
        if extension in words:
            words[extension] += 1
        else:
            words[extension] = 1
        
    for key, value in sorted(words.items()):
        print(key, value)
    return

def solution_upgrade():
    n = int(input())
    words = defaultdict(int)
    
    for _ in range(n):
        extension = input().strip().split(".")[-1]
        words[extension] += 1
        
    for key, value in sorted(words.items()):
        print(key, value)
    return

if __name__ == "__main__":
    # solution()
    solution_upgrade()