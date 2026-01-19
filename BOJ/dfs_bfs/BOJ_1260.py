import sys
from collections import deque

# [문제 링크]
# https://www.acmicpc.net/problem/1260

# [문제 정보]
# 분류 : BOJ 1260 : DFS와 BFS
# 난이도 : 실버 2

# [풀이 방법]
# 정점이 여러개인 경우에 작은 것부터 방문이므로 처음에 sort를 진행
# BFS는 그대로 풀면 원래 값이 나오지만 DFS는 다시 reversed를 진행 해주어야함
# 방문 순서대로 출력

input = sys.stdin.readline

def dfs_recursive(graphs, v, visited):
    visited[v] = True
    print(v, end=" ")
    
    # 그래프는 이미 sort() 되어 있으니, 순서대로 부르기만 하면 됨
    for g in graphs[v]:
        if not visited[g]:
            dfs_recursive(graphs, g, visited)
    return


def dfs(graphs, v, visited):
    stack = [v]
    while stack:
        c = stack.pop()
        if not visited[c]:
            visited[c] = True
            print(c, end = " ")
        for g in reversed(graphs[c]):
            if not visited[g]:
                stack.append(g)
    return

    # for g in graphs[v]:
        # if not visited[g]:
            # dfs(graphs, g, visited)

def bfs(graphs, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        c = queue.popleft()
        print(c, end = " ")
        for g in graphs[c]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)

    return


def solution():
    n, m, v = map(int, input().split())
    
    graphs = [[] for _ in range(n + 1)]

    for _ in range(m):
        connect = list(map(int, input().split()))
        graphs[connect[0]].append(connect[1])
        graphs[connect[1]].append(connect[0])

    for g in graphs:
        g.sort()
    

    visited_dfs = [False] * (n + 1)
    visited_bfs = [False] * (n + 1)
    dfs(graphs, v, visited_dfs)
    # dfs_recursive(graphs, v, visited_dfs)
    print()
    bfs(graphs, v, visited_bfs)
    
    return

if __name__ == "__main__":
    solution()