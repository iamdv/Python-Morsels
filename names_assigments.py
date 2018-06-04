nums = [1,2,3,4]

print(nums)

others = nums

nums.append(5)

others.append(6)

# print(nums)

# print(others)

# print(id(nums[0]))

# print(id(others[0]))

for x in nums:
  print(id(x))
  print(id(nums[0]))
  print(id(others[0]))