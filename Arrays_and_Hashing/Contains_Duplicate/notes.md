### Time Complexity
- O(n), where n is the number of elements in the list `nums`. We iterate through the list once.

### Space Complexity
- O(n) in the worst case. If all elements are unique, the hash set will store all `n` elements.

### Pattern
- Hash Set / Hash Map

#### Notes
- The most efficient way to solve this is by using a data structure that provides O(1) average time complexity for lookups and insertions.
- A hash set (or a hash map) is perfect for this. We iterate through the list, adding each element to the set. If we encounter an element that is already in the set, we have found a duplicate and can return `True` immediately.
