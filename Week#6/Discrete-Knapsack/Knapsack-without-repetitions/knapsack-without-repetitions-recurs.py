def knapsackWithOutRep(W, w, v, n):
    if n == 0:
        return 0
    case1 = knapsackWithOutRep(W, w, v, n - 1)
    case2 = 0
    if w[n - 1] <= W:
        case2 = knapsackWithOutRep(W - w[n - 1], w, v, n - 1) + v[n - 1]
    return max(case1, case2)



inFile = open('input.txt', 'r')
n, W = map(int, inFile.readline().split())
w = tuple(map(int, inFile.readline().split()))
v = tuple(map(int, inFile.readline().split()))
inFile.close()
result = knapsackWithOutRep(W, w, v, n)
print(result)
