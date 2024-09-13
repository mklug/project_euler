# Coin sum.

def coins_sum(coins, target_val):

    N = len(coins)

    def dfs(index, target):
        if target < 0:
            return 0
        if target == 0:
            return 1
        if index == N:
            return 0
        
        ans = dfs(index + 1, target) # Don't use.
        target -= coins[index]
        while target >= 0:
            ans += dfs(index + 1, target)
            target -= coins[index]
        return ans

    return dfs(0, target_val)


if __name__ == '__main__':
    
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ans = coins_sum(coins, 200)
    print(f'answer = {ans}')