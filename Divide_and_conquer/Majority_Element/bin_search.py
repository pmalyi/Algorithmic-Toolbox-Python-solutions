class Solution(object):
    def majorityElement(self, nums):
       nums.sort()
       n = len(nums)
       candidate = nums[n // 2]
       count = sum(1 for num in nums if num == candidate)
       if count > len(nums) // 2:
           return candidate

       return None