import sys

# [문제 링크]
# https://www.acmicpc.net/problem/1969

# [문제 정보]
# 분류 : BOJ 1969 : DNA
# 난이도 : 실버 4

# [풀이 방법]
# 문자를 세로로 하나씩 검사해줌
# dic에 저장
# 최댓값 value의 키를 사전순 가장 앞 저장
# 점수는 dic의 전체합 - dic의 제일 큰 value

input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())

    dna = []
    answer = []
    cnt = 0

    for _ in range(n):
        dna.append(input().strip())

    for i in range(m):
        word_cnt = {}
        for j in range(n):
            if dna[j][i] not in word_cnt:
                word_cnt[dna[j][i]] = 1
            else:
                word_cnt[dna[j][i]] += 1
        # 미리 최댓값을 구함
        max_val = max(word_cnt.values()) # 딱 한 번만 계산!
        words = [k for k,v in word_cnt.items() if v == max_val]

        # 나의 코드
        # words = [k for k,v in word_cnt.items() if max(word_cnt.values()) == v]
        
        words.sort()
        answer.append(words[0])
        # 더 간단한 코드
        cnt += n - max_val
        # 나의 코드 
        # cnt += sum(word_cnt.values()) - word_cnt[words[0]]
            

    print("".join(answer))
    print(cnt)
    return

if __name__ == "__main__":
    solution()