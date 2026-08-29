import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(b / a) 
        }
        for token in tokens :
            if token not in ops :
                stack.append(int(token))
            if token in ops :
                num1=stack.pop()
                num2=stack.pop()
                result =ops[token](num1,num2)
                stack.append(result)
        return stack[0]


        
        