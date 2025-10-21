### Time Complexity
- O(n log n), where n is the length of the strings. This is dominated by the `sorted()` function.
- An alternative hash map solution achieves a more optimal O(n) time complexity.

### Space Complexity
- O(n) in most Python implementations, as `sorted()` typically creates a new list to store the sorted characters.

### Pattern
- Sorting / Hash Map

#### Notes
- The provided one-line solution `sorted(s) == sorted(t)` is concise and elegant. It correctly identifies anagrams by sorting the characters of both strings and comparing the results.
- A more performant approach for interviews involves using a hash map (or a fixed-size array if the character set is known, e.g., 26 lowercase English letters) to count character frequencies.
- The hash map approach involves:
  1. A quick check: if `len(s) != len(t)`, return `False`.
  2. Count character frequencies for string `s`.
  3. Decrement counts using characters from string `t`. If a count goes below zero or a character doesn't exist, they are not anagrams.
  4. If all counts are zero at the end, they are anagrams.
