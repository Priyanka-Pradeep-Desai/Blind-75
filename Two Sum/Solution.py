from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      prevMap = {}

      for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return[prevMap[diff], i]
        prevMap[n] = i

solution = Solution()
nums = [2, 7, 11, 15]
target = 9
print(solution.twoSum(nums, target))
