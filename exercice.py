def my_sort(lst):
    lst_type = type(lst[0])
    for elmt in lst:
        if type(elmt) != lst_type: return "On mélange pas!"
    sorted = []