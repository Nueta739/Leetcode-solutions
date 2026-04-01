class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        result = []
        #Initializes anagrams hashmap and result list

        for s in strs:
        #Iterates through every string in the list
            sorted_string = ''.join(sorted(s))
            
            if sorted_string in anagrams:
                anagrams[sorted_string].append(s)
              #if the string of sorted letters is already in the anagrams hashmap the current string will be appended to the list correspending to these letters 
            
            else:
                anagrams[sorted_string] = [s]
              #if the string of sorted letters is not yet a key in the anagram it will be added as a key with the value being the current string.
      
          
        
        for key in anagrams:
            result.append(anagrams[key])
        return result
      #appends each of the anagram lists to the result lists and returns.
