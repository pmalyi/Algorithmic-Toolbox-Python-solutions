# Максимізація вартості наповненого рюкзака з повтореннями
# рекурсивне рішення з мемоїзацією
T = dict()


def knapsackWithRepRecurs(n, W, w, v) :
    if W not in T:
        T[W] = 0
        for i in range(len(w)):
            if w[i] <= W:
                T[W] = max(T[W], knapsackWithRepRecurs(n, (W - w[i]), w, v) + v[i])
    return T[W]


n, W = map(int, input().split())
w = tuple(map(int, input().split()))
v = tuple(map(int, input().split()))
res1 = knapsackWithRepRecurs(n, W, w, v)
print(f'${res1}')
# print(T)

