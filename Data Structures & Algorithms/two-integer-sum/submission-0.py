class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashset = {}

        for i, n in enumerate(nums):
            diff = target-n
            if diff in hashset:
                return [hashset[diff], i]
            hashset[n] = i