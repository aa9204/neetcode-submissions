class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {")" : "(", '}' : '{', ']' : '[' }

        for char in s:
            if char in key:
                if stack and stack[-1] == key[char]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(char)
        if not stack:
            return True
        if stack:
            return False




        