class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xAAAAAAAA) == 0

solution = Solution()
tests = [16, 5, 1, 4, 2, 8, 0, -1, 64, 256]

print("n\tResult\tExpected")
print("-" * 25)
for n in tests:
    result = solution.isPowerOfFour(n)
    expected = n in [1, 4, 16, 64, 256]
    status = "✓" if result == expected else "✗"
    print(f"{n}\t{result}\t{expected}\t{status}")

print("\n Binary Check Examples:")
for n in [16, 8, 4]:
    bin_n = bin(n)[2:].zfill(8)
    power2 = (n & (n-1)) == 0
    even_pos = (n & 0xAAAAAAAA) == 0
    print(f"{n:4} = {bin_n} | power2:{power2} | even:{even_pos}")