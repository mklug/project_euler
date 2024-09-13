from collections import Counter


def test(n):
    n_digits = Counter(str(n))
    return all(Counter(str(i * n)) == n_digits for i in range(2, 7))


if __name__ == '__main__':

    current = 1
    while True:

        if test(current):
            print(f'answer = {current}')
            import sys
            sys.exit()

        current += 1
