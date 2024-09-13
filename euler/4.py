def is_palindromic(n):
    s = str(n)
    L, R = 0, len(s) - 1
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True 

if __name__ == '__main__':

    ans = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            current = a * b
            if is_palindromic(current):
                ans = max(ans, current)
    print(f'answer = {ans}')
