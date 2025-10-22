# Encode and Decode Strings

## Problem Description

Design an algorithm to encode a list of strings to a single string. The encoded string is then sent over the network and is decoded back to the original list of strings.

The main challenge is to ensure that the encoding and decoding process is robust, meaning it can handle any possible characters within the strings, including characters that might be used as delimiters in a naive approach.

## Naive Approach and Its Flaw

A common first thought is to simply join the strings with a unique delimiter, for example, `#`:

```python
def encode(strs):
    return "#".join(strs)

def decode(s):
    return s.split('#')
```

This approach works for simple cases like `["hello", "world"]` which encodes to `"hello#world"`. However, it fails if any of the original strings contain the chosen delimiter.

**Example of failure:**
If `strs = ["neet#code", "is", "awesome"]`
`encode` would produce `"neet#code#is#awesome"`.
`decode` would then split this into `['neet', 'code', 'is', 'awesome']`, which is incorrect as it loses the original structure.

## Robust Solution: Length-Prefixing

To overcome the delimiter collision problem, a robust solution involves prepending the length of each string to the string itself, followed by a chosen delimiter (e.g., `#`). This way, the decoder knows exactly how many characters to read for each string, regardless of its content.

**Encoding Strategy:**
For each string `s` in the input list `strs`, we form a chunk `f"{len(s)}#{s}"`. All these chunks are then concatenated to form the final encoded string.

**Example:**
`strs = ["neet#code", "is", "awesome"]`
1. `"neet#code"` has length 9. Chunk: `"9#neet#code"`
2. `"is"` has length 2. Chunk: `"2#is"`
3. `"awesome"` has length 7. Chunk: `"7#awesome"`

Encoded string: `"9#neet#code2#is7#awesome"`

**Decoding Strategy:**
The decoder iterates through the encoded string.
1. It reads characters until it encounters the delimiter `#`. The substring before `#` represents the length of the next original string.
2. It converts this length string to an integer.
3. It then reads exactly that many characters immediately following the `#` to reconstruct the original string.
4. The pointer is advanced to the position after the extracted string, and the process repeats until the entire encoded string is consumed.

## Complexity Analysis

Let `N` be the number of strings in the input list `strs`, and `L` be the total number of characters across all strings (i.e., `L = sum(len(s) for s in strs)`).

### `encode` function:
-   **Time Complexity**: O(L). We iterate through each character of each string once to calculate its length and then concatenate them. String concatenation in Python can be `O(L^2)` in naive implementations, but `"".join()` is optimized to `O(L)`.
-   **Space Complexity**: O(L). The encoded string will store all characters from the original strings plus the length prefixes and delimiters.

### `decode` function:
-   **Time Complexity**: O(L). We iterate through the encoded string once. For each string, we parse its length (which is proportional to the number of digits in the length, typically small) and then slice the string. String slicing takes time proportional to the length of the slice. In total, we process each character of the encoded string once.
-   **Space Complexity**: O(L). The decoded list of strings will store all characters from the original strings.
