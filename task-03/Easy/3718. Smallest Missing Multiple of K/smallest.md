My code:
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiple = k
        while multiple in nums:
            multiple +=k
        return multiple

explanation:
i intialize the smallest multiple as k 
if multiple is inside the list of nums  then we check if the next multiple of k is there inside the list 
if the multiple is not there, we return it
if not when the list ends, the multiple increments and it is printed
