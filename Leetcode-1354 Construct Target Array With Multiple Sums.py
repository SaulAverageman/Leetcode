class Solution:
    def isPossible(self, array: List[int]) -> bool:
        length=len(array)
        total_sum=0
        for i in range(length):
            total_sum+=array[i]
            array[i]=-array[i]
        heapq.heapify(array)
        while total_sum>length:
            largest_element=-heappop(array)
            remainder_sum=total_sum-largest_element
            if remainder_sum<=0:
                return 0
            times=max(1,(largest_element//remainder_sum)-1)
            new_element=largest_element-(times*remainder_sum)
            
            if new_element<=0:
                return 0
            total_sum1=total_sum
            total_sum-=largest_element
            total_sum+=ne
            if total_sum==total_sum1:
                break
            heapq.heappush(array,-new_element)
            #print(t,st)
        if total_sum==length:
            return 1
        return 0
