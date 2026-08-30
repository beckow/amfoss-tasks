My code:

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x <0:
            sign = -1
        x=abs(x)
        if -2147483648<= x <= 2147483647:
            rev = (str(x))[::-1]
            rev = int(rev)
            if -2147483648<= rev <= 2147483647:
                return rev*sign
        return 0    

Explanation:
i store the sign of the number outside and remove the sign from the number for easier reeversal
then i check if the number is btw the range -231 <= x <= 231 - 1 and then i reverse it using string reversal by converting it to a string and then its converted back to int
and then i check if the output is also inside the range -231 <= x <= 231 - 1 and if thats true, i return the reversed number with the correct sign
otherwise i return 0
