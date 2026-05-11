def rotate(nums, k):
    n = len(nums)
    k = k % n  

    nums.reverse()

    nums[:k] = nums[:k][::-1]

    nums[k:] = nums[k:][::-1]

def main():
    arr_input = input("Enter space-separated numbers: ").strip().split()
    nums = [int(x) for x in arr_input]
    
    k = int(input("Enter k (steps to rotate right): ").strip())
    
    print("Original:", nums)
    rotate(nums, k)
    print("Rotated:", nums)

if __name__ == "__main__":
    main()