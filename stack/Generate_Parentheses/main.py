class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(o, c, path):
            if (o == c == n):
                res.append(path)
                return
            if (o < n):
                backtrack(o+1, c, path + "(")
            if (o > c):
                backtrack(o, c+1, path + ")")
        backtrack(0, 0, "")
        return res

c = Solution()
c.generateParenthesis(2)
