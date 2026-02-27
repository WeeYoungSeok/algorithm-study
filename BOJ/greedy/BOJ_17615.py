import sys

# [문제 링크]
# 

# [문제 정보]
# 분류 : 
# 난이도 : 

# [풀이 방법]

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

def ultra_clean_solution():
    n = int(input())
    balls = input().strip()

    # 1. 전체 빨간 공과 파란 공의 개수를 미리 센다 (O(N))
    total_red = balls.count('R')
    total_blue = n - total_red # 전체에서 빨간 거 빼면 파란 거

    # 2. 왼쪽 끝에서 연속된 공의 개수 세기 (O(N)이지만 사실상 아주 짧음)
    left_count = 0
    for i in range(n):
        if balls[i] == balls[0]:
            left_count += 1
        else:
            break

    # 3. 오른쪽 끝에서 연속된 공의 개수 세기
    right_count = 0
    for i in range(n-1, -1, -1):
        if balls[i] == balls[-1]:
            right_count += 1
        else:
            break

    # 4. 4가지 케이스 계산
    # 빨간 공을 왼쪽으로: 전체 빨간 공 - (만약 왼쪽 끝이 빨간색이면 그 개수만큼 이득)
    res1 = total_red - (left_count if balls[0] == 'R' else 0)
    # 빨간 공을 오른쪽으로: 전체 빨간 공 - (만약 오른쪽 끝이 빨간색이면 그 개수만큼 이득)
    res2 = total_red - (right_count if balls[-1] == 'R' else 0)
    # 파란 공을 왼쪽으로
    res3 = total_blue - (left_count if balls[0] == 'B' else 0)
    # 파란 공을 오른쪽으로
    res4 = total_blue - (right_count if balls[-1] == 'B' else 0)

    print(min(res1, res2, res3, res4))


if __name__ == "__main__":
    # solution()
    clean_solution()
    ultra_clean_solution()