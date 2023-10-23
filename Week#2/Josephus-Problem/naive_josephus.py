def naiveJosephus(n, k):
    alive = [True] * n
    num_survivors, current_position, index = n, 0, 0
    while num_survivors:
        if alive[current_position]:
            index += 1
            if index == k:
                num_survivors = num_survivors - 1
                if not num_survivors:
                    return current_position
                else:
                    alive[current_position] = False
                    index = 0
        current_position = (current_position + 1) % n


n, k = map(int, input().split())
print(naiveJosephus(n, k))