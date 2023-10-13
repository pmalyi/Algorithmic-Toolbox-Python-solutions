def primCalc(n):
    DP = [n] * (n + 1)
    DP[0], DP[1] = -1, 0
    prev = [-1] * (n + 1)
    for i in range(2, n + 1):
        div3 = DP[i]
        div2 = DP[i]
        minus1 = DP[i - 1]
        if (i % 3 == 0) and (i // 3 >= 1):
            div3 = DP[i // 3]
        if (i % 2 == 0) and (i // 2 >= 1):
            div2 = DP[i // 2]
        best = minus1
        prev_item = i - 1
        if div3 < best:
            best = div3
            prev_item = i // 3
        if div2 < best:
            best = div2
            prev_item = i // 2
        DP[i] = best + 1
        prev[i] = prev_item
    trace_back = []
    current = n
    while current > 0:
        trace_back.append(current)
        current = prev[current]
    trace_back.reverse()
    return DP[n], trace_back


n = int(input())
r1, r2 = primCalc(n)
print(r1, ' '.join(map(str, r2)), sep='\n')