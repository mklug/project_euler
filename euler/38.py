def is_pan_digital(n):
    s = str(n)
    if '0' in s:
        return False
    return len(s) == 9 and len(set(s)) == 9

def gen_con_products(n):

    current_val = int(str(n) + str(2*n))
    current_mult = 3

    while len(str(current_val)) < 10:
        if is_pan_digital(current_val):
            yield current_val
        current_val = int(str(current_val) + str(n * current_mult))
        current_mult += 1

if __name__ == '__main__':
    
    count = 0
    for y in gen_con_products(10):
        print(y)
        count +=1 
        if count > 1000:
            break
    
    print('done')

    ans = 1
    for x in range(1,1_000_000):
        for y in gen_con_products(x):
            ans = max(ans, y)
    print(f'answer = {ans}')