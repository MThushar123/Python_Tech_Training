def rotatedDigits(n):
    valid = set('01689')
    rotate = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    
    def is_good(num_str):
        rotated = []
        has_rotation = False
        
        for char in num_str:
            if char not in valid:
                return False
            rotated_char = rotate[char]
            if rotated_char != char:
                has_rotation = True
            rotated.append(rotated_char)
        
        return has_rotation
    
    count = 0
    for i in range(1, n + 1):
        if is_good(str(i)):
            count += 1
    
    return count

def main():
    n = int(input("Enter n: ").strip())
    result = rotatedDigits(n)
    print(f"Count of rotated digits from 1 to {n}: {result}")

if __name__ == "__main__":
    main()