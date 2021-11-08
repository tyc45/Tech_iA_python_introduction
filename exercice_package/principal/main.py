if __name__ == "__main__":

    import os
    import sys
    import inspect
    import math

    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)

    from parent_file import multiply
    from slevel import add
    from child_folder.child import divide

    print(round(divide(add(multiply(2,3),5),3),2))