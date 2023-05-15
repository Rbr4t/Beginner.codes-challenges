function binary_search(arr, target, start, end) {
    if(end>=start){
        const pivot = Math.floor((start+end)/2);
        if(arr[pivot]===target) {
            return pivot
        } else if(arr[pivot] > target) {
            return binary_search(arr, target, start, pivot)
        } else {
            return binary_search(arr, target, pivot+1, end)
        }
    } else {
        return "target not found"
    }
}

const l = [1, 2, 3, 4, 5, 6, 7, 8]
console.log(binary_search(l, 3, 0, 7))