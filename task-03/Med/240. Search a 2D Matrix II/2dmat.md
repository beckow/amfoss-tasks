My code:

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(m):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                lo=0
                hi=n
                while (lo<hi):
                    mid=(lo+hi)//2
                    
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]<target:
                        lo = mid + 1
                    else:
                        hi = mid
                        
        return False

Explanation:
find the no of rows and columns of the matrix
then a loop in the no of columns is made and wee check if the target to be found is inside the value range of the matrix 
if it inside, then we initialize the lo = 0 and high to n (max value)
then while the lo is less than high we find mid then and we check if the matrix [i][midd] == target
else if its less, we incrase lo to mid+1
else we lower hi to mid

and if the target is not inside we return false
