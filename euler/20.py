from math import factorial

if __name__ == '__main__':

    ans = sum(int(c) for c in str(factorial(100)))
    print(f'answer = {ans}')