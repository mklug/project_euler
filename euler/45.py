def gen_triangular(n):
    current = 1
    index = 1
    while current < n:
        yield current
        index += 1
        current += index
    
def gen_pentagonal(n):
    current = 1
    index = 1
    while current < n:
        yield current
        index += 3
        current += index

def gen_hexagonal(n):
    current = 1
    index = 1
    while current < n:
        yield current
        index += 4
        current += index

if __name__ == '__main__':

    N = 100_000_000_000 # Guess of how large.

    pent = set(gen_pentagonal(N))
    hex = set(gen_hexagonal(N))


    ans = 0
    for t in gen_triangular(N):
        if t <= 40755:
            continue
        if t in pent and t in hex:
            ans = t
            break

    print(f'answer = {ans}')