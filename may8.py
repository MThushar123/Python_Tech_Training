def customSortString(order, s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    result = []
    for char in order:
        if char in count:
            result.append(char * count[char])
            del count[char]

    for char, freq in count.items():
        result.append(char * freq)
    
    return ''.join(result)

def main():
    order = input("Enter order string: ").strip()
    s = input("Enter string to sort: ").strip()
    
    result = customSortString(order, s)
    print(f"Sorted string: {result}")

if __name__ == "__main__":
    main()