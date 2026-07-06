class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        temp=0
        count=0
        result=0
        for i in range(len(people)):
            if people[i]!=0:
                diff=limit-people[i]
            if diff>0 and diff in people:
                people[people.index(diff)]=0
                people[i]=0
        for j in range(len(people)):
            if people[j]!=0:
                temp+=1
            else:
                count+=0.5
        result=temp+count
        return int(result)

        


        