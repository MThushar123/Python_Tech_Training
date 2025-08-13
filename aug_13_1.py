#Have the function Division (num1, num2) take both parameters being passed and return the Greatest Common Factor. 
# That is, return the greatest number that evenly goes into both numbers with no remainder. 
# For example: 12 and 16 both are divisible by 1, 2. and 4 so the output should be 4. The range for both parameters will be from 1 to 10^3

def Greatest_common_factor(num1,num2):
    if num1 == 0 and num2 == 0:
        print("Can't Find for ZERO")
    else:
        if num1 <num2:
            num1,num2 = num2,num1
        while num2!=0:
            remainder = num1 % num2
            num1 = num2    
            num2 = remainder
        print(f"THE GCF OF TWO NUMBER ARE ---> {num1}")    

num1 = int(input("Enter the NUM_1 value to check Greatest Common Factor ---> "))
num2 = int(input("Enter the NUM_2 value to check Greatest Common Factor --->"))
Greatest_common_factor(num1,num2)