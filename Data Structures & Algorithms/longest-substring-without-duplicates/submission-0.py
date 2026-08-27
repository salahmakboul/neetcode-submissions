class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest =0
        right =0 
        left =0 
        s_set =set()
        
        for right in range(len(s)):
            while s[right] in s_set :
                s_set.remove(s[left])
                left+=1

            
            s_set.add(s[right])
            window_size=right - left + 1
            longest= max(longest,window_size)
        return longest
            

                


        