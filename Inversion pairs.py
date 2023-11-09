a = [5, 4,16, 1]

def find_inversions(arr):
    inversions = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions.append((arr[i], arr[j]))
    return inversions

inversion_pairs = find_inversions(a)

if inversion_pairs:
    print("Inversion pairs:")
    for pair in inversion_pairs:
        print(pair)
else:
    print("No inversions found in the given array.")