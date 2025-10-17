#Brute Force Method O(n)
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            n = matrix[i]
            for j in range(len(n)):
                if (n[j] == target):
                    return (True)
        return (False)

                
c = Solution()
c.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 21)
