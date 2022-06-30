class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid1=len(nums)//2
        mid2=mid1-1
        
        out1=0
        out2=0
        
        for e in nums:
            out1+=abs(nums[mid1]-e)
            out2+=abs(nums[mid2]-e)
        return min(out1,out2)
