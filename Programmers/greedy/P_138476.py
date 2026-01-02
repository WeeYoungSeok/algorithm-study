import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

# [문제 정보]
# 분류 : P 138476 : 귤 고르기
# 난이도 : LV 2

# [풀이 방법]
# 귤을 가장 많은 것부터 담아간다
# 남아있는 k보다 해당 귤이 많다면
# 무조건 다 채우고 나갈 수 있다
# 고로 가장 많은 귤부터 담고 다음 많은 귤을 담을때
# 만약 바구니보다 귤의 갯수가 많다면 그냥 개수만 +1 해주고
# k == 0 이라면 나오면 된다.
# else 부분에 break를 걸면 첫 if문에서 k가 0이 될 수도 있기 때문에
# 아래 걸어준다.

from collections import Counter

input = sys.stdin.readline

def solution(k, tangerine):
    tangerine_items = {}
    answer = 0
    for t in tangerine:
        if t not in tangerine_items.keys():
            tangerine_items[t] = 1
        else :
            tangerine_items[t] += 1

    tangerine_items = sorted(tangerine_items.items(), key=lambda x: x[1], reverse=True)
    for t in tangerine_items:
        if t[1] <= k:
            k -= t[1]
            answer += 1
        else:
            answer += 1
            k = 0
        if k == 0:
            break
    return answer

# 카운터 함수 이용하기
def solution(k, tangerine):
    answer = 0
    tangerine_count = Counter(tangerine)
    
    for v in sorted(tangerine_count.values(), reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer