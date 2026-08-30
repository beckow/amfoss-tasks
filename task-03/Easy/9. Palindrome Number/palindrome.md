My code:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        cpy = x
        rev = 0
        while(x>0):
            ld = x%10
            rev=rev*10+ld
            x=x//10
        return rev == cpy

Explanation:
if the number is less than 0 we return 0
then i duplicate it and then reverse it using reversal logic
then i check if reverse and copy are same and returns true or false
