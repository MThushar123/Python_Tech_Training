#_________Fibannoci series using dynamic programming___________

def fibannoci_dynamic_programming(number):
    if number == 0 or number == 1:
        return number
    else:
        dp = [0] * (number + 1)
        dp[1] = 1
        for i in range(2,number +1):
            dp[i] = dp[i-1] + dp[i-2]
    return dp[number]

number = int(input("Enter the Fibannoci number --- "))
print("Fibannoci series using Dynamic Programming",fibannoci_dynamic_programming(number))        