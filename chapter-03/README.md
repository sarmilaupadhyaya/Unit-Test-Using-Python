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

We will be moving towards multiple test case classes. How does a unittest module run test classes, in which order test cases classes are run. RUn the test_module04.py file and you can see that the test case classes are run according to alphabetical order.
