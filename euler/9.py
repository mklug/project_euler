# Unique pythagorean triple (a,b,c) with a + b + c = 1000.
# Find a * b * c.

if __name__ == '__main__':

    for a in range(1,1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                ans = a*b*c

    print(f'answer = {ans}')
