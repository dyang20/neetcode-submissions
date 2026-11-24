class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        
        res = 0
        for i in range(len(nums)):
            num = nums[i]
            curr_len = 0
            if num - 1 in seen:
                continue
            else:
                while num + 1 in seen:
                    curr_len += 1
                    num += 1
                
            res = max(res, curr_len + 1)
        return res