# Pentagonal differences.  

def gen_pentagonal(n):
    current = 1
    index = 1
    while current < n:
        yield current
        index += 3
        current += index

if __name__ == '__main__':

    N = 10_000_000
    pentagonal_list = [pent for pent in gen_pentagonal(N)]
    pentagonal_set = set(pentagonal_list)

    L = len(pentagonal_list)

    D = float("inf")
    for i in range(L - 1):
        for j in range(i):
            p1 = pentagonal_list[i]
            p2 = pentagonal_list[j]
            if (p1 + p2 in pentagonal_set and 
                p1 - p2 in pentagonal_set):
                D = min(D, p1 - p2)
    
    print(f'answer = {D}')
