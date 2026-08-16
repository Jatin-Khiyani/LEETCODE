
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)
        
        for string in strs:
            
            count = [0] * 26

            for letter in string:

                letter_num = ord(letter) - ord("a") # ASCII Letter a = 0

                count[letter_num] += 1

            hashmap[tuple(count)].append(string)
        
        return list(hashmap.values())