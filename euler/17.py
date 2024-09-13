
one_digit = {
       1 : 'one',
       2 : 'two',
       3 : 'three',
       4 : 'four',
       5 : 'five',
       6 : 'six',
       7 : 'seven',
       8 : 'eight',
       9 : 'nine'}

two_exceptions = {10 : 'ten',
                  11 : 'eleven',
                  12 : 'twelve',
                  13 : 'thirteen',
                  14 : 'fourteen',
                  15 : 'fifteen',
                  18 : 'eighteen'}

two_digit = {1 : 'teen',
             2 : 'twenty',
             3 : 'thirty',
             4 : 'forty',
             5 : 'fifty',
             6 : 'sixty',
             7 : 'seventy',
             8 : 'eighty',
             9 : 'ninety'}


def letter_count(x):
    
    s = str(x)
    N = len(s)
    match N:
        case 1:
            return len(one_digit[x])
        case 2:
            if x in two_exceptions:
                return len(two_exceptions[x])
            tens_digit = int(s[0])
            ones_digit = int(s[1])
            res = len(two_digit[tens_digit])
            if ones_digit != 0:
                res += len(one_digit[ones_digit])
            return res
        case 3:
            leading_digit = int(s[0])
            hundreds_length = len(one_digit[leading_digit]) + len('hundred')
            tens = int(s[1:])
            if tens > 0:
                return hundreds_length + len('and') + letter_count(tens)
            return hundreds_length

        case 4:
            return len('onethousand')

if __name__ == '__main__':

    ans = sum(letter_count(x) for x in range(1,1000+1))
    print(f'answer = {ans}')