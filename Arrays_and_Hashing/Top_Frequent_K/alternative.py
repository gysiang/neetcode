from typing import List
from collections import Counter
import heapq

class Solution:
    """
    Solves the Top K Frequent Elements problem using a min-heap (priority queue).
    This approach is efficient, especially when k is much smaller than the number of unique elements.
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count the frequency of each number.
        # Example: Counter({3: 3, 2: 2, 1: 1})
        counts = Counter(nums)

        # 2. Use a min-heap to keep track of the k most frequent elements.
        # The heap will store tuples of (frequency, number).
        # Python's heapq is a min-heap, so it will always pop the smallest element.
        # To get the 'k' largest frequencies, we maintain a heap of size 'k'
        # and push (frequency, number). If the heap size exceeds 'k', we pop the smallest.
        min_heap = []

        for num, freq in counts.items():
            # Push the (frequency, number) tuple onto the heap.
            heapq.heappush(min_heap, (freq, num))
            # If the heap size exceeds k, remove the smallest element (least frequent).
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # 3. Extract the numbers from the heap.
        # The heap now contains the k elements with the highest frequencies.
        # Since it's a min-heap, the elements will be ordered by frequency.
        return [item[1] for item in min_heap]
