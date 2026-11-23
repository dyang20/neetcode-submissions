class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
        
        # bucket sort
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in hmap.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
            
            if len(res) == k:
                return res