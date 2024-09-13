def is_palindrome(n):
    s = str(n)
    L = 0
    R = len(s) - 1
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True


def reverse(n):
    return int(str(n)[::-1])


def is_lychrel(k):
    current = k
    for _ in range(50):
        current += reverse(current)
        if is_palindrome(current):
            return False
    return True


if __name__ == '__main__':

    count = 0
    for k in range(1, 10_000):
        if is_lychrel(k):
            count += 1
    print(f'answer = {count}')
