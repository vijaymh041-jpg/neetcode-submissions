class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for i in range(0,len(s)):
            if s[i]!=' ' and ord(s[i])>64 and ord(s[i])<123:
                if ord(s[i])>96:
                    arr.append(chr(ord(s[i])-32))
                else:
                    arr.append(s[i])

        if arr[:]==arr[::-1]:
            return True
        else:
            print(arr)
            print(ord('A'),",",ord('Z'),",",ord('a'),ord('z'))
            return False
            



        