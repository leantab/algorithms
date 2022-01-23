memo = {}


def sum_possible(amount, numbers):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return True
    if amount < 0:
        return False

    for num in numbers:
        dif = amount - num
        if sum_possible(dif, numbers):
            memo[amount] = True
            return True

    memo[amount] = False
    return False
