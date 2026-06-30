from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        reword = ''
        for i in range(len(strs)):
            letter = list(strs[i])
            for j in range(len(letter)):
                buff = chr(ord(letter[j]) + 1)
                reword += buff
            reword += " "
        
        return reword

    def decode(self, s: str) -> List[str]:
        # Cleaned up: split 's' by spaces and drop the last trailing empty element
        encoded_words = s.split(" ")[:-1]
        
        # FIX: Define the empty list so Python knows what 'decoded' is!
        decoded = [] 
        
        for i in range(len(encoded_words)):
            letter = list(encoded_words[i])
            reword1 = ''
            for j in range(len(letter)):
                buff = chr(ord(letter[j]) - 1)
                reword1 += buff
            decoded.append(reword1)
        
        return decoded