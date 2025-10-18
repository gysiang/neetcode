from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return (0)
        if h == 0:
            return 0
        left = 1
        right = max(piles)
        min_speed = right
        while left <= right:
            mid = left + (right - left) // 2
            current_speed = mid
            total_time = 0

            for i in range(len(piles)):
                total_time += math.ceil(piles[i] / current_speed)
            if (total_time <= h):
                if (current_speed < min_speed):
                    min_speed = current_speed
                right = mid - 1
            elif (total_time > h):
                left = mid + 1
        return min_speed


c = Solution()
c.minEatingSpeed([1,4,3,2], 9)
