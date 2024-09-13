def gauss(n):
    return n * (n + 1) // 2

if __name__ == '__main__':
    n = 100
    ans = gauss(n)**2 - sum(x**2 for x in range(1,100 + 1))
    print(f'answer = {ans}')