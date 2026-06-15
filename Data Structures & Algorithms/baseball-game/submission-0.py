class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for symbol in operations:
            if symbol == "+":
                stack.append(stack[-1] + stack[-2])
            elif symbol == "D":
                stack.append(2 * stack[-1])
            elif symbol == "C":
                stack.pop()
            else:
                stack.append(int(symbol))
        return sum(stack)


        