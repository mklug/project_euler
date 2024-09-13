def sum_square_digits(x):
    return sum(int(d)**2 for d in str(x))


to_89 = set([89])
to_1 = set([1])

if __name__ == '__main__':

    for x in range(1, 10_000_000):
        chain = [x]
        current = sum_square_digits(x)
        while current not in to_89 and current not in to_1:
            chain.append(current)
            current = sum_square_digits(current)

        if current in to_89:
            for x in chain:
                to_89.add(x)

        elif current in to_1:
            for x in chain:
                to_1.add(x)

    print(f'answer = {len(to_89)}')
