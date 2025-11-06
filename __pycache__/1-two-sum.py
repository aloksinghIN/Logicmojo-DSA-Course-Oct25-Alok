from typing import List
class Solution:
    #naive approach O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for k in range(i+1, len(nums)):
          if nums[i] + nums[k] == target:
            print([i,k])
            return [i,k]
    
    #optimal approach O(n)
    def twoSumOpt(self, nums: List[int], target: int) -> List[int]:
      test = {}
      for i in range(len(nums)):
        diff = target - nums[i]
        if test.get(diff) is not None:
          return[test[diff],i]
        else:
          test[nums[i]]=i


class Main:
  s = Solution()
  nums = [2,7,11,15]
  target = 9
#   s.twoSum(nums,target)
  print(s.twoSumOpt(nums,target))