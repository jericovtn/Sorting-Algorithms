# Name: Jerico James F. Viteño
# Assignment 2: Sorting Algorithms
# Insertion Sort
# January 27, 2023

def insertionSort(array):
    for i in range(1, len(array)):
        key = i
        while array[key - 1] > array[key] and key > 0:
            array[key - 1], array[key] = array[key], array[key - 1]
            key -= 1
        
        # print(array)

array = [40, 10, 55, 96, 16, 93, 56, 4, 98, 69]

insertionSort(array)
print(array)