from fractions import Fraction

def decimals(n):

    current_val = Fraction(1, n)
    index = 0
    seen = {current_val:0} # Value and index.
    decimals = []
    current_count = 0

    while True:

        current_count = 0
        while current_val > Fraction(1, 10):
            current_count += 1
            current_val -= Fraction(1, 10)

        decimals.append(current_count)
        current_val *= 10


        if current_val in seen:
            decimals.insert(seen[current_val], "REPEAT")
            break

        index += 1
        seen[current_val] = index

    return decimals

def decimal_repeat_length(n):
    dec = decimals(n)
    for i,x in enumerate(dec):
        if x == "REPEAT":
            return len(dec) - i
    return 0


if __name__ == '__main__':
    
    longest_length = 0
    ans = 0

    for n in range(2, 1000):
        current = decimal_repeat_length(n)
        if current > longest_length:
            ans = n
            longest_length = current

    print(f'answer = {ans}')