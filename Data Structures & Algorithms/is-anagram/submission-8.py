class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list=list(s)
        for i in t:
            if i in s_list:
                s_list.remove(i)
            elif len(s)!=len(t):
                return False
            else:
                return False
        if s_list==[]:
            return True

                
        