# Name: Jerico James F. Viteño
# Assignment 2: Sorting Algorithms
# Insertion Sort
# January 27, 2023

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while array[j - 1] > array[j] and j > 0:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        
array = [40, 10, 55, 96, 16, 93, 56, 4, 98, 69]

insertionSort(array)
print(array)