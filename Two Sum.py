#My solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return
#Ai solution

def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
