class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''.join(c.lower() for c in s if c.isalnum())
        one, two = 0, len(new) - 1
        while one < two:
            if new[one] != new[two]:
                return False
            one += 1
            two -= 1
        return True