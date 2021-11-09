def my_sort(arr):
    if not arr: return []
    type_check = type(arr[0])
    for elmt in arr:
        if type_check != type(elmt): return "On mélange pas!"

    for i in range(1, len(arr)):
 
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    return arr