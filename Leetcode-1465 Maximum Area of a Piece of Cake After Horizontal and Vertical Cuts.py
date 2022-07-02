class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        def max_cut(arr,last):
            arr.sort()
            cut_max=0
            prev=0
            for e in arr:
                cut_max=max(cut_max,e-prev)
                prev=e
            cut_max=max(cut_max,last-prev)
            return cut_max
        
        return (max_cut(horizontalCuts,h)*max_cut(verticalCuts,w))%(1000000007)
