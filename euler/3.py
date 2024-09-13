from math import sqrt, ceil

# Better siev in problem 7.
def primes_below(n):
    '''Returns a boolean array where the ith entry
    is the primality of i.
    '''
    res = [True] * (n+1)
    res[0] = res[1] = False
    for i in range(2, n+1):
        if not res[i]:
            continue
        d = 2
        while d * i < n + 1:
             res[d*i] = False
             d += 1
    return res

if __name__ == '__main__':

    # 12 digits.  
    # Square root will be 6 digits.  
    # List primes up to the square root.
    # If none divide x, the answer is x, otherwise, it is the largest.  
    x = 600851475143
    primes_below_x = primes_below(ceil(sqrt(x)))
    ans = x
    for i,b in enumerate(primes_below_x):
        if b and x%i == 0:
            ans = i
    print(f'answer = {ans}')