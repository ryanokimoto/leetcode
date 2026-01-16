# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make frequency map
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        # make list of lists where index is all nums with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, v in freq.items():
            
            buckets[v].append(key)

        # iterate backwards through list of lists and return first k
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(num)
        return res
