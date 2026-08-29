My Code:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return

explanation:
so we use the outer loop to select a number and the inner loop to select any other from the list and we check if they both add together to form a sum of given target. if it does we return those two numbers
