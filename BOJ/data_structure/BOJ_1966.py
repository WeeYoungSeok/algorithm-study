import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1966

# [문제 정보]
# 분류 : BOJ 1966 : 프린터 큐
# 난이도 : 실버 3

# [풀이 방법]
# deque를 이용
# deque에 데이터를 입력할때 ([중요도, 인덱스]..)로 저장
# deque를 하나씩 조회하면서 max값보다 작다면 맨 뒤로 보냄
# max값보다 크거나 같다면 pop
# pop된 값에서 인덱스가 m과 같다면 break
# 다르다면 result += 1

from collections import deque

input = sys.stdin.readline

def solution():
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        docu_list = list(map(int, input().split()))
        docu_queue = deque()
        result = 0

        for i in range(len(docu_list)):
            docu_queue.append((docu_list[i], i))

        while docu_queue:
            docu = docu_queue.popleft()
            if not docu_queue: # 큐가 비어버리면 max()에서 에러 나니까 방어!
                result += 1
                break
            if max(docu_queue)[0] > docu[0]:
                docu_queue.append(docu)
            else:
                result += 1
                if docu[1] == m:
                    break
        print(result) 
         
    return

if __name__ == "__main__":
    solution()