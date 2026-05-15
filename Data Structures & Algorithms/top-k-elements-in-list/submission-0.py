class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        freq = [[] for _ in range(len(nums)+1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1

        for n in count.keys():
            freq[count[n]].append(n)
        
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
