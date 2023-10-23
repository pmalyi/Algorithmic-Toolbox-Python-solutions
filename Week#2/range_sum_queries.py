from itertools import accumulate
def prefixSum(A):
    '''n = len(A)
    item = 0
    prefix = []
    for i in range(n):
        item += A[i]
        prefix.append(item)'''
    prefix = list(accumulate(A, lambda a, b: a + b))
    return prefix


def rangeSumQueries(A, l, r):
    return prefixSum(A)[r] - prefixSum(A)[l - 1]


myList = list(map(int, '10 9 7 20 14 23 14 27 38 77'.split()))
queries = ['8 9', '7 9', '6 9', '5 9', '4 9']
for query in queries:
    l, r = map(int, query.split())
    print(rangeSumQueries(myList, l, r))
