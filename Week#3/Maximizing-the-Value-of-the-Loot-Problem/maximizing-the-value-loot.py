# Максимізація вартості наповненого рюкзака
def costSort(prises):
   sortIndexes = [(prises[i], i) for i in range(len(prises))]
   sortIndexes.sort(reverse=True)
   for i in range(len(sortIndexes)):
       sortIndexes[i] = sortIndexes[i][1]
   return sortIndexes


def maximumLoot(W, Weight, Cost, sortIndexes):
    if W == 0 or len(Weight) == 0 or len(sortIndexes) == 0:
        return 0
    m = sortIndexes[0]
    amount = min(Weight[m], W)
    value = Cost[m] * amount / Weight[m]
    W -= amount
    sortIndexes.remove(m)
    return value + maximumLoot(W, Weight, Cost, sortIndexes)


n, W = map(int, input().split())
Weight = []
Cost = []
for i in range(n):
    c, w = map(int, input().split())
    Cost.append(c)
    Weight.append(w)
prices = [Cost[i] / Weight[i] for i in range(len(Cost))]
sortIndexes = costSort(prices)
result = maximumLoot(W, Weight, Cost, sortIndexes)
print(f'{result:.4f}')
