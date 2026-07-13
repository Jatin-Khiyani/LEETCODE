class Solution:
    def smallerNumbersThanCurrent_WorstSol(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums) 

        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i == j:
                    continue 
                elif nums[i]>nums[j]:
                    ans[i] = ans[i] + 1
                else:
                    continue
        return ans
    
    def smallerNumbersThanCurrent_nlognSol(self, nums: list[int]) -> list[int]:

        temp = sorted((nums))

        hashmap = {}

        ans = []

        for i in range(0,len(temp)):
            if temp[i] not in hashmap:
                hashmap.update({temp[i]:i})

        for i in range(0,len(nums)):
            ans.append(hashmap[nums[i]])

        return ans


# Example

sol = Solution()

print(sol.smallerNumbersThanCurrent_WorstSol([8,1,2,2,3]))
print(sol.smallerNumbersThanCurrent_nlognSol([8,1,2,2,3]))


        








        