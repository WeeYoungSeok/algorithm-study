import sys

# [문제 링크]
# https://www.acmicpc.net/problem/4659

# [문제 정보]
# 분류 : BOJ 4659 : 비밀번호 발음하기
# 난이도 : 실버 5

# [풀이 방법]
# 비밀번호 문자를 순회하면서 자음 연속, 모음 연속의 숫자를 초기화
# 이전 문자와 현재 문자가 같으면서 e, o가 아니라면 실패 문자
# 자음 연속 또는 모음 연속이 3번 일어났다면 실패 문자
# 모음이 하나도 없다면 실패 문자
# 마지막에 조건을 통해 출력

input = sys.stdin.readline

def solution():
    vowels = "aeiou"

    while True:
        password = input().strip()
        
        if password == "end":
            break

        consonant_cnt = 0
        vowel_cnt = 0
        prev_word = ""
        has_vowel = False
        is_acceptable = True
        
        for p in password:
            if p in vowels:
                consonant_cnt = 0
                vowel_cnt += 1
                has_vowel = True
            else:
                consonant_cnt += 1
                vowel_cnt = 0

            if prev_word == p:
                if p != "e" and p != "o":
                    is_acceptable = False
                    break    
            
            prev_word = p

            if consonant_cnt == 3 or vowel_cnt == 3:
                is_acceptable = False
                break

        if not has_vowel:
            is_acceptable = False

        if is_acceptable:
            print(f"<{password}> is acceptable.")
        else:
            print(f"<{password}> is not acceptable.")
    return

if __name__ == "__main__":
    solution()