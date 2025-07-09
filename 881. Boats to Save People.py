class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
       
        people.sort()              # this part sorts the array by 0(nlog n ) time complexity 

        boats = 0
                           
        left, right = 0, len(people)-1

        while left <= right:             
            remaining = limit - people[right]                #adjust heavy weight poeple first 
            right -= 1
            boats += 1
            if left<=right and remaining >= people[left]:       # if there is capacity to enter people add them 
                left +=1
        return boats
