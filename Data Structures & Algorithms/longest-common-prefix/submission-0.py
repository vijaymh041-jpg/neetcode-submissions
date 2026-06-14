class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        string=''
        for j in range(min(len(strs[i]),len(strs[i+1]))):
            if strs[i][0]==strs[i+1][0]:
                if strs[i][j]==strs[i+1][j]:
                    string+=strs[i][j]
            
        return string
        
        