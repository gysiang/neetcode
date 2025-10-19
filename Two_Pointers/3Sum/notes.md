### Time Complexity
- O(n2)

### Pattern
- Two Pointer

#### Notes
- set i first in a range, then set the left and right pointers
- left = i + 1
- right = last index
- use similar technique to binary search if sum is > 0, right--
- if sum < 0, left++
- if the next number is the same, move to the next number
