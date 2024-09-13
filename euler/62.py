# Smallest cube for which five permutations 
# of the digits are cubes.

# Key: to show we have exactly 5 cubes with the
# digits, we must check cubes until the number of 
# digits changes. 

from collections import Counter 

def digit_frequency(x):
    res = [0] * 10
    for c in str(x):
        res[int(c)] += 1
    return tuple(res)

if __name__ == '__main__':
    
    # digit frequency --> smallest cube with that frequency.
    d = {}

    # digit frequency counter
    c = Counter()

    for x in range(1,20_000):
        cube = x**3
        df = digit_frequency(cube)
        c[df] += 1
        if df not in d:
            d[df] = cube


    # The output of the following shows the answer is
    # 127035954683.
    for k,v in c.items():
        if v == 5:
            print(sum(k)) # number of digits.
            print(k)
            print(d[k])