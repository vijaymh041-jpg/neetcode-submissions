class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=0
        temp=0
        for i in range(len(people)):
            if people[i]>0:
                diff=limit-people[i]
            if diff>0 and diff in people:
                index=people.index(diff)
                people[index]=0
                people[i]=0
        for i in range(len(people)):
            if people[i]!=0:
                temp+=1 
            else:
                count+=0.5

        return int(count+temp)
        


        