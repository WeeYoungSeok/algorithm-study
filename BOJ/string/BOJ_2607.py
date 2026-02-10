import sys

# [문제 링크]
# https://www.acmicpc.net/problem/2607

# [문제 정보]
# 분류 : BOJ 2607 : 비슷한 단어
# 난이도 : 실버 2

# [풀이 방법]
# 1. 기준 단어(첫 번째 단어)의 문자 구성을 딕셔너리(Map) 형태로 저장한다.
# 2. 비교할 단어들도 각각 딕셔너리로 변환
# 3. 두 단어 사이의 '교집합(공통된 문자)' 개수를 구함
#    - 기준 단어의 문자를 하나씩 확인하며 비교 단어에도 있는지 체크
#    - 둘 중 더 적은 개수만큼이 공통된 문자임 (min 함수와 같은 논리)
# 4. 판별 로직:
#    - (기준 단어 길이 - 교집합 개수) <= 1  AND
#    - (비교 단어 길이 - 교집합 개수) <= 1
#    - 위 두 조건이 모두 만족하면 '비슷한 단어'로 카운트


input = sys.stdin.readline

def list_to_dict(list):
    dict = {}

    for l in list:
        if l in dict:
            dict[l] += 1
        else:
            dict[l] = 1
    
    return dict

def solution():
    n = int(input())
    
    first_word_dict = list_to_dict(list(input().strip()))
    count = 0

    for _ in range(1, n):
        word = list(input().strip())
        word_dict = list_to_dict(word)
        same_count = 0

        for k, v in first_word_dict.items():
            if k in word_dict:
                # if word_dict[k] <= v:
                #     same_count += word_dict[k]
                # else:
                #     same_count += v
                same_count += min(word_dict[k], v)
        
        if sum(first_word_dict.values()) - same_count <= 1 and sum(word_dict.values()) - same_count <= 1:
            count += 1

    print(count)
    return

if __name__ == "__main__":
    solution()