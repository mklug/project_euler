def triangular_below(n):
    res = []
    current = 1
    index = 1
    while current < n:
        res.append(current)
        index += 1
        current += index
    return res

N = 1_000_000
triangular = set(triangular_below(N))

if __name__ == '__main__':

    with open('42_words.txt') as f:
        words = f.read().replace('"', '').split(',')

    ans = 0
    for word in words:
        if sum(ord(c) - ord('A') + 1 for c in word) in triangular:
            ans += 1
    print(f'answer = {ans}')