class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        one, two = 0, len(numbers) - 1

        while numbers[one] + numbers[two] != target:
            n1, n2 = numbers[one], numbers[two]
            if n1 + n2 > target:
                two -= 1
            else:
                one += 1
        
        return [one + 1, two + 1]
