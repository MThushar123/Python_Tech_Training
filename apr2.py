def find_the_difference(s, t):
    result = 0
    for char in s:
        result ^= ord(char)
    for char in t:
        result ^= ord(char)
    return chr(result)

print(" Find Extra Character")
print("String s:")
s = input().strip()
print("String t (s shuffled + extra):")
t = input().strip()

extra = find_the_difference(s, t)
print(f"\n s='{s}'")
print(f" t='{t}'")
print(f" Extra: '{extra}'")