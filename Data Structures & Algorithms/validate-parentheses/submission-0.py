class Solution:
    def isValid(self, s: str) -> bool:
        array_set={
            '[':']',
            '{':'}',
            '(':')'
        }
        result =[]

        for i in s :
            if i in array_set :
                result.append(i)
            else :
                if not result or array_set[result[-1]] != i :
                    return False 
                else :
                    result.pop()
        return len(result)==0

               
            



        