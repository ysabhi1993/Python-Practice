def quicksort(array, low, high):
    if low >= high:
        return

    pivot = partition(array, low, high)
    quicksort(array, low, pivot-1)
    quicksort(array, pivot+1, high)
     


def partition(array, low ,high):
    pivotIndex = int((low + high) / 2)
    swap(array, pivotIndex, high)

    i = low

    for j in range(low, high):
        if array[j] <= array[high]:
            swap(array, i, j)
            i += 1

    swap(array, i, high)

    return i

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


if __name__ == '__main__':
    a = [1,5,3,6,3,2,7,5,2,5,3]
    quicksort(a,0,len(a) - 1)
    print(a)


    
        
    
