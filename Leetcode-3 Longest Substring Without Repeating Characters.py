class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di={}
        out=0
        col=0
        for i in range(len(s)):
            if s[i] in di:
                col=min(col+1,i-di[s[i]])
            else:
                col+=1
            out=max(out,col)
            di[s[i]]=i
        return out
