import sys

# [문제 링크]
# https://www.acmicpc.net/problem/20125

# [문제 정보]
# 분류 : BOJ 20125 : 쿠키의 신체 측정
# 난이도 : 실버 4

# [풀이 방법]
# 심장을 먼저 찾음
# maps를 순회하면서 처음 *이 머리이므로 그것보다 한칸 아래가 심장
# 신체 사이즈를 담는 리스트 생성
# 문제에서 요구하는 신체부터 측정해가며 리스트의 숫자 +=1
# 출력 


input = sys.stdin.readline

def solution():
    n = int(input())

    maps = []
    
    for _ in range(n):
        maps.append(input().strip())
    
    heart_x = 0
    heart_y = 0
    
    bodies = [0, 0, 0, 0, 0]

    is_heart = False
    # 심장 찾기
    for i in range(n):
        for j in range(n):
            if maps[i][j] == "*":
                heart_x = i + 1
                heart_y = j
                is_heart = True
                break
        if is_heart:
            break

    # 왼팔
    for j in range(heart_y - 1, -1, -1):
        if maps[heart_x][j] == "*":
            bodies[0] += 1     

    # 오른팔
    for j in range(heart_y + 1, n):
        if maps[heart_x][j] == "*":
            bodies[1] += 1

    # 허리
    waist_end_x = 0
    for i in range(heart_x + 1, n):
        if maps[i][heart_y] == "*":
            bodies[2] += 1
            waist_end_x = i
    
    # 왼 다리
    for i in range(waist_end_x + 1, n):
        if maps[i][heart_y - 1] == "*":
            bodies[3] += 1
    
    # 오른 다리
    for i in range(waist_end_x + 1, n):
        if maps[i][heart_y + 1] == "*":
            bodies[4] += 1

    print(heart_x + 1, heart_y + 1)
    print(*bodies)
                 
    return

if __name__ == "__main__":
    solution()