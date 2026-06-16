class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string=''
        liso=[]
        
        for j in range(len(strs[0])):
            if j<len(strs):
                if strs[0][j]==strs[1][j]:
                    liso.append(strs[0][j])
                else:
                    break
        k=0
        for i in range(0,len(liso)):
            if len(liso)>0 and liso[i]!=strs[k][i]:
                liso.pop(i)
            k+=1
        for j in range(len(liso)):
            string+=liso[j]

        return string

        
            
            

        