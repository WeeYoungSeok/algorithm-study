import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1316

# [문제 정보]
# 분류 : BOJ 1316 : 그룹 단어 체커
# 난이도 : 실버 5

# [풀이 방법]
# 글자를 순회하면서 현재 글자보다 뒤에 글자들을 검사
# 뒤에 글자(j)중 현재 글자(i)와 같다면
# 뒤에 글자 바로 이전 글자(j - 1)이 현재 글자(i)와 다르다면 끊김

# [풀이 방법 slicing]
# 글자를 마지막 인덱스 전까지 순회
# 현재 글자와 다음 글자가 다르다면 다음 글자부터 끝 인덱스까지
# 현재 글자가 포함되어있다면 그룹 단어가 아님

input = sys.stdin.readline

def solution():
    n = int(input())

    cnt = n
    for _ in range(n):
        word = input().strip()
        checker = True
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                if word[i] == word[j]:
                    if word[j - 1] != word[i]:
                        checker = False
                        break
            if not checker:
                cnt -= 1
                break
                
    print(cnt)
    return

def solution_slicing():
    n = int(input())
    cnt = n  

    for _ in range(n):
        word = input().strip()
        for i in range(len(word) - 1):
            if word[i] != word[i + 1]:
                if word[i] in word[i + 1:]:
                    cnt -= 1
                    break
    
    print(cnt)

if __name__ == "__main__":
    # solution()
    solution_slicing()