T = dict()

def knapsackWithOutRep(W, w, v, n):
    if (W, n) not in T:
        if n == 0:
            T[W, n] = 0
        else:
            T[W, n] = knapsackWithOutRep(W, w, v, n - 1)
            if W >= w[n - 1]:
                T[W, n] = max(T[W, n], knapsackWithOutRep(W - w[n - 1], w, v, n - 1) + v[n - 1])
    return T[W, n]



inFile = open('input.txt', 'r')
n, W = map(int, inFile.readline().split())
w = tuple(map(int, inFile.readline().split()))
v = tuple(map(int, inFile.readline().split()))
inFile.close()
result = knapsackWithOutRep(W, w, v, n)
print(result)
