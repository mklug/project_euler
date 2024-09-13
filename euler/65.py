# Sum of the digits of the 100th convergent of the Euler continued fraction of e.
from fractions import Fraction


def euler_continued_fraction():
    yield from [2, 1]
    current = 2
    while True:
        yield from [current, 1, 1]
        current += 2


def continued_fraction_to_fraction(cf):
    if len(cf) == 0:
        return Fraction(0)
    res = Fraction(cf[0])
    if len(cf) > 1:
        res += 1/continued_fraction_to_fraction(cf[1:])
    return res


if __name__ == '__main__':
    cf = [x for _, x in zip(range(100), euler_continued_fraction())]
    num = continued_fraction_to_fraction(cf).numerator
    print(f'answer = {sum(int(d) for d in str(num))}')
