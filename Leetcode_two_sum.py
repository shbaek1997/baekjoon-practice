class Solution:
    def twoSum(self, nums, target: int):
        check_dict = {}
        for i, num in enumerate(nums):
            left = target-num
            if left in check_dict:
                return (check_dict[left], i)
            check_dict[num] = i


a = Solution()
a.twoSum([3, 2, 4], 6)
