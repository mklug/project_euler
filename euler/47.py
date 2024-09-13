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

N = 1_000_000
primes = primes_below(N)

def count_distinct_divisors(n):
    assert n < primes[-1]
    res = 0
    prime_index = 0
    while n != 1:
        if n % primes[prime_index] == 0:
            res += 1
            while n % primes[prime_index] == 0:
                n //= primes[prime_index]
        prime_index += 1
    return res

if __name__ == '__main__':

    from collections import deque
    previous_4_divs = deque([False, False, False])

    for i in range(1, N):
        b = (count_distinct_divisors(i) == 4)
        if b and all(previous_4_divs):
            ans = i - 3
            break
        previous_4_divs.popleft()
        previous_4_divs.append(b)

    print(f'answer = {ans}')