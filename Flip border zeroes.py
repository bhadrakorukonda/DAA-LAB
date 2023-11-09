def flip_border_zeros(matrix):
    if not matrix:
        return [], 0

    rows, cols = len(matrix), len(matrix[0])
    flips = 0

    # Helper function to flip 0 to 1 in the border
    def flip(x, y):
        nonlocal flips
        if matrix[x][y] == 0:
            matrix[x][y] = 1
            flips += 1

    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                flip(row, col)

    return matrix, flips

# Define the input matrix
input_matrix = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 1]
]

output_matrix, num_flips = flip_border_zeros(input_matrix)

# Print the output matrix and the number of flips
for row in output_matrix:
    print(row)

print("Number of flips:",num_flips)