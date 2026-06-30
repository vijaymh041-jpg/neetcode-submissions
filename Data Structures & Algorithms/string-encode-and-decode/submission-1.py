class Solution:

    def encode(self, strs: List[str]) -> str:
        reword=''
        if len(strs)==0:
            return " "

        for i in range(len(strs)):
            letter=list(strs[i])
            for j in range(len(letter)):
                buff=chr(ord(letter[j])+1)
                reword+=buff
            reword+=" "
        
        return reword

    def decode(self, s: str) -> List[str]:
        letter=s.split()
        decoded=[]
        reword1=''
        if s==" ":
            return[""]

        for i in range(len(letter)):
            word=list(letter[i])
            for j in range(len(word)):
                buff=chr(ord(word[j])-1)
                reword1+=buff
            decoded.append(reword1)
            reword1=""
        
        return decoded