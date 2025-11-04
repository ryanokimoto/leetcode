# https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = []
        stack.append(([], nums))
        while stack:
            top = stack.pop()
            current, remaining = top[0], top[1]
            print(current, remaining)
            if not remaining:
                result.append((current))
            else:
                for num in remaining:
                    temp = current.copy()
                    temp.append(num)
                    temprem = remaining.copy()
                    temprem.remove(num)
                    stack.append((temp, temprem))
        return result