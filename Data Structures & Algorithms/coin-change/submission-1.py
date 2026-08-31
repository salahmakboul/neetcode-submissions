class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1) :
            for coin in coins :
                if coin > i :
                    continue
                dp[i]=min(dp[i], 1 + dp[i - coin])
        
        if float('inf') == dp[amount] :
            return -1
        return dp[amount]