class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        arr=[0]*len(nums)
        
        q=[]
        s=set()
        for i in range(len(nums)-1,-1,-1):
            if i+k+1<len(nums):
                s.add((-nums[i+k+1],i+k+1))
            while len(q)!=0 and q[0] in s:
                heapq.heappop(q)
            if len(q)!=0:
                x=q[0]
                nums[i]+=-x[0]
            heapq.heappush(q,(-nums[i],i))
            #print(i,q,s)
        #print(nums)
        return nums[0]
