from typing import List
from collections import defaultdict

class Solution:
    """
    Solves the Group Anagrams problem using character counting.
    This is an alternative and more time-efficient approach compared to sorting.
    Time Complexity: O(N * K) where N is the number of strings and K is the max length.
    Space Complexity: O(N * K) for storing the result.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a defaultdict to group anagrams. The key will be a tuple
        # representing the character count of each string.
        res = defaultdict(list)

        for s in strs:
            # Create a count array for the 26 lowercase English letters.
            count = [0] * 26
            for char in s:
                # Map each character to an index (0-25) and increment its count.
                count[ord(char) - ord('a')] += 1

            # A list is mutable and cannot be a dictionary key, so convert it to a tuple.
            res[tuple(count)].append(s)

        return list(res.values())
