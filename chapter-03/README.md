----PART 1-----

Xunit test framework is another approach that's collectively designed for various programming langauge. Xunit test framework style follows same architecture for various languages.. SOme components are :

1. Test case class: Base class which we will be inheriting from.
2. Test fixures: functions or methos that runs before and after test code is executed.
3. Assertions: Checks behaviour of element or component being tested.
4. Test Suite: Group of related test to be executed together.
5. Test result formatter: The test result is formatted into different output form like  HTML, XML.

Next is fundamental example of test which is inside test_modle01.py file.

In python unittest is the framework we need. So, install it at first.

Now, run the test inside test_module01.py file by running:

```
python3 test_module01.py -vv

```

In the file unittest.main() is the test runner.

On running the above code you can see the test passing. Now is the order of the test hapenning for each module or classes. 


---PART 2----

Next we have file test_module02.py that shows us the order. Run the file and you can see irrespective of the order of test module in the class, test ran alphabetically. testcase_01 ran at first then testcase_02 ran.

---PART 3---

Next, file test_module03.py , run it 

```
python3 test_module03.py

```
Then, you will see the verbosity inside file as parameter of unittest.main() gives detailed failed cases. testcase_03 and testcase_04 failed because of assertion error which you can see because of verbosity.
 Hence, here we used test runner on single test case class with 4 test modules where 2 test cases failed which gave us idea of test case failing.

---PART 4---

We will be moving towards multiple test case classes. How does a unittest module run multiple test classes, in which order test cases classes are run. Run test_module04.py file and you can see that the test case classes running according to alphabetical order.

---PART 5---
Next is Test Fixture. Test Fixture are set of steps run before and after the test. In unittest you will override methods of TestCase as per your purpose. Run the code in test_module05.py file and you can see:

setUpModule and tearDownModule are Module level of test fixture and they run once before any test case and after all test cases respectively. WHile, setUpClass and tearDownClass are class level of fixtures. They use @classmethod decorator which should have reference to class object as first parameter. And lastly, setUp and TearDown are executed before and after each test method i.e. everytime each method runs.


--PART 6--
Up until now we were adding if __name__ == ... , now we will be running without unittest.main(). To run test method inside testmodule_06.py, you need to run following code:

```
python3 -m unittest test_module06 
```

-m unittest option tries to find test modules , name starting with test_* and run them.

Add -v for verbose.

--PART 7--
Now, you can run control granularity of test. For example: you can run whole testmodule04.py using command:
```
python3 -m unittest -v test_module04
```
You can run a single class with command:

```
python3 -m unittest -v test_module04.TestClass04
```

Similarly, you can run single method with command:

```
python3 -m unittest -v test_module04.TestClass04.test_case01

```

--PART 8--

Some Important command lines for unittest.
you can list command lines using:

```
python3 -m unittest -h
```

SImilarly, you have already used -v option for verbose. We have an option of '-q' that stands for quiet and -f stands for failsafe mode that stops the testing after first testcase fails. IT could be combined with verbose as '-fv'

--PART 9--

Creating test case packages
We can create a package of chatper 3 and run as a single module. To do so create a __init__.py file and add all python files in the directory you are standing. 

add:
```
all = ["test_module01","test_module02","test_module03","test_module04","test_module05","test_module06", "test_module07"]

```

Now, if you want to add new tests for chapter 3, go to the chapter 3 folder and add the test module inside test folder, also add its name inside __init__ file as above. Then, in the parent directory run the test with command:

```
python3 -m unittest -v test.test_module04
```

Similarly, you can run test method as:

```
python3 -m unittest -v test.test_module04.TestClass04.test_case01

```

--PART 10--
Organizing the code

In real life scenarios, how would anyone maintain the test and development code.

Placing dev and test code in single directory.
Insode test directory you can see a python code named test_me.py. So, to test the functionality of this module , test_module08.py is created. You can go over the code. Now run the test_module08 :

```
python3 -m unittest -v test_module08

```

Inside test_module08 we directly imported the test_me module.

Secondly, dev and test code are placed in different directory.

inside chapter03 there is a new package named mypackage that contains a python file to b tested. Now these modules are added to the __init__.py insode my_package folder. These packages are tested using test_module09.py which is inside test folder. Go inside the test file and checkout the codes. To run the test:

```
python3 -m unittest -v test.test_module09

```


--PART 11--

Test Discovery is the process of discovering and executing all the tests in the project directory and all its subdirectories. This process is autoated in unittest and can be invoked using discover sub command.

```
python3 -m unittest discover

``` 

Now, run and see inside chapter 03 directory

** Coding Conventions for unittest **

In order to be compatible with test discovery, all test files must be either modules or packages importable from top-level directory of project.

Test discovery starts from current directory.

test discovery always serched for test*.py patterns in filenames.


**Assertion in unittest**

Few assertion methods

- assertEqual(a,b)
  a==b

- assertNotEqual(a,b)
  a != b

- assertTrue(x)
  bool(x) is True

- assertFalse(x)
  bool(x) is False

- assertIs(a,b)
  a is b

- assertIsNot(a,b)
  a is not b

- assertIsNone(x)
  x is None

- assertIsNotNone(x)
  x is not None

- assertIn(a,b)
  a in b

- assertNotIn(a,b)
  a not in b

- assertIsInstance(a,b)
  isinstance(a,b)

- assertNotIsInstance(a,b)
  not isinstance(a,b)

- assertAlmostEqual(a,b)
  round(a-b,7)==0

- assertNotAlmostEqual(a,b)
  round(a-b, 7) != 0

- assertGreater(a,b)
  a>b

- assertGreaterEqual(a,b)
  a>=b

- assertLess(a,b)
  a< b

- assertLessEqual(a,b)
  a<=b

- assertRegexMatches(s,r)
  r.search(s)

- assertNotRegexMatches(s,r)
  not r.search(s)

- assertItemsEqual(a,b)
  sorted(a) == sorted(b)

- assertDictContainsSubset(a,b)
  all the key/value pair in a exist in b

- assertMultiLineEqual(a,b)
  strings

- assertSequenceEqual(a,b)
  sequences

- assertListEqual(a,b)
  lists

- assertSetEqual(a,b)
  sets or frozensets

- assertTupleEqual(a,b)
  tuples

- assertDictEqual(a,b)
  dicts


--PART 12--
id() and shortDescription() attributes for a mehod is useful during debugging. Run the test_module10.py file and observe.


-- PART 13--
Failing a Test

Sometimes you need to fail a test deliberatly. In unittest, fail() method is used for that purpose. 
check the test_module11.py


Skipping tests

There are various decorators for skipping tests mechanism.
Few are:

- unittest.skip(reason)
  Skips tests and print out the reason.

- unittest.skipif(condition, reason)
  Skips the test if condition is true.

- unittest.skipUnless(condition,reason)
   Skips tests unless condition is true

- unittest.expectedFailure()
  Marks the test as expected failure. when test fails, it is not counted as failure.

In test_module12.py, test skipping is demonstrated.


-- PART 14--

Exceptions in the test case

When exception is raised in a testcase, the test case fails. If you run test_module13.py file, you can see the exception raised.


asser raises function is used to check the test condition. It is used to check if the code block raises the exception mentioned inside the asserRaises().
