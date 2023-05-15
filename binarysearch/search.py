def binary_search(array: list, target: int | str, start: int, end: int) -> int:
    if end >= start:
        pivot = (start+end)//2
        if array[pivot] == target:
            return pivot
        elif array[pivot] < target:
            return binary_search(array, target, pivot+1, end)
        elif array[pivot] > target:
            return binary_search(array, target, start, pivot)
    else:
        return "target not found"
    
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(binary_search(l, 10, 0, len(l)-1))