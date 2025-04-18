class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # This approach will use two pointer approach
        # it will swap right values with left values until both pointers come to the same point, move pointer left to the right and move right pointer to the left
        left, right = 0, len(s)-1

        while left <= right:
              s[left],s[right] = s[right] , s[left]
              left +=1
              right -=1
