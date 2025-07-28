class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)   # this si goign to remove dupliactes as set automatically remove duplicates
        longest = 0
        for num in mySet:
            if (num-1) not in mySet:
                length=0            # to check whether element is first element
                while (num+length) in mySet:
                    length+=1

                longest = max(length,longest)

        return longest
