# Name: Jerico James F. Viteño
# Assignment 2: Sorting Algorithms
# Selection Sort
# January 27, 2023

def selectionSort(array):
    for i in range(9):
        minPosition = i
        for j in range(i, 10):
            if array[j] < array[minPosition]:
                minPosition = j

        temporary = array[i] 
        array[i] = array[minPosition]
        array[minPosition] = temporary

        #print(array)

array = [40, 10, 55, 96, 16, 93, 56, 4, 98, 69]

selectionSort(array)
print(array)