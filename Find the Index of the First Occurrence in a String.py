#My solution

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
      #Iterates over each char in string up until the point where the 'needle' will no longer fit in the string.
        for i in range(len(haystack) - length + 1):
            if haystack[i:i+length] == needle:
                return i
        return -1
