if __name__ == '__main__':
    n = 2**1000
    ans = sum(int(c) for c in str(n))
    print(f'answer = {ans}')