def fib(a0, a1, upper_bound):
    while a0 < upper_bound:
        yield a0
        a0, a1 = a1, a0 + a1

if __name__ == '__main__':

    ans = sum(x for x in fib(1,2,4000000) if x%2 == 0)
    print(f'answer = {ans}')