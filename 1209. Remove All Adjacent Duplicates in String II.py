class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:   #  If stack is not empty, and The last character in stack (stack[-1][0]) is same as current character c,
                stack[-1][1] +=1
            else:
                stack.append([c,1])
            
            if stack[-1][1] == k:
                stack.pop()
        res = ""
        for char, count in stack:
            res+= (char*count)
        return res