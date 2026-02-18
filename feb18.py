# Numbers 0-19 (special cases)
ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
        "seventeen", "eighteen", "nineteen"]

# Tens place
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def number_to_words(num):
    if 0 <= num <= 19:
        return ones[num]
    elif 20 <= num <= 99:
        ten = num // 10      # Tens digit
        one = num % 10       # Ones digit
        if one > 0:
            return tens[ten] + " " + ones[one]
        else:
            return tens[ten]
    else:
        return "Number must be between 0-99"

print("Enter a number (0-99):")
num = int(input().strip())
result = number_to_words(num)
print(f"{num} → {result}")
