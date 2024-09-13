def is_subseq(x, y):
    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)


codes = []
with open('79_keylog.txt') as f:
    for code in f:
        code = code.strip()
        codes.append(code)

codes = list(set(codes))


def check(k):
    '''
    Check if k could be a possible passcode.
    '''
    k_string = str(k)
    return all(is_subseq(code, k_string) for code in codes)


if __name__ == '__main__':

    # Notice ther is no 4 or 5 in the seen digits.
    digits = [0, 1, 2, 3, 6, 7, 8, 9]

    G = {digit: set() for digit in digits}
    for code in codes:
        a, b, c = code
        a, b, c = map(int, [a, b, c])
        G[a].add(b)
        G[a].add(c)
        G[b].add(c)

    print(G)

    # From looking at G, we can see the following solution.
    print(check(73162890))
