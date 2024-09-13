from math import lcm

if __name__ == '__main__':

    ans = 1
    for i in range(1,20+1):
        ans = lcm(ans, i)

    print(f'answer = {ans}')