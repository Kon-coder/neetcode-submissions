class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            elif tokens[i] == '+':
                right = stack.pop()
                left = stack.pop()
                ans =   left + right
                stack.append(ans)
            elif tokens[i] == '-':
                right = stack.pop()
                left = stack.pop()
                ans =   left - right
                stack.append(ans)
            elif tokens[i] == '/':
                right = stack.pop()
                left = stack.pop()
                ans =   left / right
                stack.append(int(ans))
            elif tokens[i] == '*':
                right = stack.pop()
                left = stack.pop()
                ans =   left * right
                stack.append(ans)

            
        return stack.pop()