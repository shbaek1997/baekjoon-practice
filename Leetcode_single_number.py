class Solution:
    def singleNumber(self, nums):
        nums_dict = dict()
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        for num, value in nums_dict.items():
            if value == 1:
                return num


a = Solution()
a.singleNumber([1, 2, 1, 2, 3])
