class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while (right > left):
            currentsum = numbers[left] + numbers[right]
            if (currentsum < target):
                left += 1
            elif (currentsum > target):
                right -= 1
            else:
                return ([left+1, right+1])

s = Solution()
print(s.twoSum([1,2,3,4], 3))

