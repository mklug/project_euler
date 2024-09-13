from math import sqrt, ceil

def primes(n):
    '''Boolean array of primes less than n.
    '''
    res = [True] * n
    res[0] = res[1] = False
    for i in range(ceil(sqrt(n))):
        if res[i]:
            for j in range(i+i, n, i):
                res[j] = False
    return res

if __name__ == '__main__':

    n = 100000 # Arbitrary start value.
    primes_below = primes(n)
    while sum(primes_below) < 10001:
        n *= 10
        primes_below = primes(n)

    count = 0
    for i,b in enumerate(primes_below):
        if b:
            count += 1
            if count == 10001:
                ans = i
                break

    print(f'answer = {ans}')