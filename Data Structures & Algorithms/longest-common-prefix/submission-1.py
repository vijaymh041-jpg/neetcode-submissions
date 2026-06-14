class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        liso=[]
        i=0
        string=''
        for j in range(min(len(strs[i]),len(strs[i+1]))):
            if i<len(strs):
                if strs[0][0]!=strs[1][0]:
                    return ""

                if strs[i][j]==strs[i+1][j]:
                    liso.append(strs[i][j])
                    string+=strs[i][j]

                
        return string

        