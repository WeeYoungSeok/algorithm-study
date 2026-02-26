import sys
from collections import defaultdict

# [문제 링크]
# https://www.acmicpc.net/problem/20922

# [문제 정보]
# 분류 : BOJ 20922 : 겹치는 건 싫어
# 난이도 : 실버 1

# [풀이 방법]
# 두 개의 포인터(start, end)를 사용하여 구간을 관리
# end를 늘리며 숫자의 개수를 세고 특정 숫자가 K개를 넘으면 start를 밀어서 구간을 조정
# 모든 과정을 한 번의 순회(O(N))로 끝내 효율성을 확보

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))

    max_len = 0
    duple_num = defaultdict(int)

    start = 0
    end = 0

    while end < n:
        if duple_num[seq[end]] + 1 > k:
            duple_num[seq[start]] -= 1
            start += 1
        else:
            duple_num[seq[end]] += 1
            max_len = max(max_len, end - start + 1)
            end += 1
    
    print(max_len)
    return

if __name__ == "__main__":
    solution()