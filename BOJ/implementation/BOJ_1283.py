import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1283

# [문제 정보]
# 분류 : BOJ 1283 : 단축키 지정
# 난이도 : 실버 1

# [풀이 방법]
# 단어의 첫 글자들을 먼저 순회하며 단축키 가능 여부를 확인함
# 첫 글자에서 실패할 경우, 전체 문자열을 인덱스 0부터 탐색하며 빈칸이 아닌 문자를 단축키로 지정함
# 단축키 지정 시 commands 셋에 추가하고 대괄호([]) 처리를 한 뒤 출력을 수행함


input = sys.stdin.readline

def solution():
    n = int(input())
    commands = set()
    options = []
    
    for _ in range(n):
        options.append(list(input().strip().split()))
    
    for option in options:
        is_first = False
        for i in range(len(option)):
            # 첫글자 다 확인
            if option[i][0].upper() not in commands:
                commands.add(option[i][0].upper())
                option[i] = "[" + option[i][0] + "]" + option[i][1:]
                is_first = True
                break
        if not is_first:
            # 한글자씩 두번째 글자부터 다 찾아
            is_option = False
            for i in range(len(option)):
                for j in range(1, len(option[i])):
                    if option[i][j].upper() not in commands:
                        commands.add(option[i][j].upper())
                        option[i] = option[i][:j] + "[" + option[i][j] + "]" + option[i][j + 1:]
                        is_option = True
                        break
                if is_option:
                    break
    
    for option in options:
        for o in option:
            print(o, end=" ")
        print()
    return

def clean_solution():
    n = int(input())
    commands = set()
    
    for _ in range(n):
        origin = input().strip()
        words = origin.split()
        is_assigned = False

        for i in range(len(words)):
            if words[i][0].upper() not in commands:
                commands.add(words[i][0].upper())
                words[i] = "[" + words[i][0] + "]" + words[i][1:]
                is_assigned = True
                break
        
        if not is_assigned:
            full_text = " ".join(words)
            for j in range(len(full_text)):
                if full_text[j] != " " and full_text[j].upper() not in commands:
                    commands.add(full_text[j].upper())
                    print(full_text[:j] + "[" + full_text[j] + "]" + full_text[j + 1:])
                    is_assigned = True
                    break
        
            if not is_assigned:
                print(full_text)
        else:
            print(" ".join(words))
    return

if __name__ == "__main__":
    # solution()
    clean_solution()