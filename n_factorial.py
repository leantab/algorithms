# find the Kth factorial of N
n = 4
k = 22


def find_k_fact(n, k):
    k -= 1  # we are using base 0
    permutation = []
    unused = list(range(1, n+1))
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1]
    # fact = 0: 1, 1:1, 2: 2*1=2, 3: 3*2=6, 4: 4*6=24, 5: 5*24=120....
    while n > 0:
        parts = fact[n]//n  # number of sections 24//4=6
        i = k//parts
        permutation.append(unused[i])
        unused.pop(i)
        n -= 1
        k = k % parts
    return ''.join(map(str, permutation))


print(find_k_fact(n, k))
