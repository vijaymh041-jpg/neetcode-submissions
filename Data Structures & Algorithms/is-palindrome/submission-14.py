class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in range(len(s)):
            if s[i].isalnum():
                if s[i].isupper():
                    arr.append(s[i].lower())
                else:
                    arr.append(s[i])    
        if arr[:]==arr[::-1]:
            return True
        else:
            return False