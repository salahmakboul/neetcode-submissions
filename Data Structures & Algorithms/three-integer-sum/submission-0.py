class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. SORTING
        # Why: The two-pointer trick ONLY works if numbers are ordered. 
        # It also puts duplicates next to each other so we can skip them.
        nums.sort()
        
        # 2. INITIALIZATION
        # Why: You need an empty list to store results. [[]] creates a list with one empty list inside, which is wrong.
        record = []
        
        # 3. THE OUTER LOOP (Fixing the first number)
        # Why: We need to try every number as the "first" number of the triplet.
        for i in range(len(nums) - 2):
            
            # 4. SKIP DUPLICATE 'FIRST' NUMBERS
            # Why: If nums[i] is the same as the previous one, we already checked all its combinations.
            # This prevents duplicate triplets like [-1, 0, 1] appearing twice.
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 5. SETTING POINTERS
            # Why: 'left' starts right after 'i'. 'right' starts at the very end.
            left = i + 1
            right = len(nums) - 1
            
            # 6. THE INNER LOOP (The Engine)
            # Why: 'left' and 'right' must walk toward each other to test different sums.
            while left < right:
                
                # 7. CALCULATE SUM
                # Bug Fix: You used 'num' instead of 'nums'. Also, use the current values.
                tr_s = nums[i] + nums[left] + nums[right]
                
                if tr_s < 0:
                    # Why: Sum is too small. Move 'left' right to get a bigger number.
                    left += 1
                elif tr_s > 0:
                    # Why: Sum is too big. Move 'right' left to get a smaller number.
                    right -= 1
                else:
                    # tr_s == 0: We found a valid triplet!
                    
                    # 8. RECORD THE TRIPLET
                    # Bug Fix: Append the actual VALUES, not the indices [i, left, right].
                    record.append([nums[i], nums[left], nums[right]])
                    
                    # 9. SKIP DUPLICATES FOR LEFT AND RIGHT
                    # Why: If the next number is the same, we'll just find the same triplet again.
                    # These MUST be inside the 'else' block.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 10. MOVE POINTERS INWARD
                    # Why: We finished with this pair. Move both to search for the next unique pair.
                    left += 1
                    right -= 1
                    
        return record