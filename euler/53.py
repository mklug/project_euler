from math import comb

if __name__ == '__main__':

    ans = 0
    for n in range(1, 101):
        for r in range(1, n):
            if comb(n, r) > 1_000_000:
                ans += 1

    print(f'answer = {ans}')
