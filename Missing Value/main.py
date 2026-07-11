class Solution:

    # nlogn becuase of sorting
    def missingNumber_nlogn(self, nums: list[int]) -> int:

        nums.sort()

        for i in range(len(nums)):
            if i != nums[i]:
                return(i)
                break

        if nums[-1] != len(nums):
            return(len(nums))
    
    # No sorting or loop O(1) solution basic maths
    def missingNumber_O1(self, nums: list[int]) -> int:

        sum_of_range = sum(range(len(nums)+1))

        sum_of_list = sum(nums)

        missing_value = sum_of_range - sum_of_list

        return missing_value
    
# Example
list = [0,1]
sol = Solution()

print(sol.missingNumber_nlogn(list))

print(sol.missingNumber_O1(list))