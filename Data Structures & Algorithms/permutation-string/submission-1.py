class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        def is_permute(s1: str, s2: str):
            if Counter(s1) == Counter(s2):
                return True
            
        for i in range(len(s2) - len(s1) + 1):
            if is_permute(s1, s2[i:i + len(s1)]):
                return True
        
        return False