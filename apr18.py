from collections import Counter

def longest_harmonious(nums):
    freq = Counter(nums)
    max_len = 0
    
    for num, count in freq.items():
        if num + 1 in freq:
            max_len = max(max_len, count + freq[num + 1])
    
    return max_len
print("Enter the number")
nums = list(map(int, input().strip().split()))
print(f'Input: {nums}')
print(f'Longest harmonious: {longest_harmonious(nums)}')