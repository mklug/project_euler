from functools import cache

@cache
def sum_proper_divisors(n):
    ans = 0
    for d in range(1, (n//2) + 1):
        if n % d == 0:
            ans += d
    return ans

if __name__ == '__main__':

    ans = 0
    for a in range(10_000):
        for b in range(a):
            if sum_proper_divisors(a) == b and sum_proper_divisors(b) == a:
                ans += a
                ans += b
    print(f'answer = {ans}')