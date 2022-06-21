class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr=[]
        h=[]
        for i in range(len(heights)-1):
            e=heights[i+1]-heights[i]
            if e>0:
                if len(h)<ladders:
                    heapq.heappush(h,e)
                else:
                    if len(h)>0 and h[0]<e:
                        bricks-=heapq.heappop(h)
                        heapq.heappush(h,e)
                    else:
                        bricks-=e
                if bricks<0:
                    return i
        return len(heights)-1
