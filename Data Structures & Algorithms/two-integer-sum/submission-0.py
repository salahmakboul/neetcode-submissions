class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums={}
        for i,j in enumerate(nums):
            comp=target - j 
            if comp in sums :
                return [sums[comp],i]
            else :
                sums[j] = i


            
