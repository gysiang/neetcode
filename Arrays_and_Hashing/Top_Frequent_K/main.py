from typing import List
from collections import defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = Counter(nums)
        desList = (sorted(n, reverse=True))
        i = 0
        while i < k:
            res.append(desList[i])
            i += 1
        return res

c = Solution()
c.topKFrequent([1,2,2,3,3,3], 2)
