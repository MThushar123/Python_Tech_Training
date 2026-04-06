def matrix_reshape(mat, r, c):
    m, n = len(mat), len(mat[0])
    if m * n != r * c:
        return mat

    reshaped = [[0] * c for _ in range(r)]

    for i in range(m):
        for j in range(n):
            # Linear index
            idx = i * n + j    
            # New pos
            new_i = idx // c
            new_j = idx % c
            
            reshaped[new_i][new_j] = mat[i][j]
    
    return reshaped

print(" Matrix Reshape")
print("Enter rows m:")
m = int(input())
print("Enter cols n:")
n = int(input())

mat = []
print("Enter matrix row by row:")
for _ in range(m):
    row = list(map(int, input().split()))
    mat.append(row)

print("\nEnter new rows r:")
r = int(input())
print("Enter new cols c:")
c = int(input())

result = matrix_reshape(mat, r, c)

print("\n Original:")
for row in mat:
    print(row)

print("\n Reshaped:")
for row in result:
    print(row)