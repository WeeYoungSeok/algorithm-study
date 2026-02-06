import sys

# [문제 링크]
# 

# [문제 정보]
# 분류 : 
# 난이도 : 

# [풀이 방법]

input = sys.stdin.readline

def solution():
    num = input().strip()

    n = 0
    idx = 0

    while idx < len(num):
        n += 1
        
        for i in range(len(str(n))):
            if str(n)[i] == num[idx]:
                idx += 1
            if idx >= len(num):
                break
    
    print(n)
    return

if __name__ == "__main__":
    solution()