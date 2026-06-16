class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in range(0,len(s)):
            if s[i].isalnum():
                if s[i]!=' ' and ord(s[i])>64 and ord(s[i])<123:
                    if ord(s[i])>96:
                        arr.append(chr(ord(s[i])-32))
                    elif ord(s[i])>96 and ord(s[i])<123:
                        arr.append(s[i])
                    else:
                        arr.append(s[i])

        if arr[:]==arr[::-1]:
            return True
        else:
            return False
            



        