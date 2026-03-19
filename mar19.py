def generate_pascal_triangle(num_rows):
    triangle = []
    
    for row in range(num_rows):
        current_row = [1]  

        for i in range(1, row):
            current_row.append(
                triangle[row-1][i-1] + triangle[row-1][i]
            )
        
        if row > 0:
            current_row.append(1) 
        
        triangle.append(current_row)
    
    return triangle

print(" Pascal's Triangle Generator")
print("How many rows?")
n = int(input().strip())

result = generate_pascal_triangle(n)

print("\n Pascal's Triangle:")
for i, row in enumerate(result):
    print(f"Row {i}: {row}")
