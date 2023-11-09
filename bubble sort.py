# bubble sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swapped = True
       
    
        if not swapped:
            break
            
arr = [1,1,0,0,2,2,0,0,1,0,2,0,1]
bubble_sort(arr)
print("Sorted array is:", arr)