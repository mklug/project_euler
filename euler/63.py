# Note that the number of digits of x is floor(log_10(x)) + 1
# Well, log_10(x^k) + 1 = k log_10(x) + 1 = k
# --> log_10(x) < 1
# This limits the x values to 1,2,3,4,5,6,7,8,9.
# To limit the k, note that floor(k * log_10(x)) = k - 1.
# Setting x = 9, we see we only need to check up to k = 25.

from math import log10


def number_digits(x):
    return len(str(x))


if __name__ == '__main__':

    # Gets the values for k
    # for k in range(1, 100):
    #    print(log10(9) * k, k-1)

    res = 0
    xs = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    seen = set()
    for x in xs:
        for k in range(1, 26):
            if number_digits(x**k) == k:
                seen.add(x**k)
                res += 1
    print(f'answer = {res}')
