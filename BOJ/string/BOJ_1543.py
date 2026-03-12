import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1543

# [문제 정보]
# 분류 : BOJ 1543 : 문서 검색
# 난이도 : 실버 5

# [풀이 방법]
# 파이썬의 str.replace()가 왼쪽부터 중복되지 않게 문자열을 처리한다는 점을 활용
# 전체 길이에서 검색어를 모두 제거한 길이를 뺀 뒤, 검색어의 길이로 나누어 개수를 구함

input = sys.stdin.readline

def solution():
    docu = input().strip()
    search_word = input().strip()

    if len(search_word) > len(docu):
        print(0)
        return
    
    print((len(docu) - len(docu.replace(search_word, ""))) // len(search_word))
    return

def solution_count():
    docu = input().strip()
    search_word = input().strip()

    if len(search_word) > len(docu):
        print(0)
        return
    
    print(docu.count(search_word))


def solution2():
    docu = input().strip()
    word = input().strip()
    
    count = 0
    idx = 0
    
    while True:
        # idx 위치부터 word가 어디 있는지 찾음
        found = docu.find(word, idx)
        
        if found == -1: # 더 이상 없으면 탈출
            break
            
        count += 1
        # 찾은 위치 + 단어 길이만큼 점프 (중복 방지 핵심)
        idx = found + len(word)
        
    print(count)

if __name__ == "__main__":
    solution()
    solution_count()
    # solution2()