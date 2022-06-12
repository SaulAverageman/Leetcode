class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        arr=[0]
        for e in nums:
            arr.append(arr[-1]+e)
        out=0
        di=[-1]*max(nums)
        i=0
        for j in range(len(nums)):
            if di[nums[j]-1]!=-1:
                if i-1<di[nums[j]-1]:
                    i=di[nums[j]-1]
            out=max(out,arr[j+1]-arr[i])
            #print(out,i,j+1)
            di[nums[j]-1]=j+1
        return out
