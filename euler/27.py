from math import ceil, sqrt

def primes(n):
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(ceil(sqrt(n))):
        if is_prime[i]:
            for j in range(i+i, n, i):
                is_prime[j] = False

    primes = []
    for i,b in enumerate(is_prime):
        if b:
            primes.append(i)
    return primes

N = 1_000_000

primes = set(primes(N))

def prime_run(a, b):
    n = 0
    while n**2 + a*n + b in primes:
        n += 1

    assert n**2 + a*n + b < N
    return n

if __name__ == '__main__':

    from itertools import product

    pairs = product(range(-999, 100),
                    range(0, 1001))

    ans = 0
    best_run = 0 

    for a, b in pairs:
        current_run = prime_run(a, b)
        if best_run < current_run:
            best_run = current_run
            ans = a * b
        
    print(f'answer = {ans}')