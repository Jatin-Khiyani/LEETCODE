
class Solution:
    def twoSum_WorstSol(self, nums: list[int], target: int) -> list[int]:
        ans = []
        for i in range(0,len(nums)):

            for j in range(i+1,len(nums)):
                
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
        return ans
    def twoSum_BestSol(self, nums: list[int], target: int) -> list[int]:

        hashmap = {}

        ans = []

        for i in range(0,len(nums)):
            
            diff = target - nums[i]

            if diff not in hashmap:

                hashmap.update({nums[i]:i})

            else:
                ans.append(hashmap[diff])
                ans.append(i)
        
        return ans
    


    
sol = Solution()

print("Worst Solution for the input [3,2,4],6 ",sol.twoSum_WorstSol([3,2,4],6))
print("Worst Solution for the input [3,3],6 ",sol.twoSum_WorstSol([3,3],6))

print("Best Solution for the input [3,2,4],6 ",sol.twoSum_BestSol([3,2,4],6))
print("Best Solution for the input [3,3],6 ",sol.twoSum_BestSol([3,3],6))
                
