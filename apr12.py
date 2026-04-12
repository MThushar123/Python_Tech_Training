def count_segments(s):
    return len(s.split())
print("Enter the sentence")
s = input().strip()
print(f'Input: "{s}"')
print(f'Segments: {count_segments(s)}')