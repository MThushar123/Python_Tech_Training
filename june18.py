
def compress(chars):
    write = 0
    read = 0

    while read < len(chars):
        current_char = chars[read]
        count = 0

        while read < len(chars) and chars[read] == current_char:
            read += 1
            count += 1

        chars[write] = current_char
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write

chars = list(input("Enter characters without spaces: "))

new_length = compress(chars)

print("Compressed Length:", new_length)
print("Compressed Array:", chars[:new_length])