# These here are a bunch of python exercises done in the context of my AI class
# The exercices collection can be found here: https://www.codewars.com/collections/python-walkthrough

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


def is_isogram(string):

    #https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

    string = string.lower()
    check = "".join(sorted(string))
    for char in check:
        if check.index(char) < len(check) - 1:
            if check[check.index(char) + 1] == char:
                return False
    return True


import math
def is_square(n):

    #https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

    if n < 0: return False
    return int(math.sqrt(n)) == math.sqrt(n)


def DNA_strand(dna):

    #https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

    result = ""
    for char in dna:
        if char == "C":
            result += "G"
        if char == "G":
            result += "C"
        if char == "A":
            result += "T"
        if char == "T":
            result += "A"
    return result

#cooler solution

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])


def solution(number):

    #https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

    if number < 0: return 0
    result = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0: 
            result += i
            
    return result


def find_it(seq):

    #https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

    for i in seq:
        if seq.count(i) % 2 == 1:
            return i



def rooting(n):
    
    '''https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
    This one reduces a number to its digital root
     '''

    result = 0
    for i in str(n):
        result += int(i)
    return result

def digital_root(n):
    result = n
    while len(str(result)) > 1:
        result = rooting(result)
    return result



def likes(names):

    #https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
    population = len(names)
    if not names: return 'no one likes this'
    if population == 1: return '{} likes this'.format(names[0])
    if population == 2: return '{} and {} like this'.format(names[0], names[1])
    if population == 3: return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    return '{}, {} and {} others like this'.format(names[0], names[1], str(population - 2))



def persist(n):

    #https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

    result = 1
    for i in str(n):
        result *= int(i)
    return result

def persistence(n):
    temp = n
    count = 0
    while len(str(temp)) > 1:
        temp = persist(temp)
        count += 1
    return count


def greet_developers(lst):

    #https://www.codewars.com/kata/58279e13c983ca4a2a00002a/train/python

    for pers in lst: 
        pers['greeting'] = 'Hi {name}, what do you like the most about {lang}?'.format(name = pers["firstName"], lang = pers["language"])
    return lst  

def is_ruby_coming(lst): 

    #https://www.codewars.com/kata/5827acd5f524dd029d0005a4/train/python

    return sum(pers['language'] == 'Ruby' for pers in lst) > 0


def valid_parentheses(string):

    #https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

    count_op = 0
    count_cl = 0
    
    for char in string:
        if char == '(': count_op += 1
        if char == ')': count_cl += 1
        if count_cl > count_op: return False
    if count_op != count_cl: return False
    return True


def elevator_distance(array):

    #https://www.codewars.com/kata/59f061773e532d0c87000d16/train/python

    result = 0
    for i in range(len(array) - 1):
        result += abs(array[i] - array[i+1])
    return result

def elevator_distance(array):

    #optimized solution

    return sum(abs(a - b) for a, b in zip(array, array[1:]))


def sc(s):

    #https://www.codewars.com/kata/5710a50d336aed828100055a/train/python

    count = 0
    for i in range(len(s)):
        count += 1
        if i < len(s) -1:
            count += 1
            if s[i] != s[i+1]:
                count += 5
    return count


def spin_words(sentence):

    #https://www.codewars.com/kata/5264d2b162488dc400000001/solutions/python

    lst = sentence.split()
    for i in range(len(lst)):
        temp = lst[i]
        if len(temp) > 4:
            lst[i] = temp[::-1]
    return ' '.join(lst)


def killer(suspect_info, dead):

    #https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d/train/python

    for key in suspect_info:
        if set(dead).issubset(suspect_info[key]):
         return key


def createDict(keys, values):

    #https://www.codewars.com/kata/5533c2a50c4fea6832000101/train/python

    newDict = {}
    limit = len(values) - 1
    for i in range(len(keys)):
        if i <= limit:
            newDict[keys[i]] = values[i]
        else:
            newDict[keys[i]] = None
    return newDict


from math import floor

def loose_change(cents):

    #https://www.codewars.com/kata/5571f712ddf00b54420000ee/train/python

    change_dict = {'Quarters': 0, 'Dimes': 0, 'Pennies': 0, 'Nickels': 0}
    cents = floor(cents)
    if cents <= 0: return change_dict
    while cents >= 25:
        cents -= 25
        change_dict['Quarters'] += 1
    while cents >= 10:
        cents -= 10
        change_dict['Dimes'] += 1
    while cents >= 5:
        cents -= 5
        change_dict['Nickels'] += 1
    while cents >= 1:
        cents -= 1
        change_dict['Pennies'] += 1
    return change_dict