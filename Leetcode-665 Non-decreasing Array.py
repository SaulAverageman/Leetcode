class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n2=nums.copy()
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                nums[i]=nums[i-1]
                n2[i-1]=n2[i]
                break

        def ck(arr):
            for i in range(1,len(arr)):
                if arr[i-1]>arr[i]:
                    return 0
            return 1
        
        return ck(nums) or ck(n2)
