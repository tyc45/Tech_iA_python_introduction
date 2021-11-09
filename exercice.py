def my_sort(arr):

    # Checking for an empty list and if every elements of list are of the same type

    if not arr: return []
    type_check = type(arr[0])
    for elmt in arr:
        if type_check != type(elmt): return "On mélange pas!"

    # Sorting with an insertion sort algorithm

    for i in range(1, len(arr)):
 
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr