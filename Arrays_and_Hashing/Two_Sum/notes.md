### Time Complexity
- **O(n)**: We iterate through the `nums` list exactly once. Dictionary (hash map) lookups and insertions take O(1) on average. In the worst case (hash collisions), it could degrade to O(n), but this is rare with good hash functions.

### Space Complexity
- **O(n)**: In the worst case, we might store all `n` elements and their indices in the `num_map` dictionary if no pair is found until the very last element.

### Pattern
- Hash Map / Dictionary

#### Notes
- This is the classic and most efficient solution for the Two Sum problem when the input array is not sorted.
- The core idea is to iterate through the array and for each number, calculate the `complement` (the number needed to reach the target).
- We then check if this `complement` has already been seen and stored in our hash map.
- If the `complement` is in the map, we've found our pair, and we return its stored index along with the current number's index.
- If the `complement` is not in the map, we add the current number and its index to the map for future lookups.
- This approach avoids nested loops (which would be O(n^2)) by leveraging the O(1) average time complexity of hash map lookups.
- The problem statement typically guarantees that exactly one solution exists, so we don't need to worry about cases with no solution or multiple solutions.
