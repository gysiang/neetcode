class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')':'(', ']':'[', '}':'{'}
        for char in s:
            #if open brackets insert into stack
            if (char in map.values()):
                stack.append(char)
            else:
                #check if there is anything in stack
                if (len(stack) > 0):
                    tmp = stack.pop()
                    if (map[char] != tmp):
                        return (False)
                else:
                # if there are nothing to pop, it must be wrong
                    return (False)
        #check if the stack is empty, if not empty return False
        return (not stack)     
