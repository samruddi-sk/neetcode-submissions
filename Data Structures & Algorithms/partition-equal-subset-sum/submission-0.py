class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        dp = {0}

        for num in nums:
            new_dp = set()

            for s in dp:
                if s + num == target:
                    return True
                if s + num < target:
                    new_dp.add(s + num)

            dp.update(new_dp)

        return target in dp