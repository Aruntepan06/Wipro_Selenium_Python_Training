empty_list=[]
numbers=[1,2,3,4,5,6,7,8,9]
mixed_data=[1,"Hello",True,6.67]
nested =[[1,2],[3,4]]


fruits=["apple","banana","mango"]
for idx,fruit in enumerate(fruits,start=1):
    print(idx,fruit)

numbers.insert(3,16)
print(numbers)
numbers.sort()
print(f"Numbers List after sorting:{numbers}")

fruits.reverse()
print(fruits)

# slicing
nums=[1,2,3,4,5,6,7,8,9]
odd_nums=[3,5,7,9]
print(nums[5:])

print(nums[: 5])

print(nums[ : ])
nums[:5]
nums.sort()
print(nums)
#extend
nums.extend(odd_nums)
print(nums)