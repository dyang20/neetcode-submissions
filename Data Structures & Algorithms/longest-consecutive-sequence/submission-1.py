class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = {}
        for n in nums:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 1
        
        res = 0
        for i in range(len(nums)):
            num = nums[i]
            curr_len = 0
            if num - 1 in hmap:
                continue
            else:
                while num + 1 in hmap:
                    curr_len += 1
                    num += 1
                
            res = max(res, curr_len + 1)
        return res