import sys

# [문제 링크]
# https://www.acmicpc.net/problem/15721

# [문제 정보]
# 분류 : BOJ 15721 : 번데기
# 난이도 : 실버 5

# [풀이 방법]
# 번데기 게임의 회차 리스트를 만듦
# 해당 회차 게임을 돌면서 뻔, 데기의 카운터를 올려줌
# target과 뻔 or 데기의 카운터가 t와 같다면 해당 사람이 정답
# 해당 번째 사람은 번째 % 사람의 수
# 만약 찾기 못했다면 게임을 다음회차로 바꿈

input = sys.stdin.readline

'''
def solution():
    a = int(input())
    t = int(input())
    pu_pa = int(input())
    pu_or_pa = "뻔" if pu_pa == 0 else "데기"
    turn = 2
    turn_check_a = 0

    preix_game = ["뻔", "데기", "뻔", "데기"]
    turn_suffix_game_pu = ["뻔"] * turn
    turn_suffix_game_pa = ["데기"] * turn

    game = preix_game + turn_suffix_game_pu + turn_suffix_game_pa
    start_game_index = 0
    end_game_index = len(preix_game + turn_suffix_game_pu + turn_suffix_game_pa)

    while t > 0:
        # 찾았다면
        if pu_or_pa == game[start_game_index]:
            t -= 1
            if t == 0:
                break

        turn_check_a += 1
        start_game_index += 1

        if start_game_index == end_game_index:
            start_game_index = 0
            turn += 1
            turn_suffix_game_pu = ["뻔"] * turn
            turn_suffix_game_pa = ["데기"] * turn
            game = preix_game + turn_suffix_game_pu + turn_suffix_game_pa
            end_game_index = len(preix_game + turn_suffix_game_pu + turn_suffix_game_pa)

        # 끝사람까지 다돌았다면
        if turn_check_a == a:
            turn_check_a = 0
    print(turn_check_a)
    return
'''

# 클린 + 최적화 코드
def solution_clean():
    a = int(input())
    t = int(input())
    target = int(input())
    
    cnt_bun = 0
    cnt_degi = 0

    total_turn = 0

    n = 2

    while True:
        current_round = [0, 1, 0, 1] + [0] * n + [1] * n

        for code in current_round:
            if code == 0:
                cnt_bun += 1
            else:
                cnt_degi += 1

            if code == target:
                if (target == 0 and cnt_bun == t) or (target == 1 and cnt_degi == t):
                    print(total_turn % a) # 전체 턴 % 사람 수 = 현재 사람 번호
                    return
            
            total_turn += 1
        
        n += 1

if __name__ == "__main__":
    # solution()
    solution_clean()