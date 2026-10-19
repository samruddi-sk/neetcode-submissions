from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()

        for right in range(len(nums)):
            while window and nums[window[-1]] < nums[right]:
                window.pop()

            window.append(right)

            if window[0] <= right - k:
                window.popleft()

            if right >= k - 1:
                result.append(nums[window[0]])

        return result