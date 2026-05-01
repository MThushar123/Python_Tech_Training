def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    result = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    return result

def read_matrix():
    rows = int(input("Enter number of rows: "))
    matrix = []
    
    for i in range(rows):
        row_input = input(f"Enter row {i+1} (space-separated): ").strip().split()
        matrix.append([int(x) for x in row_input])
    
    return matrix

def print_matrix(matrix, label=""):
    print(f"\n{label}:")
    for row in matrix:
        print(row)

def main():
    print("Original Matrix:")
    original = read_matrix()
    print_matrix(original, "Original")
    
    transposed = transpose(original)
    print_matrix(transposed, "Transposed")

if __name__ == "__main__":
    main()