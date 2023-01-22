# Name: Jerico James F. Viteño
# Assignment 2: Sorting Algorithms
# Merge Sort
# January 27, 2023

def mergeSort(arr):
    if len(arr) > 1:
        leftArray = arr[:len(arr)//2]
        rightArray = arr[len(arr)//2:]

        # Recursion
        mergeSort(leftArray)
        mergeSort(rightArray)

        # Merge
        i = 0 # for left array index
        j = 0 # for right array indez
        k = 0 # for merge array index

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
                k += 1
            else:
                arr[k] = rightArray[j]
                j += 1
                k += 1

        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1

array = [40, 10, 55, 96, 16, 93, 56, 4, 98, 69]

mergeSort(array)
print(array)