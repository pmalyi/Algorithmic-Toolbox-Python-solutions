def JosephusIter(n, k):
    person = 0
    for count in range(1, n + 1):
        person = (person + k) % count
    return person


n, k = map(int, input().split())
print(JosephusIter(n, k))
