# import pytest
# import os
# import sys
# import inspect

# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir) 

# from file_to_test import add, add_integer, divide

# # Il suffit de définir le test, puis écrire pytest dans le terminal suffit à le lancer
# def test_add():
#     assert add(3,4) == 7
#     assert add("a","b") == "ab"
#     #assert add(3.2,5.3) == 8.0

# def test_add_integer():
#     assert add_integer(3,4) == 7
#     assert add_integer("a","b") == None
#     assert add_integer(3.2,5.3) == None

# def test_divide():
#     assert divide(8,2) == 4
#     with pytest.raises(ZeroDivisionError):
#         divide(8,0)

# # on peut tester plusieurs paramètres d'un coup grâce à un décorateur.
# @pytest.mark.parametrize("numerator, numerator , result", [(2, 2, 4), ("a", "b", "ab"), (3.2, 5.3, 8.5)])
# def test_should_return_square(numerator, denominator, result):
#     assert add(numerator,numerator) == result