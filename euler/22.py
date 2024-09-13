def score(name):
    res = 0
    for c in name:
        res += ord(c) - ord('A') + 1
    return res

if __name__ == '__main__':

    with open('22_names.txt') as f:
        names = f.read().strip()
        names = names.replace('\"', '')
        names = names.split(',')
        names.sort()

    ans = 0
    for i, name in enumerate(names):
        ans += (i + 1) * score(name)

    print(f'answer = {ans}')