from fractions import Fraction


def gen():
    current = 1 + Fraction(1, 2)
    while True:
        yield current
        current = 1 + Fraction(1, 2 + current - 1)


if __name__ == '__main__':

    ans = 0
    for approx, _ in zip(gen(), range(1000)):
        if len(str(approx.numerator)) > len(str(approx.denominator)):
            ans += 1

    print(f'answer = {ans}')
