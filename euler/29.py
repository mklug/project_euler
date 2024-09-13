from itertools import product

if __name__ == '__main__':
    
    pairs = product(range(2, 101), range(2, 101))
    unique_nums = set((map(lambda x: x[0] ** x[1], pairs)))
    ans = len(unique_nums)
    print(f'answer = {ans}')