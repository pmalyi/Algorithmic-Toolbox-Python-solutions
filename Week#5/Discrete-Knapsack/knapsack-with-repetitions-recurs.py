# Максимізація вартості наповненого рюкзака з повтореннями
# рекурсивне рішення
def knapsackWithRepRecurs(n, W, w, v) :
    if W == 0:
        return 0
    result = 0
    for i in range(len(w)):
        if w[i] <= W:
            result = max(result, knapsackWithRepRecurs(n, (W - w[i]), w, v) + v[i])
    return result


n, W = map(int, input().split())
w = tuple(map(int, input().split()))
v = tuple(map(int, input().split()))
res1 = knapsackWithRepRecurs(n, W, w, v)
print(f'${res1}')