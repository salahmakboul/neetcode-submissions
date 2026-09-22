import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # 1. SETUP: Count exactly what we need from 't'
        target_counts = collections.Counter(t)
        window_counts = {}
        
        # 'need' is how many UNIQUE characters we must satisfy.
        # 'have' is how many unique characters we currently satisfy.
        need = len(target_counts)
        have = 0
        
        left = 0
        min_len = float('inf')
        start_idx = 0
        
        # 2. EXPAND: Move 'right' to find a valid window
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If adding this char hits the exact required amount, we satisfied one more requirement
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1
            
            # 3. SHRINK: While the window is valid, try to make it smaller
            while have == need:
                # Record the shortest valid window we've seen
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    start_idx = left
                
                # Remove the left character to shrink the window
                left_char = s[left]
                window_counts[left_char] -= 1
                
                # If removing it drops us below the required amount, the window is now invalid
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    have -= 1
                    
                left += 1
                
        # 4. RETURN: If we found a valid window, slice it. Otherwise, return ""
        return s[start_idx : start_idx + min_len] if min_len != float('inf') else ""