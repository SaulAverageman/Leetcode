class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:[-x[0],x[1]])
        out=[]
        
        for e in people:
            out.insert(e[1],e)
        
        return out
