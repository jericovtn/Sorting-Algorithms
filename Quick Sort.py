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


array = [40, 10, 55, 96, 16, 93, 56, 4, 98, 69]
