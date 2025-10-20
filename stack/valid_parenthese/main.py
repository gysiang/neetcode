class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or bracket_map[char] != stack.pop():
                    return False
            else:
                # Character is not a valid bracket, could be an edge case
                # depending on problem constraints. Assuming only brackets are in s.
                pass
        return not stack
