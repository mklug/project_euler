# Which starting number under 1_000_000 produces the longest Collatz chain?

from functools import cache

@cache
def collatz_chain_length(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz_chain_length(n//2)
    else:
        return 1 + collatz_chain_length(3 * n + 1)
    
if __name__ == '__main__':

    ans = 1
    longest = 1
    for x in range(1,1_000_000):
        current_chain_length = collatz_chain_length(x)
        if current_chain_length > longest:
            longest = current_chain_length
            ans = x

    print(f'answer = {ans}')
