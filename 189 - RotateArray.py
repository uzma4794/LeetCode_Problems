# This takes O(1)

        # if k is given out of range 
        k = k % len(nums) 

        #reverse whole array of given nums
        l , r = 0 , len(nums)-1
       
        while l < r:
           nums[l], nums[r] = nums[r], nums[l]
           l+=1
           r -=1
       # Reverse first part upto k  
        l , r = 0 , k-1
        while l < r :
           nums[l], nums[r] = nums[r], nums[l]
           l+=1
           r -=1
        # reverse rest of the part 
        l , r = k , len(nums)-1
        while l < r :
           nums[l], nums[r] = nums[r], nums[l]
           l+=1
           r -=1
        