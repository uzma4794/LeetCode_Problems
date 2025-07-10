class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []      
        for i , a in enumerate(nums):   
            if i > 0 and a == nums[i - 1]:    # This ensures no two elements are same are selected. 
                continue

            l, r = i + 1, len(nums) - 1         # Two sum Array    

            while l < r:
                threesum1 = a + nums[l] + nums[r]
                if threesum1 >  0:
                    r-=1
                elif threesum1 < 0:
                    l+=1 
                else: 
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1   
                   
        return res