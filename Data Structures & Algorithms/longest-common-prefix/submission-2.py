class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string=''
        for i in range(1):
            for j in range(len(strs[i])):
                if strs[i][j]==strs[i+1][j]:
                    string+=strs[i][j]
                else:
                    break
        return string

        
            
            

        