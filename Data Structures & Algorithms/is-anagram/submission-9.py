class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=list(s)
        if len(s)!=len(t):
            return False
        for i in t:
            if i in s_list:
                s_list.remove(i)
            else:
                return False
        if s_list==[]:
            return True

                
        