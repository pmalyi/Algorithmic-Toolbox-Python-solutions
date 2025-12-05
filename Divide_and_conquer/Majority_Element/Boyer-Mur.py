class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        #if count > len(nums) // 2:
        return candidate

if __name__ == "__main__":
    nums = tuple(map(int, input().split()))
    res = Solution()
    print(res.majorityElement(nums))