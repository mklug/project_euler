# Digit cancelling fractions.

from fractions import Fraction

def nontrivial_cancel(num, den):

    num = str(num)
    den = str(den)

    if len(num) < 2 or len(den) < 2:
        return Fraction(0)

    if num[1] == den[1] != '0':
        return Fraction(int(num[0]), 
                        int(den[0]))
    
    if num[0] == den[0] and den[1] != '0':
        return Fraction(int(num[1]), 
                        int(den[1]))
    
    if num[1] == den[0] and den[1] != '0':
        return Fraction(int(num[0]), 
                        int(den[1]))
    
    if num[0] == den[1] and den[0] != '0':
        return Fraction(int(num[1]), 
                        int(den[0]))
    
    return Fraction(0)

if __name__ == '__main__':
    
    prod = Fraction(1)
    for den in range(1,100):
        for num in range(den):
            if nontrivial_cancel(num, den) == Fraction(num, den) != 0:
                print(num, den, Fraction(num, den))
                prod *= Fraction(num, den)
    
    print(f'answer = {prod.denominator}')
