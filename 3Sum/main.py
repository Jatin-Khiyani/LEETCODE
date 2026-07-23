class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        ans = []

        for i, value in enumerate(nums):
            if i > 0 and value == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = value + nums[r] + nums[l]

                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    ans.append([value, nums[r], nums[l]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return ans


Example = Solution()

print(Example.threeSum([-1, 0, 1, 2, -1, -4]))
