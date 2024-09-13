def permutations(nums):
    if len(nums) == 0:
        yield []
    for i,x in enumerate(nums):
        rest = nums[:i] + nums[i+1:]
        for perm in permutations(rest):
            yield [x] + perm

if __name__ == '__main__':

    digits = [0,1,2,3,4,5,6,7,8,9]

    # Built-in solution.
    # Permutations are in lexicographical ordering of input.  
    #from itertools import permutations
    for index, perm in enumerate(permutations(digits)):
        if index == 999_999:
            break

    ans = ''.join([str(d) for d in perm])
    print(f'answer is {ans}')