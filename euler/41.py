from math import ceil, sqrt
def primes_below(n):
    is_prime = [True] * (n)
    is_prime[0] = is_prime[1] = False
    for i in range(ceil(sqrt(n))):
        if is_prime[i]:
            for j in range(i + i, n, i):
                is_prime[j] = False

    primes = [p for p,b in enumerate(is_prime) if b]
    return primes


if __name__ == '__main__':

    primes = primes_below(10_000_000)
    def is_prime(k):
        for p in primes:
            if k % p == 0:
                return False
            if p > ceil(sqrt(k)):
                return True
        return True
    
    digits = '123456789'

    from itertools import permutations

    print(is_prime(98765431))
    ans = 1
    for k in range(2,10):
        comb = digits[:k]
        for perm in permutations(comb):
            current = int(''.join(perm))
            if is_prime(current):
                ans = max(ans, current)
    print(f'answer = {ans}')