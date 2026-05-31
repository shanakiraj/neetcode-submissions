class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # dp[i] = cost[i] + min(dp[i+1], dp[i+2])


        # n = len(cost)
        # dp = [0] * (n+2)

        # for i in range(len(cost)-1, - 1, -1):
        #     dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        # return min(dp[0], dp[1])

        end = len(cost)
        memo = {}

        def recurse(i):
            if i in memo:
                return memo[i]
            if i >= end:
                return 0
            
            memo[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return memo[i]
        recurse(0)
        return min(memo[0], memo[1])
