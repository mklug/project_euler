def num_rights(p):
    '''
    Returns the number of right triangles with perimeter p.
    '''
    res = 0
    for a in range(1, p):
        for b in range(1, a + 1):
            if a**2 + b**2 == (p-a-b)**2:
                res += 1
    return res

if __name__ == '__main__':
    print(f'answer = {max(range(1,1001), key=num_rights)}')