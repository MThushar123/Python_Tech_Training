def is_valid_anagram(s, t):
    if len(s) != len(t):
        return False

    count = [0] * 26

    for char_s, char_t in zip(s, t):
        count[ord(char_s) - ord('a')] += 1
        count[ord(char_t) - ord('a')] -= 1

    return all(x == 0 for x in count)

print(" Anagram Checker")
print("String 1:")
s = input().strip()
print("String 2:")
t = input().strip()

result = is_valid_anagram(s, t)
print(f"\n'{s}' + '{t}' → {'ANAGRAM!' if result else 'NOT ANAGRAM!'}")

print(f"Sorted s: {sorted(s)}")
print(f"Sorted t: {sorted(t)}")
