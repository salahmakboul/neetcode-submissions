class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        n = len(nums)
       
        left_P=1
        for i in range(n):
            output.append(left_P)
            left_P*=nums[i]
        
        right_P=1
        for i in range(n-1,-1,-1):
            output[i]*=right_P
            right_P*=nums[i]
        
        return output
            

        

            

        