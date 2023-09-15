# https://academy.yandex.ru/handbook/algorithms/article/zadacha-para-blizhajshih-tochek
from math import sqrt
def distance(p1, p2):
    return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])


def getMinDistance(Points, low, high):
    if high - low == 1:
        return distance(Points[low], Points[high])
    if high - low == 2:
        d1 = distance(Points[low], Points[low + 1])
        d2 = distance(Points[low + 1], Points[high])
        d3 = distance(Points[low], Points[high])
        return min(d1, d2, d3)
    mid = low + (high - low) // 2
    dist1 = getMinDistance(Points, low, mid)
    dist2 = getMinDistance(Points, mid + 1, high)
    dist = min(dist1, dist2)
    '''left = mid
    right = mid
    while left >= low:
        if Points[mid][0] - Points[left][0] - sqrt(dist) < 0.001:
            left -= 1
        else:
            break
    while right <= high:
        if Points[right][0] - Points[mid][0] - sqrt(dist) < 0.001:
            right += 1
        else:
            break
    Strip = Points[left:right]'''
    Strip = Points[low:high]
    Strip.sort(key=lambda X: X[1])
    for p in range(len(Strip) - 1):
        q = p + 1
        step = 0
        while q < len(Strip) and step < 7:
            cur_dist = distance(Strip[p], Strip[q])
            dist = min(dist, cur_dist)
            q += 1
            step += 1
    return dist


n = int(input())
points = [tuple(map(int, input().split())) for i in range(n)]
'''with open('input.txt', 'r', encoding='utf-8') as inF:
    n = int(inF.readline())
    points = [tuple(map(int, inF.readline().split())) for i in range(n)]'''
points.sort()
res = sqrt(getMinDistance(points, 0, n - 1))
print(res)
