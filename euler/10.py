# Sum of the primes below 2 million.  

def primes(n):
    res = [True] * n
    res[0] = res[1] = False
    for i in range(n):
        if res[i]:
            for j in range(i + i, n, i):
                res[j] = False
    return res

if __name__ == '__main__':

    ans = 0
    for p,b in enumerate(primes(2_000_000)):
        if b:
            ans += p
    print(f'answer = {ans}')