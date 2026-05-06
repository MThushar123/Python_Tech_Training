def findNumbers(nums):
    def has_even_digits(num):
        digit_count = 0
        while num > 0:
            num //= 10
            digit_count += 1
        return digit_count % 2 == 0
    
    count = 0
    for num in nums:
        if has_even_digits(num):
            count += 1
    
    return count

def main():
    arr_input = input("Enter space-separated numbers: ").strip().split()
    nums = [int(x) for x in arr_input]
    
    result = findNumbers(nums)
    print(f"Numbers with even digits: {result}")

if __name__ == "__main__":
    main()