def JosephusRecurs(n, k):
    if n < 2:
        return 0
    ''' 
    new_n = n - 1
    call = JosephusRecurs(new_n, k)
    pre_res = call + k
    res = pre_res % n
    return res'''
    return (JosephusRecurs(n - 1, k) + k) % n


n, k = map(int, input().split())
print(JosephusRecurs(n, k))

