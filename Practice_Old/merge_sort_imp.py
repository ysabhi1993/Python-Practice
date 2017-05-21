def merge_sort(array):
    if len(array) == 1:
        return

    middleIndex = len(array)// 2
    
    left_half = array[:middleIndex]
    right_half = array[middleIndex:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = 0
    j = 0
    k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            array[k] = left_half[i]
            i += 1
        else:
            array[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        array[k] = left_half[i]
        k += 1
        i += 1

if __name__ == '__main__':
    array = [1,2,3,7,6,5]
    merge_sort(array)
    print(array)

    
        
