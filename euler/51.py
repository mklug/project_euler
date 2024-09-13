from itertools import combinations
from math import isqrt


def primes_below(N):
    is_prime = bytearray((0, 1) * (N//2))
    is_prime[1] = 0
    is_prime[2] = 1
    for p in range(isqrt(N) + 1):
        if is_prime[p]:
            is_prime[p**2: N: 2*p] = bytes(len(range(p**2, N, 2*p)))
    primes = []
    for p in range(N):
        if is_prime[p]:
            primes.append(p)
    return primes


N = 10_000_000
primes_list = primes_below(N)
primes_set = set(primes_list)
digits = '0123456789'
INF = float("inf")


def count(p_string, star_indices):
    '''
    e.g. p_string = '101'
         star_indices = [1]
         Return the number of primes of the form 1*1.
    '''
    p_star = []
    for i in range(len(p_string)):
        if i in star_indices:
            p_star.append('*')
        else:
            p_star.append(p_string[i])
    p_star = ''.join(p_star)

    res = 0
    smallest_prime = INF
    for digit in digits:

        if digit == '0' and 0 in star_indices:
            continue

        current = int(p_star.replace('*', digit))
        if current in primes_set:
            res += 1
            smallest_prime = min(smallest_prime, current)

    return res, smallest_prime


if __name__ == '__main__':

    for p in primes_list:
        p_string = str(p)
        N = len(p_string)
        for k in range(1, N+1):
            for star_indices in combinations(range(N), k):
                c, current_p = count(p_string, star_indices)
                if c == 8:
                    print(f'answer = {current_p}')
                    exit()
