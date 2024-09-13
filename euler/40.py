def gen():
    current = 1
    while True:
        yield from [int(c) for c in str(current)]
        current += 1

if __name__ == '__main__':

    ans = 1
    target = 1

    for i,x in enumerate(gen()):
        i += 1
        if i == target:
            ans *= x
            target *= 10
        if i == 1_000_000:
            break
    
    print(f'answer = {ans}')