# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, n in enumerate(nums):
            if target - n in seen:
                return seen[target - n], index
            else:
                seen[n] = index
        return None 