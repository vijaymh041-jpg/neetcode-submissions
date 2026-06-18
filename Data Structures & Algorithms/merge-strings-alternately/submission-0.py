class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_word=''
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            if i>len(word1):
                final_word=final_word+word2[j]
            elif j>len(word2):
                final_word=final_word+word1[i]
            else:
                final_word=final_word+word1[i]+word2[j]    
            i+=1
            j+=1
        return final_word