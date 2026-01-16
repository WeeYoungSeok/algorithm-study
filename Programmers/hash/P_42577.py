import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# [문제 정보]
# 분류 : P 42577 : 전화번호 목록
# 난이도 : LV 2

# [풀이 방법]
# phone_book을 오름차순으로 sort
# 나와 바로 뒷사람만 검사해주면 됨
# in으로 할시에 포함 여부라 안됨
# 접두어는 앞에 포함되어있냐만 검사해야함


input = sys.stdin.readline

def solution(phone_book):
    answer = True

    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        # 파이썬의 기능
        if phone_book[i + 1].startswith(phone_book[i]):
        # if phone_book[i] in phone_book[i + 1][0:len(phone_book[i])]:
            answer = False
            break

    return answer

if __name__ == "__main__":
    solution(["123","456","789"])