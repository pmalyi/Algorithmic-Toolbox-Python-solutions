from random import randint
from max_pairwise_product_naive import maxPairwiseProductNaive
from max_pairwise_product_fast import maxPairwiseProductFast


def stressTest(size, max_number):
    while True:
        n = randint(0, 2 ** 31) % size + 2
        print(n)
        testList = [randint(0, 2 ** 32) % max_number for _ in range(n)]
        print(*testList)
        res1 = maxPairwiseProductNaive(testList)
        res2 = maxPairwiseProductFast(testList)
        if res1 != res2:
            print("Wrong answer", res1, res2)
            break
        else:
            print(res1, res2)
            print("OK")

size_array = int(input())
max_number = int(input())
stressTest(size_array, max_number)
