# Sum of all numbers that can be written as pandigital products.

# Bound the number of digits of the multiplicand.
# Assume it is longer than or the same as the multiplier.
# Call the length L.  If L >= 5, the result has at least 5 digits
# (but 5 + 1 + 5 > 9).  So L <= 4. 

def has_pandigital_prod(a,b):
    p = a * b
    abp = str(a) + str(b) + str(p)
    if len(abp) == 9 == len(set(abp)) and '0' not in abp:
        return p
    return -1

if __name__ == '__main__':

    pandigital_prods = set()
    for a in range(10_000):
        for b in range(a):
            if (prod := has_pandigital_prod(a,b)) != -1:
                pandigital_prods.add(prod)

    print(f'answer = {sum(pandigital_prods)}')