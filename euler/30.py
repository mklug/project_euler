
def is_sum_of_fifth(n):
    return n == sum(int(c) ** 5 for c in str(n))

if __name__ == '__main__':

    #for n in range(6,10):
    #    print(10**(n-1) - (9**5) * n)

    # f(n) = 10**(n-1) - (9**5) * n
    # Becomes positive at n = 7.
    # So numbers that satisfy the condition must have less than 7 digits.  

    ans = 0
    for x in range(2, 10**7):
        if is_sum_of_fifth(x):
            ans += x

    print(f'answer = {ans}')
