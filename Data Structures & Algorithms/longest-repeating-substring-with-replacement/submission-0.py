class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right =0 
        left = 0
        longest = 0
        s_set={}
        for right in range(len(s)) :
            if s[right] in s_set :
                s_set[s[right]] +=1
            else :
                s_set[s[right]]=1
             
            window_size = right - left +1
            max_frequency=max(s_set.values())
            Odds=  window_size - max_frequency
            while Odds> k :
                s_set[s[left]]-=1
                left+=1
                window_size = right - left +1
                max_frequency=max(s_set.values())
                Odds=window_size - max_frequency
            longest=max(longest,window_size)
        return longest



        