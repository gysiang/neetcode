### Time Complexity
- O(n)

### Pattern
- Two Pointers

#### Notes
- Do a one pass, left < right, where left is 0 while right is last index
- area of water is min(height(left), right) * (right - left)
- if the area is > than current saved max, save the new area.
- what we are comparing is the height of left and right index to move left and right
- if both height are same, move left and right
