import sys

# [문제 링크]
# https://www.acmicpc.net/problem/2816

# [문제 정보]
# 분류 : BOJ 2816 : 디지털 티비
# 난이도 : 브론즈 1

# [풀이 방법]
# KBS1의 현재 위치(idx1)와 KBS2의 현재 위치(idx2)를 찾음
# KBS1을 맨 위로 올리는 과정에서 KBS2를 지나친다면 KBS2의 위치는 한 칸 밑으로 밀림
# 1번 버튼(내리기)으로 해당 채널까지 이동 후 4번 버튼(위로 스왑)으로 목표 지점까지 올림

input = sys.stdin.readline

def solution():
    n = int(input())
    channel = []

    for _ in range(n):
        channel.append(input().strip())
    
    result = []
    
    # KBS1을 먼저 최상단으로 올리기
    idx = 0
    while True:
        if channel[idx] == "KBS2":
            # KBS1 찾기
            kbs_one_idx = 0
            for i in range(idx + 1, n):
                if channel[i] == "KBS1":
                    kbs_one_idx = i
            # KBS2부터 올림 
            for _ in range(idx):
                result.append("4")
            # KBS1까지 내려감
            for _ in range(kbs_one_idx):
                result.append("1")
            # KBS1를 올림
            for _ in range(kbs_one_idx):
                result.append("4")
            break
        elif channel[idx] == "KBS1":
            kbs_two_idx = 0
            for i in range(idx + 1, n):
                if channel[i] == "KBS2":
                    kbs_two_idx = i
                    break
            # KBS1부터 올림
            for _ in range(idx):
                result.append("4")
            # KBS2까지 내려감
            for _ in range(kbs_two_idx):
                result.append("1")
            # KBS2를 올림
            for _ in range(kbs_two_idx - 1):
                result.append("4")
            break
        
        idx += 1
        result.append("1")
                
    
    print("".join(result))
    return

def clean_solution():
    n = int(input())
    channel = []

    for _ in range(n):
        channel.append(input().strip())

    idx1 = channel.index("KBS1")
    idx2 = channel.index('KBS2')

    if idx1 > idx2:
        idx2 += 1

    result = "1" * idx1 + "4" * idx1
    result += '1' * idx2 + '4' * (idx2 - 1)    

    print(result)

if __name__ == "__main__":
    # solution()
    clean_solution()