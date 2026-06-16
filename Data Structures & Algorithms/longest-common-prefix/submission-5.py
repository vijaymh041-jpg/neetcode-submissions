class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string=''
        liso=[]
        for i in range(1):
            for j in range(len(strs[i])):
                if j<len(strs):
                    if strs[i][j]==strs[i+1][j]:
                        liso.append(strs[i][j])
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

        
            
            

        