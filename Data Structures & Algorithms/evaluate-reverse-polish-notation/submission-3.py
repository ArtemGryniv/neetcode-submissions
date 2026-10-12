class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
        
            if token == '+':
                second = int(stack.pop())
                first = int(stack.pop())
                result = first + second
                stack.append(result)
            elif token == '-':
                second = int(stack.pop())
                first = int(stack.pop())
                result = first - second
                stack.append(result)
            elif token == '*':
                second = int(stack.pop())
                first = int(stack.pop())
                result = first * second
                stack.append(result)
            elif token == '/':
                second = int(stack.pop())
                first = int(stack.pop())
                result = int(first / second)
                stack.append(result)
            else:
                stack.append(token)

        return result

