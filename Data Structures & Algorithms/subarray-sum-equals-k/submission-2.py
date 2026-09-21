class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =0
        sted={0:1}
        current_prefix=0

        for i in range(len(nums)):
            current_prefix+=nums[i]
            complement = current_prefix - k
            if complement in sted:
                count += sted[complement]
            if current_prefix in sted:
                sted[current_prefix] += 1
            else:
                sted[current_prefix] = 1
        
        return count

            
            
        