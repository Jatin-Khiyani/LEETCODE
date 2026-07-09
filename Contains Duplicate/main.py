class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Changing the list to set as sets cannot store duplicates
        nums_set = set(nums)

        ''' 
        Sets will only store the first 
        occurance of the number, if another is present in the list it will remove
        it and the length of the set will become shorter
        '''
        if len(nums_set) != len(nums):
            return True
        else:
            return False
        
## Example run 

sol = Solution()

print(sol.containsDuplicate([2,3,2,1]))
