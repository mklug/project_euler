# Sum of double-base palindromes in base 10 and 2 less than 1_000_000.

def is_palindrome(s):
    L = 0
    R = len(s) - 1
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True

if __name__ == '__main__':

    ans = 0
    for x in range(1_000_000):
        if is_palindrome(str(x)) and is_palindrome(bin(x)[2:]):
            ans += x

    print(f'answer = {ans}')