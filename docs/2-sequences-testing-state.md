---
title: Reading 2
nav_order: 5
layout: default
---
# Reading 2: Sequences, Testing, and Program State

In this reading, you will learn about two new types: lists and ranges. We call these types *sequences* because they represent a collection of data arranged in a specific order. Sequences are particularly useful for another core feature of Python, called *loops*. Loops allow you to repeat blocks of code based on various conditions, and can be very useful in writing more complex functions and programs.

You will also learn about unit testing, which can help you check that your code is working as expected. Well-written unit tests can also be beneficial before you write code, helping you to clarify your thoughts and expectations for the way that your code should behave in specific cases.

Finally, you will learn about how to keep track of *program state*, which is essentially a snapshot of a program's behavior and data at a particular point in time. You will see how keeping track of program state can be helpful in debugging and fixing code that is not behaving as expected.

## Lists

A *list* represents a sequence of items, that is, some number of items arranged in a specific order. You can define a list with square brackets (`[]`) and items separated by commas (`,`):

```python
pi_digits = [3, 1, 4, 1, 5, 9]
```

You can get the length of list with `len` just like you would with a string, so `len(pi_digits)` would be 6.

The items in a list do not all have to be of the same type:

```python
mixed_list = [42, True, "Hello", 3.14]
```

We generally discourage mixing types within a list because, as we see later in this chapter, it is fairly common in Python to do some operation with each item of a list, and reasoning about what operations you can do is far easier when all of the items in the list are of the same type. (Remember, an object's type determines what operations you can do with it.)

Similar to the empty string, there is an empty list, which is a list that contains nothing:

```python
empty_list = []
```

It is *somewhat* similar to the empty string - `len([])` is 0. But the empty list behaves differently with `in`, as you will see below.

### List Operators

As with many types, you can check equality between lists with `==`/`!=`:

```python
base_list = [1, 2, 3]
copy_list = [1, 2, 3]
not_copy_list = [3, 2, 1]

base_list == copy_list  # True
base_list != copy_list  # False
base_list != not_copy_list  # True
```

As with strings, you can concatenate and multiply lists:

```python
group_1 = ["Alice", "Bob"]
group_2 = ["Charlie", "David"]

group_1 + group_2  # ["Alice", "Bob", "Charlie", "David"]
group_1 * 2  # ["Alice", "Bob", "Alice", "Bob"]
```

You can also index and slice lists just like you would strings:

```python
pi_digits = [3, 1, 4, 1, 5, 9]

pi_digits[2]  # 4
pi_digits[:3]  # [3, 1, 4]
pi_digits[2:4]  # [4, 1]
pi_digits[::-1]  # [9, 5, 1, 4, 1, 3]
```

In contrast to strings, you can modify lists *in place*. This means that you can assign something to a specific element inside a list, like this:

```python
passengers = ["Alice", "Bob", "Charlie", "David"]

# This makes passengers ["Alice", "Bob", "Eleanor", "David"].
passengers[2] = "Eleanor"
```

You can use `in` or `not in` to check whether a **single element** is in a list:

```python
passengers = ["Alice", "Bob", "Charlie", "David"]

"Alice" in passengers  # True
"Billy" in passengers  # False
"Charlie" not in passengers  # False
```

This means that the empty list `[]` is not guaranteed to be in every list, unless it is literally an element in the list:

```python
contains_empty = [[], [1, 2, 3]]
the_numbers = [4, 8, 15, 16, 23, 42]

[] in contains_empty  # True
[] in the_numbers  # False
```

### List Functions

There are a number of built-in functions that work with lists. You have already seen one, `len`.

`sum` can be used to add together a list of numbers:

```python
ones = [1, 11, 111]

sum(ones)  # 123
```

As a short aside, note that `sum` does not work for lists of strings. For strings, you can do this:

```python
letters = ["ab", "cd", "ef"]

"".join(letters)  # "abcdef"
```

Whatever you put in the string is placed in between elements of the list, so for example, `" ".join(["Hello", "World!"])` would return `"Hello World!"`.

You can use `min` or `max` to get the minimum or maximum element of a list, respectively:

```python
pi_digits = [3, 1, 4, 1, 5, 9]

min(pi_digits)  # 1
max(pi_digits)  # 9
```

The `sorted` function returns a copy of a list in sorted order, from least to greatest:

```python
pi_digits = [3, 1, 4, 1, 5, 9]

sorted(pi_digits)  # [1, 1, 3, 4, 5, 9]
```

You can do this with lists of any type, as long as they can be compared with `<`, `>`, and `==`. It's important to note that this creates a sorted *copy* of the original list, so in the example above, `pi_digits` is still `[3, 1, 4, 1, 5, 9]` even after running `sorted`.

### List Methods

There are also special functions called *methods* that you can run on lists. We will cover more on methods later in this course, but for now, just remember that methods of the list class "belong" to a specific list and are thus called in a slightly different way from normal functions, as you will see below.

Lists have a method very similar to `sorted` called `sort`. You can call it like this:

```python
pi_digits = [3, 1, 4, 1, 5, 9]

pi_digits.sort()  # pi_digits is now [1, 1, 3, 4, 5, 9]
```

As you might guess from the above, you can call a list method by taking any list object `L` and calling the function `L.sort()`.

The `sort` method is different from `sorted` because it modifies the objects it "belongs" to in place. This means that `pi_digits.sort()` does not return a new copy of a list - in fact, it returns `None`. Instead, `pi_digits.sort()` actually changes `pi_digits` so that it becomes `[1, 1, 3, 4, 5, 9]`.

The `reverse` method reverses a list in place:

```python
pi_digits = [3, 1, 4, 1, 5, 9]

pi_digits.reverse()  # pi_digits is now [9, 5, 1, 4, 1, 3]
```

(There is also a `reversed` function, but we skip it because it doesn't return a list, but a slightly different type that we may see later in this course.)

The `count` method counts the number of times that an element occurs in the list:

```python
pi_digits.count(1)  # 2
pi_digits.count(8)  # 0
```

The `index` method returns the first index in a list whose element is equal to some value. For example:

```python
dob_digits = [0, 1, 0, 1, 1, 9, 4, 7]

dob_digits.index(1)  # 1
```

In this example, `dob_digits.index(1)` returns 1 because `dob_digits[1]` is 1, and this is the first point in the list where 1 occurs.

Perhaps the most commonly used list method is `append`, which adds a single element to the end of a list:

```python
pi_digits = [3, 1, 4, 1, 5, 9]

pi_digits.append(2)  # pi_digits is now [3, 1, 4, 1, 5, 9, 2]
```

Again, remember that this differs from `pi_digits + [2]` because it returns `None` and changes the value of `pi_digits` rather than returning an entirely new list.

The `list` class has more methods, but we will not cover them here. If you want to see a listing of these methods with a short description for each, you can look at the relevant section of the [official Python tutorial](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists). Note that this is purely optional.

## Ranges

Specifically ordered lists of integers, such as `[0, 1, 2, 3, 4]`, are sequences that are so common in Python that there is a special type designed to make these easy to create called *ranges*. You can define a range like by using two or three numbers very similarly to how you might slice a string:

```python
range(5)  # Essentially [0, 1, 2, 3, 4]
range(1, 6)  # Essentially [1, 2, 3, 4, 5]
range(1, 6, 2)  # Essentially [1, 3, 5]
range(5, 0, -1)  # Essentially [5, 4, 3, 2, 1]
```

In the comments above, we say that a range is *essentially* a list. Ranges can be easily made into a list using type conversion, so `list(range(5))` actually returns the list `[0, 1, 2, 3, 4]`. But ranges are *not* lists, and many of the operators that work on lists do not work on ranges.

Ranges are useful not only because they save you from having to type long lists (imagine having to manually write out the list equivalent of `range(10000)`), but also because ranges store their data in a way that is much more memory-efficient than lists. Thus if you need to use a list of integers that can be defined as a range, you are generally encouraged to do so.

## `for` Loops

*Loops* are a common feature of many widely-used programming languages. They are blocks of code that are written to repeat some number of times, or based on specific conditions. In Python, a `for` loop is a common type of loop that repeats a block of code once for each item in a sequence called an *iterable* (called this because you can iterate through its items). Among the types we have seen so far, strings, lists, and ranges are iterables.

Here is a simple `for` loop:

```python
for seconds_left in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
    print(seconds_left)
```

This prints the following:

```
10
9
8
7
6
5
4
3
2
1
```

In this `for` loop, the line `print(seconds_left)` is repeated ten times, with the value of `seconds_left` being set to successive items in the list each time through.

The name you use for the variable in a `for` loop (`seconds_left` in the example above) should not be used outside of the body of the loop (i.e., the code within the loop). You will not get an error if you do this, but you may get some unintuitive results.

Sometimes, you may simply want to repeat a block of code some number of times, without changing anything each time through the block. In this case, you should use `_` as the variable in the loop, like this:

```python
# Print "Hello!" three times, each on its own line.
for _ in range(3):
    print("Hello!")
```

(Notice here that using `range(3)` in the loop is essentially the same as if we had instead used the list `[0, 1, 2]`.)

In this case, each printing of `Hello!` does not rely on the integers in `range(3)` in any way. Using `_` as the variable name makes that clear, both to you and to anyone else reading your code, and is a good habit to develop.

Finally, if you are iterating through a list, you should not modify that list in place in the body of the loop, as it can lead to strange results. For example, if you have a loop that starts with `for point in entries:`, calling something like `entries.append(42)` in the loop body may result in an infinite loop, or may not loop through all of the appended entries. While in some cases you might find that writing a loop this way happens to behave the way you want it to, you should not count on this behavior, as it may change between different versions of Python.

## `while` Loops

Sometimes, you may not know in advance how many times you need to repeat a certain block of code, so a `for` loop will not work. Instead, you may find it helpful to repeat a block of code as long as some condition is met. For this, you can use a `while` loop, which repeats a block of code *while* some expression is set to `True`.

Here is an example function that uses a `while` loop:

```python
def greatest_common_divisor(a, b):
    """
    Find the greatest common divisor of two numbers.

    Given two positive integers, find and return the largest number that evenly
    divides both integers.

    Args:
        a: An integer that represents the larger of the two numbers.
        b: An integer that represents the smaller of the two numbers.

    Returns:
        An integer that represents that largest number that divides both a and b
        (i.e., that a and b are both integer multiples of).
    """
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
```

This function implements [Euclid's algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm), for finding the greatest common divisor of two numbers. In this function, the line `while b != 0:` indicates that the following three lines execute for as long as `b` is not equal to 0. Whether `b` is 0 or not is checked at the *end* of each time through the block - in other words, if `b` is set to 0 during an iteration through the block, the following line (`a = temp`) runs one more time before moving on.

A `while` loop can be helpful in this context because just from looking at two numbers `a` and `b`, it isn't necessarily clear how many times the lines in the `while` loop have to be repeated before `b` becomes 0.

Because a `while` loop runs while some condition is true, the expression that follows `while` should return a boolean (i.e., `True` or `False`).

When writing `while` loops, one point that is helpful to remember is that at least one variable used in the loop's condition should be updated in the body, or the loop may repeat forever. Going back to the above example, the loop is checking `b != 0`, so if `b` were not 0 at the start of the loop and never got updated in the loop body, the loop would run forever. (If this happens while you are running a program on the command line or in a Jupyter notebook cell, you can use Ctrl-C to terminate execution of the program.)

## `break` and `continue`

Sometimes, in `for` or `while` loops, it can be helpful to exit the loop early. For example, you may want to print the first punctuation mark in a string `sentence`. You could do this using a `for` loop and a `break` statement:

```python
from string import punctuation

for character in sentence:
    if character in punctuation:
        print(character)
        break
```

The `break` statement *immediately* exits the loop body, skipping the rest of the loop body as well as any remaining iterations. As this example shows, it is particularly useful if you want to run a block of code until you finish a `for` loop *or* satisfy some other condition. In this way, you can think of a `break` statement as allowing you to combine the features of a `for` and `while` loop.

Related to this is the `continue` statement, which skips the rest of the loop body but instead of exiting the loop entirely, continues onto the next iteration. So for example, if you wanted to print the characters of a string on separate lines, ignoring spaces, you could do the following:

```python
great_creature = "superb owl"

for character in great_creature:
    if character == " ":
        continue
    print(character)
```

This prints the following:

```
s
u
p
e
r
b
o
w
l
```

## Comprehensions

*Comprehensions* are not data structures of their own, but rather ways to concisely express sequences (and a few other similar types that we will see later).

As an example, suppose you wanted to make a list of the squares of the numbers 0 through 99. You could do this with what you have seen so far in these readings:

```python
squares = []

for i in range(100):
    squares.append(i ** 2)
```

However, with a comprehension, you can do this with one line:

```python
squares = [i ** 2 for i in range(100)]
```

As this example shows, a comprehension allows you to define a list using something like a `for` loop. Notice that the order is somewhat inverted from a usual `for` loop, since you place the expression for the values in the loop `i ** 2` at the beginning of the comprehension.

You can further enhance comprehensions by adding `if` statements to the end of the statement. For example, suppose you have a list of words called `words` (because we are in a creative mood) and you want to get only the words that are less than 8 letters long. You could express this list as a comprehension as follows:

```python
short_words = [word for word in words if len(word) < 8]
```

Comprehensions can be quite powerful, but it is also important to be careful when using them. They can make your code difficult for others to read and understand, so we recommend only using them for fairly simple conditions, like what you see above.

For example, suppose you had a list of numbers called `numbers` (truly the most original name for such a list) and wanted to get only three-digit numbers whose ones digit was a prime number. You could do this:

```python
[number for number in numbers if number >= 100 and number < 1000
                                 and number % 10 in [2, 3, 5, 7]]
```

However, this is rather convoluted to read. It would be better to write this as a `for` loop, which is longer but easier to understand and less error-prone.

## A Type for Nothing

Sometimes, you may want to have a value that represents nothing at all, rather than a default value.

For example, suppose that you want to write code to find the maximum integer in a list `temperatures` without using the `max` function. You might write something like this:

```python
# NOTE: This code has a bug, so don't use it in your program.
current_max = 0

# After this loop, current_max will be equal to the max value in uranium_levels.
for reading in temperatures:
    if reading > current_max:
        current_max = reading
```

However, if all of the values in `temperatures` are negative, then `current_max` will stay at 0 - a number that never appears in the list at all!

To avoid this situation, there is a special value called `None` that you can use to represent nothing. Instead of initially setting `current_max` to 0, you can set it to `None` and add a check to update `current_max` if it is `None`, using something like this:

```python
# NOTE: This code has a bug, so don't use it in your program.
current_max = None

# After this loop, current_max will be equal to the max value in uranium_levels.
for reading in temperatures:
    if current_max == None or reading > current_max:
        current_max = reading
```

So why does this code still have a bug? This is because the syntax for checking equality to `None` is slightly different - rather than using `==` or `!=`, you use `is` or `is not`:

```python
current_max = None

# After this loop, current_max will be equal to the max value in uranium_levels.
for reading in temperatures:
    if current_max is None or reading > current_max:
        current_max = reading
```

In summary, remember to use `None` when you need a value that stands for nothing (usually useful when you are looking at variables that could have any value of its type), and use `is` or `is not` to check equality with `None`.

## Unit Testing

In the [previous reading](https://softdes.olin.edu/docs/readings/1-python-basics/#basic-types-and-operators), we saw how docstrings can be used to describe what a function does, what inputs it takes, and what it returns. However, it is important to also make sure that the function actually does what your docstring says it does. Testing the behavior of code in a systematic way allows you to provide evidence to others, and to yourself, that your code works in the way that you think it does.

One way of doing this is to use *unit tests*, which are test programs designed to check that a small, specific piece of code (a "unit") behaves in a specific way. In this section, you will see a few techniques to how to think through unit tests, with some sample implementations. The sample code we use is written for use with the [Pytest](https://pytest.org) testing framework, which is a library for Python that allows you to write unit tests. The techniques we describe, however, can be applied in any mainstream testing framework.

### The Structure and Meaning of a Unit Test

In Pytest and many other frameworks, a unit test is simply a function that tests another function by calling it and checking that its behavior or output in response to a specific input is as expected. For example, if we wanted to test the `max` function for lists that we saw earlier in this reading, we could write a unit test function that calls `max([3, 1, 4, 1, 5, 9])` and checks that it returns 9.

In Pytest, we can write the unit test as the following function:

```python
def test_list_max():
    """
    Check that the maximum of a list of integers is as expected.
    """
    assert max([3, 1, 4, 1, 5, 9]) == 9
```

Unit test functions in Pytest must have a name that follows a specific format; names starting with `test_` are automatically interpreted as being unit test functions in Pytest.

You will also notice that we use a new keyword, `assert`. This can be used anywhere in Python code, but is usually used within unit tests. The `assert` keyword checks that what follows it evaluates to `True` and causes an error if it does not. The Pytest framework makes sure to handle this error so that your unit testing code does not crash if a function is not working properly.

This unit test function does not take any inputs or return anything. For now, if you write your own unit test functions, you should follow this format, though we will later see examples of unit test functions that do take input.

It is also worth noting what this unit test means. If a function fails a unit test, and the test has been written correctly, then you know with certainty that the function is behaving incorrectly.

However, if this unit test passes, it does *not* necessarily mean that `max` is implemented correctly for all cases - it does not even mean that `max` is implemented correctly for lists of integers. In fact, the only thing that you can conclude with absolute certainty from this unit test is that `max` works as intended specifically for the list `[3, 1, 4, 1, 5, 9]`. So why are unit tests useful if they only tell us that a function works for a specific individual case?

By using a diverse range of unit test cases, you can gain more confidence that the function works as intended in general. For example, you could test that `max` works for lists of all negative numbers, lists where all numbers are the same, an empty list, and many more. Coming up with these tests may even help you think through your expectation of what a function should do in a specific condition - for example, should `max([])` crash with an error, and if not, what should it return?

Unit testing is a valuable tool in any programmer's arsenal, but it also draws on a skillset that many software designers do not practice often enough. In fact, software companies often hire engineers specifically for software testing who are experts in finding ways that code can break. As you get more comfortable writing code and making mistakes in Python, you will gain some intuition for the errors that Python programmers make, and this will allow you to write unit tests that specifically check that these errors were not made. We hope that you get the chance to practice this craft in this course.

### Example: List Average

Here is a longer example that highlights some of the principle of unit testing in action.

Consider the function `average_value`, which takes a list of numbers `numbers` and returns its average (as a float). You could write it (incorrectly) like this:

```python
def average_value(numbers):
    """
    Return the average of a list of numbers.

    Args:
        numbers: A list of numbers (ints or floats):

    Returns:
        A float representing the average value of the numbers in the list.
    """
    return sum(numbers) / 3
```

This function incorrectly divides the total sum of the list numbers by 3 instead of by the length of `num_list`.

You could write the following tests to check that the function works correctly:

```python
def test_average_value_123():
    """
    Check that the average of the simple list [1, 2, 3] is 2.0.
    """
    assert average_value([1, 2, 3]) == 2.0


def test_average_value_triple_ones():
    """
    Check that the average of a list of three 1s is indeed 1.0.
    """
    assert average_value([1, 1, 1]) == 1.0
```

These unit tests will indicate that `average_value` runs correctly, but this is actually a fluke, given the incorrect implementation of `average_value`.

If you then add the following test, the current incorrect implementation of `average_value` will fail:

```python
def test_average_value_single_one():
    """
    Check that the average of a list of a single 1 is indeed 1.0.
    """
    assert average_value([1]) == 1.0
```

While looking at the implementation of `average_value` will probably give you the idea that the above test will cause the function to return an incorrect value, you can also write these tests without having written `average_value` at all. In fact, writing unit tests before the implementation is part of a software development methodology called *test-driven development*, and can be helpful in helping you to clarify your expectations of a function's behavior before you get into the weeds with implementation.

### Running Unit Tests

Typically, the way to run unit tests is to create a separate testing file. This helps you keep your code and tests separate, which makes your files more readable. Similarly to functions, your unit test files in Pytest should have names that start with `test_`. For example, if the `average_value` function above were in a file called `average.py`, the unit tests should be in a file called `test_average.py`.

In your unit test file, you need to be able to access the functions that you defined. You can do this by *importing* the function into your file. Importing is a concept that we will see in more detail later, but in the example above, you could write the following line at the top of `test_average.py` (assuming that `average.py` and `test_average.py` are in the same directory):

```python
from average import average_value
```

The `from average` indicates that you are accessing variables in `average.py`, and `import average_value` indicates that you are specifically accessing `average_value`. In the rest of this file, you can use `average_value` as defined in `average.py`.

To run unit tests in Pytest, you can run the command `pytest` from within this directory - Pytest automatically detects and runs all relevant tests for you. With the example function and three tests above, you would get output that looked something like this:

```
============================= test session starts ==============================
platform linux -- Python 3.9.1, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /home/softdes/pytest-example
plugins: timeout-1.4.2, anyio-2.0.2
collected 3 items

test_average.py ..F                                                      [100%]

=================================== FAILURES ===================================
________________________ test_average_value_single_one _________________________

    def test_average_value_single_one():
>       assert average_value([1]) == 1.0
E       assert 0.3333333333333333 == 1.0
E        +  where 0.3333333333333333 = average_value([1])

test_average.py:13: AssertionError
=========================== short test summary info ============================
FAILED test_average.py::test_average_value_single_one - assert 0.333333333333...
========================= 1 failed, 2 passed in 0.02s ==========================
```

Reading this output, we can see that two tests passed - the ones that use a test list of exactly three elements. The one test that failed shows what `average_value([1])` returned, as well as what the expected output was. The test output also includes some helpful information including how long it took to run the tests, what version of Python and Pytest you are running, what folder you are running the tests from, etc.

### Unit Testing Tips

As we mentioned previously, the process of designing unit tests might feel unintuitive at first. As you write more programs and tests, you will develop a sense of what to test for, but below, we list a few tips for thinking about unit tests.

First, try to think of basic or trivial cases that produce clear expected behavior from a function. For example, if your function takes a string as input, you may want to think about what its behavior should be if you give it an empty string. It's okay if your function doesn't work in a case like this, but if so, you should make that expectation clear in your docstring by saying something like "takes a nonempty string" or "results in an error if given an empty string".

Second, if your function has conditionals (`if`/`elif`/`else`), you should try to run tests so that every "path" through these conditionals is executed. In other words, write at least one test that causes the function to go through each of the `if`, `elif`, and `else` blocks. This helps you to check that there are likely no glaring errors in any of those blocks that would cause your function to only fail for some inputs.

Finally, if your function has a `for` or `while` loop, write tests that go through the loop as well as tests that do not, if possible. For example, if a `while` loop begins with `while x > 10:` and `x` is less than or equal to 10 when the program reaches the loop, the body of the loop will not execute at all. It is good practice to ensure that the function still works in this case.

No matter how long you have been writing code, you will always write buggy code at least occasionally. But bugs in your code can be beneficial to your development as a software designer - as you encounter more bugs, you will develop a better and better intuition for the types of mistakes that result in bugs, how to test for them, and eventually, how to avoid them in the first place.

## Testing and Bias

Testing in the software industry has a history of excluding minority voices, creating problems for both developers and users in the long run. For example, using the image of Lenna Forsen, a playboy model from the 1970s, has been a standard practice in testing computer vision models for many years, since it was first used in jpeg testing. Forsen's cropped photo, which was originally a nude taken from the playboy magazine, has appeared in thousands of educational resources and books, and [remains one of the most used test images in the world](https://themanitoban.com/2020/01/the-devastating-consequences-of-tech-bro-culture/38819/). This practice can make software development feel more hostile towards women who are trying to enter the field.

On the user-end, excluding minority voices from testing can result in an unintentionally offensive product. For example, in 2015, [Google Photos mislabelled black individuals as gorillas in photos](https://www.sfgate.com/business/article/How-tech-s-lack-of-diversity-leads-to-racist-6398224.php). This was due to a lack of diversity in training data, something that might have been caught if there were more diverse voices on the team.

When testing, it is important to be mindful of who will be working on your software and who is using your software. Limit bias and use practices that will make your work accessible to both these groups, and any other groups that might use the software in the future.

## Program State

Sometimes your code does not behave as expected. This may be due to a bug in your code, or it may be due to a quirk of how Python behaves.

In this situation, it can be helpful to keep track of *program state*, which essentially tells you what a program is doing at a specific point in time. In particular, a program's state includes information such as which functions are executing, what variables are defined, what the values of those variables are, and what line of code the program will execute next.

In this section, we will provide a few tools and techniques you can use to see part of all of the program state. Specifically, we will describe print-based debugging, which allows you to get part of the program state at predetermined points in the code. We will also describe state and stack diagrams, which provide a more complete picture of what a function or program is doing.

### Print-Based Debugging

Suppose that you are trying to count the number of times that a digit (i.e., `0` through `9`) appears in a sentence. To do this, you write the following function:

```python
# NOTE: This code has a bug, so don't use it in your program.
from string import digits

def count_digits(sentence):
    """
    Count the number of digits that occur in a sentence.

    Args:
        sentence: A string representing the sentence to search in.

    Returns:
        An int representing the number of digits in the sentence.
    """
    current_digits = 0
    for character in sentence:
        if character in digits:
            current_digits += current_digits + 1
    return current_digits
```

You then run the following code to try the function out:

```python
sentence = "1, 2, 3, 4"
count_digits(sentence)  # This returns 15
```

Something is clearly wrong here, as there are only 4 digits in the sentence.

To find out what is wrong, we can start by seeing what the value of `current_digits` is in the loop. To do this, we can add a `print` statement as follows (the rest of the function is omitted here):

```python
for character in sentence:
    if character in digits:
        current_digits += current_digits + 1
    print(f"Digits counted so far: {current_digits}")
```

Running `count_digits(sentence)` still returns 15, but now it also prints the following:

```
Digits counted so far: 1
Digits counted so far: 1
Digits counted so far: 1
Digits counted so far: 3
Digits counted so far: 3
Digits counted so far: 3
Digits counted so far: 7
Digits counted so far: 7
Digits counted so far: 7
Digits counted so far: 15
```

It is clear that the count is being incremented incorrectly, but it may still be difficult to tell why. One reason for this difficulty is that we do not have quite enough information here: we lack a bit of context as to when the number of digits increases.

We can thus add this context by adding another print statement (again omitting the rest of the function):

```python
for character in sentence:
    print(f"Current character: {character}")
    if character in digits:
        current_digits += current_digits + 1
    print(f"Digits counted so far: {current_digits}")
```

This prints the following:

```
Current character: 1
Digits counted so far: 1
Current character: ,
Digits counted so far: 1
Current character:
Digits counted so far: 1
Current character: 2
Digits counted so far: 3
Current character: ,
Digits counted so far: 3
Current character:
Digits counted so far: 3
Current character: 3
Digits counted so far: 7
Current character: ,
Digits counted so far: 7
Current character:
Digits counted so far: 7
Current character: 4
Digits counted so far: 15
```

So now we can see that the count increases each time a digit is provided. But it increases by the wrong amount, so the problem is likely in the line `current_digits += current_digits + 1`.

Looking at this line more closely, we see that this line should be `current_digits = current_digits + 1`. The problem is that the line has `+=` instead of `=` - this is an [arithmetic assignment operator](https://softdes.olin.edu/docs/readings/arithmetic-assignment/) which causes the number of digits counted so far to more than double each time it sees a new digit.

Print-based debugging can be useful for finding bugs, particularly if you are relatively certain of what variable(s) might be responsible for a bug. It is a common way to get a view of program state among software designers, but it also has some drawbacks. The process of print-based debugging can take quite a long time and several iterations to get right, and it is easy to accidentally leave these debugging messages in code after the bug has been fixed.

### State Diagrams

A more powerful tool used to track program state is the *state diagram*. This keeps track of the values of each variable at a particular point in the program's execution. The collection of each variable's value, along with the next line of code to execute, is called the program's *state*.

As an example, consider our example from earlier in this reading, in which we want to find the maximum temperature reading from a list of recorded temperatures. We could write that code as a function, like this:

```python
# NOTE: This code has a bug, so don't use it in your program.
def max_temperature(temperatures):
    """
    Find the maximum temperature in a list of recorded temperatures.

    Args:
        temperatures: A list of ints representing recorded temperature values
            over time.

    Returns:
        An integer representing the maximum temperature of the list.
    """
    current_max = 0
    for reading in temperatures:
        if reading > current_max:
            current_max = reading
    return current_max
```

If we call `max_temperature([1, 3, 2])` and track the values of all the variables it uses over time (either by hand or through an automated tool like what we describe below), then we get the following:

| Line | `temperatures` | `current_max` | `reading` |
|------|----------------|---------------|-----------|
| `current_max = 0` | `[1, 3, 2]` | `0` | (not defined) |
| `for reading in temperatures:` | `[1, 3, 2]` | `0` | `1` |
| `if reading > current_max:` | `[1, 3, 2]` | `0` | `1` |
| `current_max = reading` | `[1, 3, 2]` | `1` | `1` |
| `if reading > current_max:` | `[1, 3, 2]` | `1` | `3` |
| `current_max = reading` | `[1, 3, 2]` | `3` | `3` |
| `if reading > current_max:` | `[1, 3, 2]` | `3` | `2` |
| `return current_max` | `[1, 3, 2]` | `3` | (not defined) |

(The value of each variable above is after the line shown has executed.)

Each line of this is a state diagram of the function's execution at a particular point in time. Here, you can see a nicer visualization (using [Python Tutor](http://www.pythontutor.com/visualize.html)) of the state diagram at the fifth line of the table above.

State diagrams are useful for tracking the values of variables as a program executes. While during debugging, state diagrams often provide a great deal of extraneous information and are more work to track than may be worth it, we highly recommend you to practice creating state diagrams of small functions as you write and run them. This skill can come in handy, especially as you dip your toes into more complex Python code.

### Stack Diagrams

A *stack diagram* is essentially a more complicated cousin of the state diagram. Sometimes, your code may have functions that themselves call other functions, and each of these functions keep their own set of variables. Here is an example:

```python
def count_vowels(word):
    """
    Count the number of vowels in a word.

    Args:
        word: A string representing a single word in lowercase to count vowels
            in.

    Returns:
        An integer representing the number of vowels in the word.
    """
    vowels = 0
    for letter in word:
        if letter in "aeiou":
            vowels += 1
    return vowels


def count_all_vowels(words):
    """
    Count all vowels that occur in a list of words.

    Args:
        words: A list of strings that represent the words in lowercase to count
            vowels in.

    Returns:
        An integer representing the number of vowels in all words.
    """
    vowels = 0
    for word in words:
        vowels += count_vowels(word)
    return vowels
```

If we called `count_all_vowels(["four", "score", "and", "seven", "years", "ago"])`, we would see that there are two functions, `count_all_vowels` and `count_vowels`, each of which maintains its own state with regards to variables and their values. The functions can use the same names for their variables, but the values are set independently.

Stack diagrams are useful if you need to trace through multiple functions at once. Like state diagrams, stack diagrams may require quite a bit of mental effort to create due to the number of variables that need to be tracked, but they can be particularly helpful in debugging more complex code.