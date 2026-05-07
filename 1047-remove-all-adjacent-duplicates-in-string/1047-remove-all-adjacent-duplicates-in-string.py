class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for curr in s:
            if stack and curr==stack[-1]:
                stack.pop()
            else:
                stack.append(curr)
        return "".join(stack)