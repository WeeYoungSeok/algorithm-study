import sys

# [문제 링크]
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

# [문제 정보]
# 분류 : P 12906 : 같은 숫자는 싫어
# 난이도 : LV 1

# [풀이 방법]
# 나의 풀이
# 큐를 이용해서 arr을 큐로 만들어 왼쪽부터 꺼낸다
# 제일 처음에 arr이 비어있으면 에러가 난다..
# 만약 빈 배열이 아니라면 해당 코드대로 왼쪽부터 꺼내서
# 가장 마지막에 answer에 들어간 값이랑 다르면 넣고 같다면 넣지 않는다

# 클린 코드 풀이
# 큐를 사용할 필요도 없이 리스트에서 꺼내
# answer가 비어잇다면 바로 넣고 비어있지 않은데 마지막 요소랑 다르다면 넣어준다.

from collections import deque

input = sys.stdin.readline

def solution(arr):
    answer = []
    queue = deque(arr)
    # 여기서 예외 발생 가능성 있음
    answer.append(queue.popleft())
    while queue:
        num = queue.popleft()
        if num != answer[-1]:
            answer.append(num)
    return answer

# 굳이 queue를 안써도 되는 코드
def solution(arr):
    answer = []
    for num in arr:
        # 1. 바구니가 비어있으면 무조건 넣기
        # 2. 바구니 맨 위(answer[-1])랑 지금 숫자(num)가 다르면 넣기
        if len(answer) == 0 or answer[-1] != num:
            answer.append(num)
    return answer

if __name__ == "__main__":
    solution([1,1,3,3,0,1,1])

