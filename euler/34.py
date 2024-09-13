# 8 * factorial(9) has 7 digits!  
# So such numbers must have less than 8 digits.  

from math import factorial
def is_digit_sum(n):
    return sum(factorial(int(c)) for c in str(n)) == n

if __name__ == '__main__':

    ans = 0
    for n in range(3, 10_000_000):
        if is_digit_sum(n):
            ans += n
    
    print(f'answer is {ans}')