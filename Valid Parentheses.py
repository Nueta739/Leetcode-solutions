class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')','[':']','{':'}'}
        stack = []
#Iterates over each character in the string, if the character is an open bracket it is pushed onto the stack.
        for char in s: 
            if char in brackets:
                stack.append(char)
#If a closed bracket is encountered then this must correspond to the last bracket on the stack, if there is no bracket on the stack or the brackets dont match then program returns False
            else:
                if stack == [] or brackets[str(stack.pop())] != char:
                    return False     

        return stack == []
        
