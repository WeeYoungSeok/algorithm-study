import sys

# [문제 링크]
# https://www.acmicpc.net/problem/20006

# [문제 정보]
# 분류 : BOJ 20006 : 랭킹전 대기열
# 난이도 : 실버 2

# [풀이 방법]
# 방 배열을 생성 (rooms)
# 내부의 인덱스는 방의 번호이며 방의 번호 안의 구성은 [[level, name]...]으로 구성
# 플레이어를 순회하면서 방을 체크하여 자신이 들어갈 수 있는 방이라면 들어가고 들어갈 수 있는 방이 없다면 새로운 방 생성
# 방의 체크 기준은 방의 0번지(방장)의 레벨 -10 ~ +10 사이의 레벨만 입장 가능
# 순회가 끝난 후 방을 돌면서 정렬을 진행하고 꽉찬 방이면 출발
# 꽉찬 방이 아니라면 대기

input = sys.stdin.readline

def solution():
    p, m = map(int, input().split())

    player = []

    for _ in range(p):
        level, name = list(input().strip().split())
        player.append([int(level), name])
    
    rooms = []

    for level, name in player:
        new_room = True
        for room in rooms:
            if len(room) < m and level >= room[0][0] - 10 and level <= room[0][0] + 10:
                room.append([level, name])
                new_room = False
                break
        if new_room:
            rooms.append([[level, name]])
                
    for room in rooms:
        room.sort(key=lambda x : x[1])
        if len(room) == m:
            print("Started!")
        else:
            print("Waiting!")
        for level, name in room:
                print(level, name)
    return

if __name__ == "__main__":
    solution()