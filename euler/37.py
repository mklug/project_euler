

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

def left_truncations(s):
    current = s
    while len(current) > 0:
        yield current
        current = current[1:]

def right_truncations(s):
    current = s
    while len(current) > 0:
        yield current
        current = current[:-1]

if __name__ == '__main__':


    N = 1_000_000

    primes = set(primes_below(N))
    ans = 0
    count = 0

    from itertools import chain

    for p in primes:
        ps = str(p)
        if len(ps) == 1:
            continue
        if all(int(k) in primes for k in chain(left_truncations(ps), 
                                               right_truncations(ps))):
            ans += p
            count += 1

    if count == 11:
        print(f'answer = {ans}')
    else:
        print('Need to look at more primes.')