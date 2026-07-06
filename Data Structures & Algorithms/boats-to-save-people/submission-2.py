class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count=len(people)
        temp=0
        for i in range(len(people)):
            if people[i]>0:
                diff=limit-people[i]
            if diff>0 and diff in people:
                index=people.index(diff)
                people[index]=0
                count-=2
                temp+=1
                people[i]=0

        return temp+abs(count)
        


        