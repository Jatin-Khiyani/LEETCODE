class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        ans = []

        for index,value in enumerate(nums):
            difference = target - value
            if difference in hashmap:
                ans.append(hashmap[difference])
                ans.append(index)
            else:
                hashmap[value] = index

        return ans



        