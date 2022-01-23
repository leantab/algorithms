memo = {
    0: 0,
    1: 1,
    2: 1,
}


def fib(n):
    if n in memo:
        return memo[n]
    val = fib(n-1) + fib(n-2)
    memo[n] = val
    return val


print(fib(35))
