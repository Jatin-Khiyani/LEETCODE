class Solution:
    def findDisappearedNumbers_worstsol(self, nums: list[int]) -> list[int]:

        len_of_list = len(nums)

        nums = list(set(nums))

        missing_num = []

        for i in range(0,len_of_list):
            if len(nums)-1 >= i: 
                if i+1 == nums[i]:
                    continue
                else:
                    nums.insert(i,i+1)
                    missing_num.append(i+1)
            else: 
                nums.insert(i,i+1)
                missing_num.append(i+1)
                    
        return missing_num
    
    def findDisappearedNumbers_bestsol(self, nums: list[int]) -> list[int]:

        nums_set = set(nums)

        missing_num = []

        for i in range(1,len(nums)+1):

            if i not in nums_set:
                missing_num.append(i)
        
        return missing_num


# Example 

nums = [1,1]

sol = Solution()

ans_bestsol = sol.findDisappearedNumbers_bestsol(nums)

ans_worstsol = sol.findDisappearedNumbers_worstsol(nums)

print("Best Solution Answer: ",ans_bestsol)

print("Worst Solution Answer: ",ans_worstsol)
