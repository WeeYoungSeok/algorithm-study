import sys
from collections import defaultdict

# [문제 링크]
# 

# [문제 정보]
# 분류 : 
# 난이도 : 

# [풀이 방법]

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