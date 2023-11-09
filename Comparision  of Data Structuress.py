def compare_data_structures(ds1, ds2):
  """Compares two data structures and returns True if they are equal, False otherwise."""
  # Check if the data structures have the same number of elements.
  if len(ds1) != len(ds2):
    return False
  # Check if the elements of the data structures are equal.
  for i in range(len(ds1)):
    if ds1[i] != ds2[i]:
      return False
  # If all of the above checks pass, then the data structures are equal.
  return True
