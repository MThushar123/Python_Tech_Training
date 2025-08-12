#permutations of a string

def permutation_string(string,prefix=""):
    n = len(string)
    
    if n ==0:
        print(prefix)
    else:
        for i in range(n):
            new_string = string[:i] + string[i+1:]
            permutation_string(new_string,prefix+string[i])
    
string = input("Enter a String to get permutation of it -->")
permutation_string(string)