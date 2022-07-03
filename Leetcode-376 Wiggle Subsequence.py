class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        arr=[[0,0] for e in nums]
        out=0
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    arr[i][0]=max(arr[i][0],arr[j][1]+1)
                elif nums[i]<nums[j]:
                    arr[i][1]=max(arr[i][1],arr[j][0]+1)
            out=max(out,max(arr[i]))
        #print(arr)
        return out+1
