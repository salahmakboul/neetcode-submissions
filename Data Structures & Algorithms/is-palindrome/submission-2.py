class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_string = ""
        for i in s :
            if i.isalnum():
                final_string += i.lower()
        reversed_string=final_string[::-1]
        if final_string == reversed_string :
            return True
        return False

        