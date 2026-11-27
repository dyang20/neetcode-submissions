class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        res = 0
        
        while l < r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                res += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                res += rmax - height[r]
                r -= 1
        return res

        # post = [0] * len(height)
        # cur_max = post[-1]
        # for i in range(len(height) - 1, -1, -1):
        #     post[i] = max(cur_max, height[i])
        #     cur_max = post[i]
        
        # pre = [0] * len(height)
        # cur_maxp = pre[0]
        # for i in range(len(height)):
        #     pre[i] = max(cur_maxp, height[i])
        #     cur_maxp = pre[i]

        # res = 0
        # for i in range(len(height)):
        #     res += min(pre[i], post[i]) - height[i]
        
        # return res