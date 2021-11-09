def my_sort(arr):
    if not arr: return []
    type_check = type(arr[0])
    for elmt in arr:
        if type_check != type(elmt): return "On mélange pas!"
    
    result = arr
    for i in range(1, len(result)):
 
        key = result[i]

        j = i-1
        while j >= 0 and key < result[j] :
                result[j + 1] = result[j]
                j -= 1
        result[j + 1] = key
    return result