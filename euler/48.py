if __name__ == '__main__':

    ans = 0

    for i in range(1,1001):
        ans += i**i
        ans %= 10**10
    print(f'answer = {ans}')