import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/64061

# [문제 정보]
# 분류 : P 64061 : 크레인 인형뽑기 게임
# 난이도 : LV 1

# [풀이 방법]
# 행과 열의 위치를 바꿔주는 zip 함수를 이용해 세로로 내려가는 어려움을 없앰
# moves를 순회하면서 해당 지점을 크레인으로 뽑을때 0이 아닌 구간까지 순회
# 0이 아닐 경우 바구니가 비어있다면 바로 넣어주고
# 바구니가 비어있지 않다면 바구니의 제일 위와 같다면 pop 이후 answer += 2
# 같지 않다면 바로 넣기

input = sys.stdin.readline

def solution(board, moves):
    answer = 0
    board = list(map(list, zip(*board)))
    basket = []

    for m in moves:
        for i in range(len(board[m - 1])):
            if board[m - 1][i] != 0:
                doll = board[m - 1][i]
                board[m - 1][i] = 0
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
                break
    return answer

if __name__ == "__main__":
    solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])