class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=0
        for i in range(len(t)):
            if t[i] in s:
                count+=1
        if count==len(t):
            return True
        else:
            return False
                
        