import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from exercice import my_sort

def test_my_sort():
    assert my_sort([10,6,3,9]) == [3,6,9,10]
    assert my_sort(["ab","a","zfq","cgt","cdt"]) == ["a","ab","cdt","cgt","zfq"]
    assert my_sort([]) == []
    assert my_sort([True,False,True]) == [False,True,True]
    assert my_sort([5.6,7.3,0.1,0.2,10.6]) == [0.1,0.2,5.6,7.3,10.6]
    assert my_sort([10,6,"a"]) == "On mélange pas!"
    assert my_sort([1,1.2,3]) == "On mélange pas!"
    assert my_sort(["a","b",3]) == "On mélange pas!"