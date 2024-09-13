# First triangular number to have over 500 divisors.  

def triangular_numbers():
    n = 1
    t = 1
    while True:
        yield t
        n += 1
        t += n

def primes_below(n):
    res = [True] * (n + 1)
    res[0] = res[1] = False
    for i in range(n + 1):
        if res[i]:
            for j in range(i + i, n + 1, i):
                res[j] = False
    return res


primes = primes_below(1_000_000)
primes = [i for i,b in enumerate(primes) if b]

from math import prod

def faster_number_divisors(x):
    exponents = []
    for p in primes:
        if x % p == 0:
            current = x/p
            e = 1
            while current % p == 0:
                e += 1
                current /= p
            exponents.append(e)
        if p > x:
            break
    return prod(e+1 for e in exponents)

if __name__ == '__main__':

    for x in triangular_numbers():
        if faster_number_divisors(x) > 500:
            break

    print(f'answer = {x}')


'''
This one is a bit tricky to be certain that we got.

We found that 76_576_500 has more than 500 divisors.  
But we only looked for divisors with primes less than 
1_00_000.

Find the smallest number divisable  by a prime over 
one million with over 250 divisors... We need
to see that that is larger than our number.  Hence
it suffices to look at small primes.    
'''