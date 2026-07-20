nums = [-4, -1, 0, 3, 10]

first = 0
last = len(nums) - 1
ans = []


while first <= last:
    if abs(nums[first]) > abs(nums[last]):
        ans.append(nums[first] * nums[first])
        first += 1
    else:
        ans.append(nums[last] * nums[last])
        last -= 1


print(ans[::-1])
