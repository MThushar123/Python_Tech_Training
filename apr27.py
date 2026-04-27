def repeatedStringMatch(a, b):
    if not b:
        return 0

    max_repeats = (len(b) + len(a) - 1) // len(a) + 1
    
    repeated = ""
    count = 0
    
    for i in range(max_repeats):
        if b in repeated + a:
            return count + 1
        repeated += a
        count += 1
    
    return -1

def main():
    a = input("Enter string A: ").strip()
    b = input("Enter string B: ").strip()
    
    result = repeatedStringMatch(a, b)
    print(f"Minimum repetitions needed: {result}")

if __name__ == "__main__":
    main()