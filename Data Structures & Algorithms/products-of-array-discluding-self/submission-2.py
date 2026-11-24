class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        pre[0] = nums[0]
        post[-1] = nums[-1]

        for i in range(1, len(nums)):
            pre[i] = pre[i - 1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i]
        
        res = [1] * len(nums)
        res[0], res[-1] = post[1], pre[-2]
        for i in range(1, len(nums) - 1):
            res[i] = pre[i - 1] * post[i + 1]
        return res

