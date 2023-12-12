import sys
import random


def max_pairwise_product(n, a):
    first = max(a)
    a.remove(first)
    second = max(a)

    return first*second

# def stress_test(n, a):
#     while True:
#         n = random.uniform(2, 12)
#         a = [random.uniform(1, 1000) for _ in range(n)]
        

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))

    # passed = stress_test(n, a)
    max_product = max_pairwise_product(n, a)
    print(max_product)

main()