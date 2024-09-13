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

primes = primes_below(10_000)
primes_set = set(primes)

from itertools import permutations
def are_perms(a,b,c):
    a,b,c = str(a), str(b), str(c)
    perms = set(''.join(perm) for perm in permutations(a))
    return b in perms and c in perms

if __name__ == '__main__':

    P = len(primes)
    for i in range(P):
        for j in range(i):
            p2 = primes[i]
            p1 = primes[j]
            next_num = p2 + (p2 - p1)
            if p1 == 1487:
                continue

            if (next_num in primes_set 
                and are_perms(p1, p2, next_num)):
                ap = [p1,p2,next_num]

    ans = int(str(ap[0]) + str(ap[1]) + str(ap[2]))
    print(f'answer = {ans}')