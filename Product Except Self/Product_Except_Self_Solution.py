class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        Left = [1] * (len(nums))
        Right = [1] * (len(nums))
        answer =[]
        for i in range(1,len(nums)):
            Left[i] = Left[i-1] * nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            Right[j] = Right[j+1] * nums[j+1]
        for i in range(len(nums)):
            answer.append(Left[i]*Right[i])
        return answer 

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
