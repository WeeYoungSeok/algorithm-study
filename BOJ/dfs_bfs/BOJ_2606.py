import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/2606

# [문제 정보]
# 분류 : BOJ 2606 : 바이러스
# 난이도 : 실버 3

# [풀이 방법]
# 컴퓨터와 연결되어있는 쌍을 그래프로 만들어 양쪽으로 이어줌
# 1번 컴퓨터부터 출발하므로 1번 컴퓨터를 초기화 해주며
# 1번 컴퓨터와 연결된 컴퓨터를 다시 queue or stack에 넣을때 방문 처리해주면서
# queue or stack에 넣어줌
# 마지막에 1번 컴퓨터를 제외한 바이러스가 걸린 컴퓨터의 개수를 출력

input = sys.stdin.readline

def solution_dfs():
    n = int(input())
    pair = int(input())
    computer = [[] for _ in range(n + 1)]
    result = [False] * (n + 1)
    result[1] = True

    for _ in range(pair):
        connect = list(map(int, input().split()))
        computer[connect[0]].append(connect[1])
        computer[connect[1]].append(connect[0])
    
    # virus = []
    # while computer[1]:
    #     com = computer[1].pop()
    #     virus.append(com)
    virus = [1]
    
    while virus:
        v = virus.pop()
        for com in computer[v]:
            if not result[com]:
                result[com] = True
                virus.append(com)

    return

def bfs(graphs, start, visited):    
    queue = deque([start])
    visited[start] = True
    while queue:
        computer = queue.popleft()
        for com in graphs[computer]:
            if not visited[com]:
                visited[com] = True
                queue.append(com)

    return visited.count(True) - 1 if visited.count(True) - 1 > 0 else 0



def solution_bfs():
    n = int(input())
    pair = int(input())

    computer = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for _ in range(pair):
        connect = list(map(int, input().split()))
        computer[connect[0]].append(connect[1])
        computer[connect[1]].append(connect[0])
    
    print(bfs(computer, 1, visited))
    return

if __name__ == "__main__":
    # solution_dfs()
    solution_bfs()