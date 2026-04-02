class Solution:
    def isPalindrome(self, s: str) -> bool:
      #converts all chars in string to lowercase and then creates a new string containing only the alphanumeric characters 
        s = s.lower()
        new = ''.join(char for char in s if char.isalnum())
    #if else statement checks whether the reversed string is identical to the original string and returns true or false accordingly 
        if new[::-1] == new:
            return True
        else:
            return False
