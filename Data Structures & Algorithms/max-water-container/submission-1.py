class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1
        while l < r:
            cur_max = (r - l) * min(heights[r], heights[l])
            res = max(res, cur_max)

            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return res