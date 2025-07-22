class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqT = defaultdict(int)              # hashmap for string T
        for letter in t:
            freqT[letter] +=1                  
        
        lettersToSatisfy = len(freqT)        # 3
        left , right = float('-inf') , float ('inf')   #substring 
        i = 0      
        for j, char in enumerate(s):
            if char in freqT:              # ADOBECODEBANC      ABC           T A 0 B 0 C 0 
                freqT[char] -=1                           # A D O B E C 
                if freqT[char] == 0:                        # DOBECODEB     B =-1 A = 1 C =0
                    lettersToSatisfy -= 1     # 0   i =0 , j =1 ,2, 3,4, 5 , 6,7,8,9 
            while lettersToSatisfy == 0 :    #   When all letters are satisfied (valid window)
                                              #Try to shrink the window from the left to find the minimum.


                if j -i < right -left:      
                    left , right = i,j    
                if s[i] in freqT:           
                    freqT[s[i]] +=1
                    if freqT[s[i]] >0 :
                        lettersToSatisfy +=1          
                i+=1           # i =1                

        return '' if right== float ('inf') else s[left:right+1]
       