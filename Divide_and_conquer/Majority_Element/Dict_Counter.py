from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        cd = Counter(nums)
        mid = len(nums) // 2
        for key in cd:
            if cd[key] >= mid:
                return key
        return -1

if __name__ == "__main__":
    nums = tuple(map(int, input().split()))
    res = Solution()
    print(res.majorityElement(nums))