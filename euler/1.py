def multiples_below(n, multiples):
    '''Returns boolean array of length n+1
    with which elements are a multiple of 
    an element of multiples.
    '''
    res = [False] * (n+1)
    for i in range(n+1):
        for m in multiples:
            if i%m == 0:
                res[i] = True
    return res

if __name__ == '__main__':
    multiples = multiples_below(999, [3,5])
    ans = 0
    for i,b in enumerate(multiples):
        if b:
            ans += i
    print(f'answer = {ans}')
