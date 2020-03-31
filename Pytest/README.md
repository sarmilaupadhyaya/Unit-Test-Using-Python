** BAICS **

Since, we have already done group testing in unittest, we will directly ump towards advance example in pytest.

Before that:

Unlike unittest, pytest should be installed explicitly.

```
pip install -U pytest
```

pytest module when running in certain directory finds all the test files with test_*.py or *_test.py pattern. Functions writing in the form test_*. 

f you go to chapter-03/test directory inside Unittest and run pytest only, it will indeed find all the test cases but will throw path error. 

to solve this error, you can run pytest through python as a result the path of the directory will be added to sys.path.

```
python3 -m pytest

```


```
pytest -x           # stop after first failure
pytest --maxfail=2  # stop after two failures

```

** DEBUGGING **

So, I will directly move towards most useful tool I have been using for debudding. Its [PDB](https://docs.python.org/3/library/pdb.html) Debugging tool. It allows breakpoint in the code and debugging line by line. Follow the  link for detail.

You can add --pdb in pytest command which will trigger pdb after in failure. SImilarly, 

```
pytest -x --pdb   # drop to PDB on first failure, then end test session
pytest --pdb --maxfail=3  # drop to PDB for first three failures

```

You can access the information about failure in the command prompt. Following are the options:

sys.last_traceback
sys.last_value
sys.last_type.

Also, you can add code 

```
import pdb
pdb.set_trace()
```

in the certain lines inside your code where you want to debug. "n" is to execute next line in the prompt and "c" for executing whole script till next break point of available.


Next: builtin breakpoints

Python 3.7 introduces a builtin breakpoint() function. Pytest supports the use of breakpoint() with the following behaviours:

- When breakpoint() is called and PYTHONBREAKPOINT is set to the default value, pytest will use the custom internal PDB trace UI instead of the system default Pdb.
- When tests are complete, the system will default back to the system Pdb trace UI.
- With --pdb passed to pytest, the custom internal Pdb trace UI is used with both breakpoint() and failed tests/unhandled exceptions.
- --pdbcls can be used to specify a custom debugger class.


**TEST EXECUTION DURATION**

You can list slow test cases by specifying --duration=<n slowest test_case (int)>


Similarly, to throw timeout exception to the tests that takes longer time you can use:

```
 python3 -m pytest -o faulthandler_timeout=10

```

**CALLING FROM PYTHON FILE**

One can invoke pytest inside pythonfile using pytest.main()

alternative 
```
pytest.main(["-x", "mytestdir"])

```

** ASSERT STATEMENTS**

pytest supports python's assert statement.i One simple usage is to assert that your function returns the expected value.


Assertion about exceptions:
    Assertion of raised exceptions can be done by  pytest.raises.
Here is snippet of code I took from the documentation that illustrated the usecase.

```
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)
```

here the recursion hits the maximum depth and will raise the exception. The pytest.raises() scope throws the exception and its information is stores in object excinfo which has attributes like value,type and traceback.

Alternative 1:

```
pytest.raises(ExpectedException, func, *args, **kwargs)
```
Akternative 2:

```
@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()
```

@pytest.mark.xfail(raises=IndexError) rather than just raising exception , checks that the test is failing in a more specific way.

Hence, Using pytest.raises is ysed when you are testing exceptions your own code is deliberately raising, whereas using @pytest.mark.xfail with a check function is probably better for something like documenting unfixed bugs or  bugs in dependencies. 



Another cool feature is adding custom explanation of test fail cases. pytest_assertrepr_compare(config, op, left, right) function can take left and right object and compares and we can give our custom reason for the comparision to be zero. Oryou can return NOne for no custom explanation.


## FIXTURES ##
Fixures are 
