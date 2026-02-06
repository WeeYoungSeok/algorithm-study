import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1515

# [문제 정보]
# 분류 : BOJ 1515 : 수 이어 쓰기
# 난이도 : 실버 2

# [풀이 방법]
# n을 증가시키면서 n을 인덱스 0부터 순회하면서 num의 포인터 위치에 있는 숫자랑 일치하는지 검사
# 일치한다면 num의 포인터를 증가
# num의 포인터가 끝 인덱스에 위치할떄 n이 최소값

input = sys.stdin.readline

def solution():
    num = input().strip()
    n = 0
    idx = 0

    while idx < len(num):
        n += 1

        str_n = str(n)
        
        for s in str_n:
            if s == num[idx]:
                idx += 1
            if idx >= len(num):
                break
    
    print(n)
    return

if __name__ == "__main__":
    solution()