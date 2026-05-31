class Solution:
    def rob(self, nums: List[int]) -> int:
        

        # dp[i] = max(nums[i] + dp[i+2], dp[i])
        # n = len(nums)
        # dp = [0]*(n+2)

        # for i in range(len(nums)-1, -1, -1):
        #     dp[i] = max(nums[i]+dp[i+2], dp[i+1])
        # return dp[0]

        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2