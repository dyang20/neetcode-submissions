class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
        
        while k > 0:
            val = max(hmap.values())
            keys = [k for k, v in hmap.items() if v == val]
            res.append(keys[0])
            hmap.pop(keys[0])
            k -= 1
        return res