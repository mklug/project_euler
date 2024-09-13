# Which prime below 1_000_000 can be written 
# as the sum of the most consecutive primes?

from math import sqrt, ceil
def primes_below(n):

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(ceil(sqrt(n))):
        if is_prime[i]:
            for j in range(i+i, n, i):
                is_prime[j] = False
    
    primes = []
    for p,b in enumerate(is_prime):
        if b:
            primes.append(p)

    return primes

primes = primes_below(1_000_000)
print(primes[:10])


max_window = 0
current_sum = 0
index = 0
while current_sum < 1_000_000:
    current_sum += primes[index]
    index += 1

max_window = index # 547


set_primes = set(primes)

# Idea: sliding window of bounded size in the primes list

def contains_window_sum(window_size):
    '''
    Returns a prime if there is a sum of window_size
    primes that is also prime in the primes less than
    one million.  Return -1 otherwise.
    '''

    L = 0
    R = window_size
    N = len(primes)

    current_sum = sum(primes[L:R])
    if current_sum in set_primes:
        return current_sum
    
    for R in range(window_size, N):

        current_sum += primes[R]
        current_sum -= primes[L]
        L += 1

        if current_sum in set_primes:
            return current_sum
        
        if current_sum > 1_000_000:
            return -1

    return -1


if __name__ == '__main__':
    
    ans = 2
    for window_size in range(2, max_window + 1):
        if (current := contains_window_sum(window_size)) != -1:
            ans = current
    
    print(f'answer = {ans}')