def backspaceCompare(s, t):
    def process_string(string):
        stack = []
        for char in string:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
    return process_string(s) == process_string(t)

def main():
    s = input("Enter string S: ").strip()
    t = input("Enter string T: ").strip()
    
    result = backspaceCompare(s, t)
    print(f"Strings match: {result}")

if __name__ == "__main__":
    main()