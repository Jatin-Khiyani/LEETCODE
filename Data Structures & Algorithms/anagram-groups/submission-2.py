
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}
        
        for string in strs:
            
            count = [0] * 26

            for letter in string:

                letter_num = ord(letter) - ord("a") # ASCII Letter a = 0

                count[letter_num] += 1

            key = tuple(count) # List cannot be key for a dict

            if key not in hashmap:
                hashmap[key] = [string]
            else:
                hashmap[key].append(string)
        
        return list(hashmap.values())