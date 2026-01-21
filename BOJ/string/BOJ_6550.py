import sys

# [문제 링크]
# https://www.acmicpc.net/problem/6550

# [문제 정보]
# 분류 : BOJ 6550 : 부분 문자열
# 난이도 : 실버 5

# [풀이 방법]
# s를 처음부터 순회함
# t를 내부에서 돌면서 s의 문자와 만난다면 count를 -해주고 t의 인덱스를 하나 증가한 위치 저장
# 다시 거기서부터 s의 다음 문제를 내부에서 인덱스가 증가된 값으로 t를 순회
# 전부 다 찾았다면 Yes 그렇지 않다면 No

input = sys.stdin.readline

def solution():
    
    while True:
        try:
            line = input().strip()
            if not line:
                break
            s, t = map(str, line.split())
            s_len = len(s)
            t_start = 0
            for i in range(len(s)):
                for j in range(t_start, len(t)):
                    if s[i] == t[j]:
                        s_len -= 1
                        t_start = j + 1
                        break
            if s_len == 0:
                print("Yes")
            else:
                print("No")

        except:
            break
    return

if __name__ == "__main__":
    solution()