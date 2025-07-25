# linear search
def linear_search(nums,target):
    nums_length  = len(nums)
    for value in range(nums_length):
        if nums[value] == target:
            print("Value found at position ",value+1)
            return
    print("VAlue not in the array")

nums = [1,2,3,4,5,6,7,8,9,10]
target = 5
linear_search(nums,target)