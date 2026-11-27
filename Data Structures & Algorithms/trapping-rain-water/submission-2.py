class Solution:
    def trap(self, height: List[int]) -> int:
        post = [0] * len(height)
        cur_max = post[-1]
        for i in range(len(height) - 1, -1, -1):
            post[i] = max(cur_max, height[i])
            cur_max = post[i]
        
        pre = [0] * len(height)
        cur_maxp = pre[0]
        for i in range(len(height)):
            pre[i] = max(cur_maxp, height[i])
            cur_maxp = pre[i]

        res = 0
        for i in range(len(height)):
            res += min(pre[i], post[i]) - height[i]
        
        return res