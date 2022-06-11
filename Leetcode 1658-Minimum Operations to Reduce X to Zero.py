class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i=0
        x=sum(nums)-x
        w=nums[i]
        j=i+1
        out=1000000
        if x==0:
            out=len(nums)
        while i<=j:
            if i==len(nums):
                break
            if w==x:
                print(i,j)
                out=min(out,len(nums)-(j-i))
                w-=nums[i]
                i+=1
            elif w>x:
                w-=nums[i]
                i+=1
            else:
                if j==len(nums):
                    break
                w+=nums[j]
                j+=1
        return out if out!=1000000 else -1
