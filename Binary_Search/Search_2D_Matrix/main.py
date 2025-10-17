#Brute Force Method O(n)
from typing import List
class Solution:
    ##def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    ##    for i in range(len(matrix)):
    ##        n = matrix[i]
    ##        for j in range(len(n)):
    ##            if (n[j] == target):
    ##                return (True)
    ##     return (False)
    # Using Binary Sort O(logm*n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
                    return False
        R = len(matrix)
        C = len(matrix[0]) 
        low = 0
        high = R * C - 1

        while low <= high:
            mid = low + (high - low) // 2
            i = mid // C
            j = mid % C
            mid_value = matrix[i][j] 
            if mid_value == target:
                return True
            elif mid_value < target:
                low = mid + 1
            else:
                high = mid - 1       
        return False

                
c = Solution()
c.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 21)
