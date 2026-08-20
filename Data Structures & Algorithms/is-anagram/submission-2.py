class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_string1=''.join(sorted(s))
        sorted_string2=''.join(sorted(t))
        if len(s) != len(t): return False
        for i in range(len(sorted_string1)) :
            if sorted_string1[i]!=sorted_string2[i]:
                return False
        return True

        