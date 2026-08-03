from collections import Counter

def customSortString(order, s):
    freq = Counter(s)
    result = []

    for ch in order:
        if ch in freq:
            result.append(ch * freq[ch])
            del freq[ch]

    for ch, count in freq.items():
        result.append(ch * count)

    return "".join(result)

order = input("Enter custom order string: ")
s = input("Enter string to sort: ")

result = customSortString(order, s)

print("Custom Sorted String:", result)