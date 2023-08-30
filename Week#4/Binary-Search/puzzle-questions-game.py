def guess(A, low, high):
    count_query = 1
    while len(A[low:high]) > 1:
        count_query += 1
        middle = (low + high) // 2
        print(A[middle])
        answer = input()
        if answer == 'sm':
            high = middle - 1
            #print(f'x is smaller than {A[middle]}')
        elif answer == 'lg':
            low = middle + 1
            #print(f'x is larger than {A[middle]}')
        else:
            print(f'Congratulations! x is equal to {A[middle]}')
            break
    else:
        print(f'Congratulations! x is equal to {A[low]}')
    return count_query


n = int(input())
myTuple = tuple(range(1, n + 1))
print(f'Number of query is {guess(myTuple, 0, len(myTuple) - 1)}')
