class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
            
        # Structure target_counts properly as {char: frequency}
        target_counts = {}
        for c in t:
            target_counts[c] = target_counts.get(c, 0) + 1
            
        window_counts = {}
        min_len = float('inf')
        start_idx = 0
        left = 0
        
        # Proper sliding window loop structure
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check window validity and shrink
            while all(window_counts.get(k, 0) >= target_counts[k] for k in target_counts):
                current_len = right - left + 1
                if current_len < min_len:
                    min_len = current_len
                    start_idx = left
                    
                left_char = s[left]
                window_counts[left_char] -= 1
                if window_counts[left_char] == 0:
                    del window_counts[left_char]
                left += 1
                
        return "" if min_len == float('inf') else s[start_idx:start_idx + min_len]
