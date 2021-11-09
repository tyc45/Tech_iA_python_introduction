# import pytest
# import os
# import sys
# import inspect

# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir) 

<<<<<<< HEAD
# from file_to_test import add, add_integer, divide

# # Il suffit de définir le test, puis écrire pytest dans le terminal suffit à le lancer
# def test_add():
#     assert add(3,4) == 7
#     assert add("a","b") == "ab"
#     #assert add(3.2,5.3) == 8.0
=======
from file_to_test import add, add_integer, divide, alea_uniform

# Il suffit de définir le test, puis écrire pytest dans le terminal suffit à le lancer
def test_add():
    assert add(3,4) == 7
    assert add("a","b") == "ab"
    assert add(3.2,5.3) == 8.5
>>>>>>> b744fe7a10807a76a9688c69613fb6ae1a30df75

# def test_add_integer():
#     assert add_integer(3,4) == 7
#     assert add_integer("a","b") == None
#     assert add_integer(3.2,5.3) == None

# def test_divide():
#     assert divide(8,2) == 4
#     with pytest.raises(ZeroDivisionError):
#         divide(8,0)

<<<<<<< HEAD
# # on peut tester plusieurs paramètres d'un coup grâce à un décorateur.
# @pytest.mark.parametrize("numerator, numerator , result", [(2, 2, 4), ("a", "b", "ab"), (3.2, 5.3, 8.5)])
# def test_should_return_square(numerator, denominator, result):
#     assert add(numerator,numerator) == result
=======
def test_alea_uniform():
    assert  0 < alea_uniform(0,1) < 1
    assert type(alea_uniform(0,1)) == float
    with pytest.raises(TypeError):
        alea_uniform("a",0)
    

# on peut tester plusieurs paramètres d'un coup grâce à un décorateur.
@pytest.mark.parametrize("numerator, denominator , result", [(2, 2, 4), ("a", "b", "ab"), (3.2, 5.3, 8.5)])
def test_should_return_square(numerator, denominator, result):
    assert add(numerator,denominator) == result
>>>>>>> b744fe7a10807a76a9688c69613fb6ae1a30df75
