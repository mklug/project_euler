def digit_sum(n):
    return sum(int(c) for c in str(n))


if __name__ == '__main__':

    ans = 1
    for a in range(100):
        for b in range(100):
            ans = max(ans, digit_sum(a**b))

    print(f'answer = {ans}')
