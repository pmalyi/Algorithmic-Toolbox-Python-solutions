from random import randint
from time import time
from max_pairwise_product_naive import maxPairwiseProductNaive
from max_pairwise_product_fast import maxPairwiseProductFast


def stressTest(size, max_number):
    while True:
        n = randint(0, 2 ** 31) % size + 2
        print(n)
        testList = [randint(0, 2 ** 32) % max_number for _ in range(n)]
        print(*testList)
        start_naive = time()
        res1 = maxPairwiseProductNaive(testList)
        end_naive = time()
        rtn = float(end_naive - start_naive)
        print(f"Run time naive = {rtn:.15f} sec")
        start_fast = time()
        res2 = maxPairwiseProductFast(testList)
        end_fast = time()
        rtf = float(end_fast - start_fast)
        print(f"Run time fast  = {rtf:.15f} sec")
        if res1 != res2:
            print("Wrong answer", res1, res2)
            break
        else:
            print(res1, res2)
            print("OK")

size_array = int(input())
max_number = int(input())
stressTest(size_array, max_number)
