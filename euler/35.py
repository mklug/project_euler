# Number of circular primes below 1_000_000.

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
        
def circular_digit_rotations(x):
    current = str(x)
    N = len(current)
    for _ in range(N):
        yield int(current)
        current = current[-1] + current[0:-1]

if __name__ == '__main__':

    primes = set(primes_below(1_000_000))

    ans = 0
    for k in range(1_000_000):
        if all(a in primes for a in circular_digit_rotations(k)):
            ans += 1

    print(f'answer = {ans}')