#The function accepts a string ‘str’ as its argument. 
# The function needs to return the transformed string by replacing all occurrences of the character ‘a’ with the character ‘b’ and vice versa

def string_replace(string):
    string_length = len(string)
    print("Length of String is - ",string_length)

    new_string = string.maketrans({'a':'b','b':'a'})
    new_string = string.translate(new_string)
    print(new_string)

string = input("Enter the strings in the form of 'a' and 'b' --->")
string_replace(string)