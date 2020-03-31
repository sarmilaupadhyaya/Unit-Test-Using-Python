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
Fixures are used by test functions as an argument. Fixures are itself modules or functions.They act as initializer for test function. It is possible to re-use fixtures across function, class, module or whole test session scopes. 
In gist fixtures could be used to pass parameters or any environment before running a particular test.

Fixture functions are registered by marking them with @pytest.fixture.
Fixtures allow test functions to easily receive and work against specific pre-initialized application objects without having to care about import/setup/cleanup details.

Now if you want to use fixure for multiple tests in multiple files, you dont need to add them in each of the files. Instead you could add fixures in conftest.py file and access it without importing. It automatically gets discovered by pytest. The discovery of fixture functions starts at test classes, then test modules, then conftest.py files and finally builtin and third party plugins. Please run the test_fixures_example01.py and test_fixures_example02.py files :

```
python3 -m pytest

``` 

## SHARED DATA ##

If you want to use shared data from any file. Then, there are few packages you can use. One is pytest-datadir. Install it as:

```
pip install pytest-datadir
```
pytest-datadir will look up for a directory with the name of your module or the global 'data' folder.
You can access the contents of the files using injected variables datadir (for test_ folder) or shared_datadir (for data folder)

Example of usage is shown in the file test_module03.py.

## TEST FIXTURES SCOPE ##

You can define scope of a fixture defined in a file. It could be  function, class, module, package or session. If scope is "module", then the respective fixture is called for each module.

SImilarly, dynamic scope can also be created. You can write a function by passing the fixture_name, config parameter and setting condition and returning the required scope. THis function then would be passed to the "scope" parameter of pytest.fixture decorator.

This is snippet of code from documentation.

```

def determine_scope(fixture_name, config):
    if config.getoption("--keep-containers", None):
        return "session"
    return "function"


@pytest.fixture(scope=determine_scope)
def docker_container():
    yield spawn_container()


```

Another important attribute of fixture is *autouse* which enables fixures to be used automatically in all test module.

** ORDER OF FIXTURES **

run the snippet of code inside test_module04.py file and see the initialization of scope in a test function, I mean order of fixtures.

Within a function request for fixtures, those of higher-scopes (such as session) are instantiated before lower-scoped fixtures (such as function or class). The relative order of fixtures of same scope follows the declared order in the test function and honours dependencies between fixtures. Autouse fixtures will be instantiated before explicitly used fixtures.



Going through the documentation, I came across a feature of fixture where it is needed by single test multiple time. At that time, creating instance multiple time is not efficient. Hence, the fixture returns a generator function that gives data. I find it quite useful in my case. Here is the code from documentation:

```

@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")

```


** PARAMETERIZING FIXTURES **

This feature of fixtures, I am planning to use abundantly personally. Here we can parameterize i.e. Fixture functions can be parametrized in which case they will be called multiple times, each time executing the set of dependent tests.

See the code below:

```
@pytest.fixture(scope='module', params=[2,4,5])
def square(request):
    
    yield request.params ** 2


def test_area(square):

    assert (square * pi) > 0 
```

This code tests area for three radius. Not only int could be passed as params, but also, string bool or any data type inclusing functions too.
To see how function is passed as fixture parameter see the code in test_module05.py

The ids parameter in the fixture represents ids for each params, which will help us to locate test result for each params.

Most proficient use of this could be creating input and expected output needed for testing scenes.
