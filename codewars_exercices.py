def double_char(s):

    #Method doubling every single char in a string
    
    result = ""
    for char in s:
        result = result + char
        result = result + char
    return result

def get_count(sentence):

    #Method counting the number of vowels in a sentence

    count = 0
    for char in sentence:
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            count += 1
    return count

def accum(s):

    #https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/solutions/python

    result = ""
    count = 0
    for char in s:
        count += 1
        toAdd = char*count+"-"
        result += toAdd.capitalize()
    return result[:-1]


def square_digits(num):

    #https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

    result = ""
    for char in str(num):
        result += str(int(char)**2)
    return int(result)


def get_middle(s):

    #https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

    middle = len(s)//2
    if len(s) % 2 == 0:
        return s[middle - 1] + s[middle]
    else:
        return s[middle]