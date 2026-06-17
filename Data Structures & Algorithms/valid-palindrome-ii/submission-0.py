class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[:]==s[::-1]:
            return True
        count=0
        i=0
        j=len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                count+=1
            if count>1:
                return False
            i+=1
            j-=1
        return True


        