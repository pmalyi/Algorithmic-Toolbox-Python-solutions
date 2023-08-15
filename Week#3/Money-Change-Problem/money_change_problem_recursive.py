# Recursive Python3 program for
# coin change problem.

# Returns the count of ways we can sum
# coins[0...n-1] coins to get sum "sum"


def count(coins, n, money):
    # If sum is 0 then there is 1
    # solution (do not include any coin)
    if (money == 0):
        return 1

    # If money is less than 0 then no
    # solution exists
    if (money < 0):
        return 0

    # If there are no coins and money
    # is greater than 0, then no
    # solution exist
    if (n <= 0):
        return 0

    # count is money of solutions (i)
    # including coins[n-1] (ii) excluding coins[n-1]
    return count(coins, n - 1, money) + count(coins, n, money - coins[n - 1])


# Driver program to test above function
money = int(input())
coins = list(map(int, input().split()))
n = len(coins)
print(count(coins, n, money))

# This code is contributed by Smitha Dinesh Semwal