# Name: Jerico James F. Viteño
# Assignment 2: Sorting Algorithms
# Quick Sort
# January 27, 2023

def quickSort(array, left, right):
    if left < right:
        partitionPosition = partition(array, left, right)
        quickSort(array, left, partitionPosition -1)
        quickSort(array, partitionPosition + 1, right)

def partition(array, left, right):
    # Indexes
    i = left # defines the left point to area to sort
    j = right - 1 # defines the right point of the pivot
    pivot = array[right] # array at the index right

    while i < j:

        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
            array[i], array[right] = array[right], array[i]
        
    return i


array = [40, 10, 55, 96, 16, 93, 56, 4, 98, 69]

quickSort(array)
print(array)