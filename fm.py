class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        ans = []
        
        for i in range(len(nums)):   
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] = nums[temp]*(-1)
                
        for i in range(len(nums)):      
            if nums[i] > 0:      
                ans.append(i+1)
                
                
        return ans
