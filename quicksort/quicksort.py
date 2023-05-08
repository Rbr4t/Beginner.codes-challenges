

def partitionFunc(array, low, high):
    pivot = array[high]  # set the pivot
    index = low-1  # set the index variable
    for j in range(low, high):  # loop through the array
        if array[j] <= pivot:  # if the element is greater than pivot
            # swap the elements and increment left index
            index += 1
            save = array[j] 
            array[j] = array[index]
            array[index] = save
    # swap the pivot with index +1 value
    save = array[index+1]
    array[index+1] = array[high]
    array[high] = save
    return index+1


def quicksort(array, low, high):
    # sort recursively
    if high > low:
        pivot = partitionFunc(array, low, high)
        quicksort(array, low, pivot-1)
        quicksort(array, pivot+1, high)
    return array


print(quicksort(l, 0, len(l)-1))