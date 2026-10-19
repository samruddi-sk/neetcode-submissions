class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                area = h * (i - index)
                max_area = max(max_area, area)
                start = index

            stack.append((start, height))

        for index, height in stack:
            area = height * (len(heights) - index)
            max_area = max(max_area, area)

        return max_area