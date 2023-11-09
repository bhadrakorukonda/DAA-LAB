def print_max_number_of_1s(matrix):
  """Prints the maximum number of 1's in a 4 by 4 matrix.

  Args:
    matrix: A 4 by 4 matrix.
  """

  max_count = 0
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      count = 0
      while col < len(matrix[0]) and matrix[row][col] == 1:
        count += 1
        col += 1
      max_count = max(max_count, count)

  print("The maximum number of 1's in the matrix is:", max_count)
