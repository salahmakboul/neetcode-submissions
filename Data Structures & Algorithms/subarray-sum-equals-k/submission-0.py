class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =0
        sted={0:1}
        current_prefix=0

        for i in range(len(nums)):
            current_prefix+=nums[i]
            complement = current_prefix - k
            if complement in sted:
                count+=1
            if var in sted:
                count += 1
            else:
                sted[var] = 1
        
        return count

            
            
        