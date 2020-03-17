I have been skimming through Python Unit Test Automation: Practical Techniques for python developers by Ashwin Pajankar. This repo contains the code for hands on and briefing or lets say summary of each chapters. It's for my personal reference. If someone finds it useful that's plus point.


## Chapter 2

Chapter 2 explores about doc string and doc test. Doc string tends to be more powerful than I thought.

**PART I**

file: test_module01 has a class(a module inside class) and a separate module outside the class.

Each module and class have there doc string. These doc string attatched to module or class or file is a __doc__ attribute. If you run a bash python and import the file test_module01. Then by invoking the __doc__ attribute of file you can fetch doc string.

>>> python3
>>> import test_module01
>>> test_module01.__doc__

Result: 
"""
    This is test_module01.
    This is example of multiline docstring
"""

Similarly for classes and module you can do the same. 

**PART II**

DOC TEST

You can test functionality or breach in your module through doc test as well. Doc string parses the python interactive prompy and takes the output as the expected output, run the module and test if expected output is met. 

Example:

def add(a,b):
    """

    >>> add(3,4)
        7
    """ 
    return a+b

The following function is inside file **test_module02**. To run doc test , you dont need any explicit package or code. Just run the python file with "-m doctest" with -vv, which is verbose.

You can make the test fail by changing a+b to *(multiply) operator. Hence, it is fault in code. Also, you can send wrong input like add([{a,b},{t,y}). Similarly, if the expected output is wrong, test will fail. Hence, three ways test might fail.
