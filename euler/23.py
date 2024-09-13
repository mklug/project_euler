# All above 28123 are the sum of two abundant numbers.
# Sum of all numbers that are not the sum of two abundant numbers.

def divisors_sum(n):
    res = 0
    for d in range(1, (n//2) + 1):
        if n % d == 0:
            res += d
    return res

def is_abundant(n):
    return n < divisors_sum(n)

if __name__ == '__main__':

    N = 28123 + 1

    abundant = []
    for i in range(1, N):
        if is_abundant(i):
            abundant.append(i)

    sum_two_abundant = [False] * N
    for a in abundant:
        for b in abundant:
            if a + b < N:
                sum_two_abundant[a + b] = True

    ans = 0
    for i, b in enumerate(sum_two_abundant):
        if not b:
            ans += i
    
    print(f'answer = {ans}')