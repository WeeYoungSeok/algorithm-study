import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1244

# [문제 정보]
# 분류 : BOJ 1244 : 스위치 켜고 끄기
# 난이도 : 실버 4

# [풀이 방법]
# 남학생일 경우에는 받은 숫자만큼 건너 뛰면서 바꿔줌
# 여학생일 경우 양옆을 검사하면서 조건이 안맞을때까지 퍼져나감
# while문을 나왔을 떄 무조건 한칸씩 퍼져나갔으므로 다시 줄여줌
# 그 사이를 전부 뒤집어서 바꿈
# 20씩 찍으면서 줄바꿈 출력

input = sys.stdin.readline

def solution():
    n = int(input())

    switch = list(map(int, input().split()))

    t = int(input())

    for _ in range(t):
        gender, num = map(int, input().split())
        num -= 1

        if gender == 1:
            for i in range(num, len(switch), num + 1):
                switch[i] ^= 1
        else:
            left_idx = num - 1
            right_idx = num + 1

            while left_idx >= 0 and right_idx < len(switch):
                if switch[left_idx] != switch[right_idx]:
                    break
                left_idx -= 1
                right_idx += 1
            
            left_idx += 1
            right_idx -= 1

            for i in range(left_idx, right_idx + 1):
                switch[i] ^= 1
    
    for i in range(len(switch)):
        print(switch[i], end=" ")
        if (i + 1) % 20 == 0:
            print()

    return

if __name__ == "__main__":
    solution()