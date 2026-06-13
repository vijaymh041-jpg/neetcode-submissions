class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        liso=[]
        res=[]
        if len(strs)==1:
            liso.append(strs)
            return liso
        i=0
        j=1
        # for i in range(len(strs)):
        #     for j in range(len(strs)):
        #         if sorted(strs[i])==sorted(strs[j]):
        #             liso.append(strs[j])
        #     if liso not in res:        
        #         res.append(liso)
        #     liso=[]
        # return res


        while len(strs)>0 and j<len(strs):
            if sorted(strs[i])==sorted(strs[j]):
                liso.append(strs[j])
                strs.pop(j)
            j+=1
            if j==len(strs)-1:
                i+=1
                j=i+1
            res.append(liso)
        
        return res
        