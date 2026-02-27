import sys

# [문제 링크]
# https://www.acmicpc.net/problem/17615

# [문제 정보]
# 분류 : BOJ 17615 : 볼 모으기
# 난이도 : 실버 1

# [풀이 방법]
# 공을 옮기는 과정이 아닌 최종 결과 상태에 집중함.
# 목표 방향 끝에 이미 붙어 있는 같은 색 공들은 이동 대상에서 제외함.
# lstrip/rstrip을 사용하여 정렬된 공을 지우고 남은 공의 개수를 세어 최소값을 반환함.

input = sys.stdin.readline

def solution():
    n = int(input())
    balls = list(input().strip())

    min_count = n + 1

    # 빨간, 파란 공을 왼쪽에서부터 왼쪽으로 전부 옮기기
    red_count = 0
    blue_count = 0
    is_blue = False
    is_red = False
    for i in range(len(balls)):
        if balls[i] == "B" and not is_blue:
            is_blue = True
        elif is_blue and balls[i] == "R":
            red_count += 1
        
        if balls[i] == "R" and not is_red:
            is_red = True
        elif is_red and balls[i] == "B":
            blue_count += 1
    min_count = min(red_count, blue_count, min_count)

    # 빨간, 파란 공을 오른쪽에서부터 오른쪽으로 전부 옮기기
    red_count = 0
    blue_count = 0
    is_blue = False
    is_red = False
    for i in range(len(balls) -1, -1, -1):
        if balls[i] == "B" and not is_blue:
            is_blue = True
        elif is_blue and balls[i] == "R":
            red_count += 1

        if balls[i] == "R" and not is_red:
            is_red = True
        elif is_red and balls[i] == "B":
            blue_count += 1
    min_count = min(red_count, blue_count, min_count)

    print(min_count)
    return

def clean_solution():
    n = int(input())
    balls = input().strip()

    min_count = n + 1

    min_count = min(
        min_count, 
        balls.lstrip("R").count("R"), 
        balls.lstrip("B").count("B"), 
        balls.rstrip("R").count("R"), 
        balls.rstrip("B").count("B")
        )
    
    print(min_count)
    return



if __name__ == "__main__":
    # solution()
    clean_solution()