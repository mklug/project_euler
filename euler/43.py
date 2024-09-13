from itertools import permutations

if __name__ == '__main__':

    digits = '0123456789'
    primes = [2,3,5,7,11,13,17]

    ans = 0
    for perm in permutations(digits):
        if all(int(''.join(perm[index+1:index+4])) 
               % primes[index] == 0
               for index in range(0,7)):
            ans += int(''.join(perm))

    print(f'answer = {ans}')