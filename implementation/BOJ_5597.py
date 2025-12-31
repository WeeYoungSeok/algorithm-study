import sys

# [문제 링크]
# https://www.acmicpc.net/problem/5597

# [문제 정보]
# 분류: 백준 5597번 : 과제 안 내신 분..?
# 난이도 : 브론즈3

# [풀이 방법]
# 1. 1 ~ 30번 학생의 번호를 미리 생성
# 2. 제출한 학생의 번호를 받아 1 ~ 30번 학생에 포함되어 있지 않는 번호만 출력

input = sys.stdin.readline

students = [i for i in range(1, 31)]
print(students)

submit_students = []

for num in range(28):
    submit_students.append(int(input()))

for r in students:
    if r not in submit_students:
        print(r)