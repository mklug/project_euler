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

def squares():
    current = 0
    while True:
        yield current ** 2
        current += 1

def squares_below(n):
    res = []
    for x in squares():
        if x >= n:
            break
        res.append(x)
    return res

if __name__ == '__main__':


    N = 1000000
    prime = primes_below(N)
    square = squares_below(N)

    def test(k):
        '''
        Is k a sum of a prime and twice a square?
        '''
        for p in prime:
            if p > k:
                break
            for s in square:
                if p + 2 * s > k:
                    break
                if p + 2 * s == k:
                    return True
        return False

    for k in range(3,N):
        if k % 2 == 0:
            continue
        if not test(k):
            break

    print(f'answer = {k}')

