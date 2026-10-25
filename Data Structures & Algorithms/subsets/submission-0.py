class Solution:
    def subsets(self, nums):
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res