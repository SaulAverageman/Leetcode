class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s):
            for i in range(len(s)):
                if s[i]!=s[len(s)-1-i]:
                    return 2
            return 1
        return 0