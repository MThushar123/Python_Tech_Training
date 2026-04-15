def is_subsequence(s, t):
    i = 0
    for c in t:
        if i < len(s) and s[i] == c:
            i += 1
    return i == len(s)
print("Enter the string")
s = input("Enter s: ").strip()
t = input("Enter t: ").strip()
print(f's="{s}", t="{t}"')
print(f'Is subsequence: {is_subsequence(s, t)}')