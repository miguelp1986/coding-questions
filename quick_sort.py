# Quick Sort
def quickSort(array):
    # Write your code here.
    if len(array) <= 1:
        return array

    low = 0 
    high = len(array) - 1

    quick_sort_helper(array, low, high)
    return array


def partition(array, low, high):
    pivot = array[low]
    i = low
    j = high

    while i < j: 
        while i < high and array[i] <= pivot:
            i += 1

        while j > low and array[j] >= pivot: 
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    array[low], array[j] = array[j], array[low]
    return j


def quick_sort_helper(array, low, high):
    if low < high:
        j = partition(array, low, high)
        quick_sort_helper(array, low, j)
        quick_sort_helper(array, j + 1, high)


if __name__ == "__main__":
    a = [10, 16, 8, 12, 15, 6, 3, 9, 5]
    # a = [2, 1]
    # a = [8, 5, 2, 9, 5, 6, 3]
    quickSort(a)
    print(a)
