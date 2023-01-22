# Name: Jerico James F. Viteño
# Assignment 2: Sorting Algorithms
# Bubble Sort
# January 27, 2023

def bubbleSort(array):
    for i in range(len(array) -1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                temporary = array[j]
                array[j] = array[j + 1]
                array [j + 1] = temporary

        #print(array)

array = [40, 10, 55, 96, 16, 93, 56, 4, 98, 69]

bubbleSort(array)
print(array)