def is_perfect(num):
    if num <= 1:
        return False
    
    divisor_sum = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i and num // i != num:
                divisor_sum += num // i
    
    return divisor_sum == num
print("enter the number")
num = int(input().strip())
print(f'Input: {num}')
print(f'Is perfect: {is_perfect(num)}')