from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # First pass: Calculate prefix products
        prefix_product = 1
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]

        # Second pass: Calculate suffix products and multiply
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix_product
            suffix_product *= nums[i]

        return res
