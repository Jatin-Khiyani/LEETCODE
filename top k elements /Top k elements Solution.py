class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for element in nums:
            count[element] = count.get(element, 0) + 1
        sorted_count = sorted(count.items(),key = lambda x: x[1], reverse =True)
        top_k = []
        for i in range(k):
            key = sorted_count[i][0]
            top_k.append(key)
        return top_k

        
sol = Solution()
top_k_list = sol.topKFrequent([3,3,4,4,2,2,1],3)
print(top_k_list)
