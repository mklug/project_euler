from functools import cache

@cache
def dp(i,j):
    if i == 20:
        return 1
    if j == 20:
        return 1
    return dp(i + 1, j) + dp(i, j + 1)

if __name__ == '__main__':

    ans = dp(0,0)
    print(f'answer = {ans}')