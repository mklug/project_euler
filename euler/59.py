from itertools import cycle, product

with open('59_cipher.txt', 'r') as f:
    encoded = f.read().split(',')
    encoded = list(map(int, encoded))

def decode(key):
    key = [ord(c) for c in key]
    res = []
    for x,k in zip(encoded, cycle(key)):
        res.append(chr(x ^ k))
    return ''.join(res)

def contains(words, decoded):
    return all(word in decoded for word in words)

if __name__ == '__main__':

    target_words = ['and', 'the', 'from', 'for', 'of']

    from string import ascii_lowercase

    # Finds the code : 'exp'
    for key in product(ascii_lowercase, repeat=3):
        if contains(target_words, decode(key)):
            print(key)
            print(decode(key))

    ans = sum(ord(c) for c in decode(['e','x','p']))
    print(f'answer = {ans}')

