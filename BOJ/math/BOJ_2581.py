import sys
import math

# [문제 링크]
# https://www.acmicpc.net/problem/2581

# [문제 정보]
# 분류 : BOJ 2581 : 소수
# 난이도 : 브론즈 2

# [풀이 방법]
# 에라토스테네스의 체 알고리즘을 사용하여 소수를 판별
# N까지의 모든 수에 대해 소수 판별 배열(is_not_prime)을 생성하고 False로 초기화
# 0과 1은 소수가 아니므로 미리 True로 마킹
# 효율성을 위해 2부터 N의 제곱근(sqrt(N))까지만 반복하며 소수를 찾는다.
# 현재 수(i)가 소수라면(False), 자기 자신을 제외한 i의 배수들을 모두 소수가 아님(True)으로 변경
# 이때 range의 step 기능을 활용하여 배수 처리를 최적화
# M부터 N까지의 숫자 중 소수로 판별된(False) 수들을 리스트에 수집
# 수집된 소수가 없다면 -1을, 있다면 합계(sum)와 최솟값(min)을 출력

input = sys.stdin.readline

def solution():
    m = int(input())
    n = int(input())

    is_not_prime = [False] * (n + 1)
    
    is_not_prime[0] = True
    is_not_prime[1] = True

    for i in range(2, int(math.sqrt(n)) + 1):
        if not is_not_prime[i]:
            for j in range(i * 2, n + 1, i):
                is_not_prime[j] = True

    primes = []
    for i in range(m, n + 1):
        if not is_not_prime[i]:
            primes.append(i)
    
    if not primes:
        print("-1")
    else:
        print(sum(primes))
        print(min(primes))

if __name__ == "__main__":
    solution()