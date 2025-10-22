### Time Complexity
- **O(N * K log K)**
  - `N` is the number of strings in the input list `strs`.
  - `K` is the maximum length of a string in `strs`.
  - We iterate through each of the `N` strings. For each string, sorting its characters takes `O(K log K)` time. This makes the sorting operation the bottleneck.

### Space Complexity
- **O(N * K)**
  - The total information stored in our hash map (`res`) is, at most, all the characters from every string in the input list.

### Pattern
- **Hash Map / Dictionary with a Computed Key**

#### Notes
- The core insight is that all anagrams of a string become identical when their characters are sorted. This sorted string can be used as a unique key in a hash map to group all its corresponding anagrams.
- `collections.defaultdict(list)` is a convenient Python tool for this task. It automatically creates an empty list as the value for a new key, which simplifies the code by removing the need to check if a key already exists before appending to its list.
- The process is:
  1. Initialize a `defaultdict(list)`.
  2. For each string `s` in the input list:
     a. Create a key by sorting the characters of `s` (e.g., `'eat' -> 'aet'`).
     b. Append the original string `s` to the list associated with that key in the dictionary.
  3. Finally, return the values from the dictionary, which are the lists of grouped anagrams.
