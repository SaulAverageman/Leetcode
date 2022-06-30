class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        arr=[]
        prev="a"
        count=1
        for i in range(1,len(nums)):
            x=nums[i]-nums[i-1]
            if prev=="a":
                pass
            elif x!=prev:
                arr.append(count)
                count=1
            count+=1
            prev=x
        arr.append(count)
        out=0
        
        for e in arr:
            n=e-2
            out+=(n*(n+1))//2
        return out
