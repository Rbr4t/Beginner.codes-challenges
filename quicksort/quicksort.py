

def partitionFunc(array: list, low: int, high: int, asc=True) -> int:
    pivot = array[high]  # set the pivot
    index = low-1  # set the index variable
    if asc:
        for j in range(low, high):  # loop through the array
            if array[j] <= pivot:  # if the element is greater than pivot
                # swap the elements and increment left index
                index += 1
                save = array[j]
                array[j] = array[index]
                array[index] = save
    else:
        j = low
        while j <= high:
            if array[j] <= pivot:
                # swap the elements and increment left index
                save = array[j]
                array[j] = array[index]
                array[index] = save
                j += 1
    # swap the pivot with index +1 value
    save = array[index+1]
    array[index+1] = array[high]
    array[high] = save
    return index+1


def quicksort(array: list, low: int, high: int) -> list:
    global sorting
    # sort recursively
    if high > low:
        pivot = partitionFunc(array, low, high, sorting)
        quicksort(array, low, pivot-1)
        quicksort(array, pivot+1, high)
    return array


sorting = False  # set false if you want the final list in descending order
array = [2, 1, 3, 5, 9]
print(quicksort(array, 0, len(array)-1))
