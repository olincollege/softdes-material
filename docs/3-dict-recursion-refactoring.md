---
title: Reading 3 - Dictionaries, Recursion, & Refactoring
nav_order: 6
layout: default
---

# Reading 3: Dictionaries, Recursion, and Refactoring
{: .no_toc }

- TOC
{:toc}

In this reading, you will learn about dictionaries, which allow you to associate pairs of data, as well as tuples, which are similar to lists but can be more useful in some aspects of working with dictionaries. Not only are dictionaries commonly used in Python programming, but they also form a core part of how Python works under the hood (though we won't cover the latter here).

You will also learn about recursion, a powerful problem-solving approach in computing that is rooted in mathematical principles. Recursion is an alternative to using loops that can make solving certain types of problems much simpler than if you had used loops.

Finally, you will learn about refactoring, which is the process of rewriting code to improve it in some way while keeping its external behavior unchanged. You will learn a few ways that you can refactor code, and how it might help improve code that you have already written.

## Dictionaries

In its most basic form, an English dictionary allows you to look for a specific word and find its definition. Similarly, a _dictionary_ in Python allows you to associate pairs of data. You can then "look up" one member of the pair to get the other member. As an example, here is a dictionary that maps integers to their English word:

```python
number_words = {"one": 1, "two": 2, "three": 3}
```

As you can see, you use curly braces (`{` and `}`) to surround the pairs and use the colon (`:`) to connect a pair of items (like the integer `1` and the string `"one"`).

We say that this dictionary _maps_ `"one"` to `1`. In this dictionary, `"one"`, `"two"`, and `"three"` are called _keys_, while `1`, `2`, and `3` are called _values_. Coming back to the English dictionary example, the keys are like the words, while the values are like the definitions of those words.

As with lists, you can mix and match types used for keys and values, but we again discourage this, as it can make it difficult to reason about the behavior of your dictionary in a program.

Like the empty string and empty list, there is also the empty dictionary which contains no key-value pairs:

```python
empty_dict = {}
```

### Dictionary Operators

You can compare whether two dictionaries are equal with `==` and `!=`, which checks that all key-value pairs of the two dictionaries are the same.

The most common thing you will do with a dictionary is to "look up" or find the value corresponding to a key. You can do that with syntax that is similar to getting an element in a list:

```python
# This returns 1
number_words["one"]
```

And like most English language dictionaries, the lookup only goes in one direction: you can't get `"one"` by running `number_words[1]`.

If you try to look up a key that is not in a dictionary, you will get an error (called `KeyError`):

```python
>>> number_words["zero"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'zero'
```

You can avoid this error by first checking if the key is mapped to a value using `in` (or `not in`), like this:

```python
"zero" in number_words  # This returns False
"one" in number_words  # This returns True
```

You can add entries to a dictionary by assigning a value to a specific lookup, like this:

```python
number_words["zero"] = 0
number_words  # This is now {"one": 1, "two": 2, "three": 3, "zero": 0}
```

A key can only have one value associated with it (unlike English dictionaries, where words can have multiple definitions). If you assign a value to a key already in a dictionary, you will overwrite its previous value:

```python
number_words["one"] = 42
number_words  # This is now {"one": 42, "two": 2, "three": 3, "zero": 0}
```

You can also delete keys out of a dictionaries using the keyword `del`:

```python
del number_words["two"]
number_words  # This is now {"one": 42, "three": 3, "zero": 0}
```

If you try to delete something not in the dictionary, like `del number_words["four"]`, you will get a `KeyError`.

### Dictionary Iteration

You can also use a dictionary in a `for` loop, which will loop through its keys:

```python
number_words = {"one": 1, "two": 2, "three": 3}

for word in number_words:
    print(f"The word {word} is the number {number_words[word]}")
```

This prints the following:

```
The word one is the number 1
The word two is the number 2
The word three is the number 3
```

The order in which we go through the keys is the order in which they were first added to the dictionary. So if we had instead defined `number_words` as `{"three": 3, "two": 2, "one": 1}`, we would see the above lines printed in reverse order.

It can sometimes be tedious to loop through a dictionary and have to look up each of its values. To make this process more convenient, you can use the dictionary method `items` like this:

```python
# This prints the same lines as above, but is a bit neater to write.
for word, number in number_words.items():
    print(f"The word {word} is the number {number}")
```

We haven't mentioned `for` loops that look like this before, but for now, it is enough to note that using this structure with `items` allows you to essentially loop through two things at the same time.

Like with lists, you can use a comprehension to create a dictionary, using a similar syntax with a `for` loop:

```python
# This sets squares to {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
squares = {i: i ** 2 for i in range(5)}
```

### Dictionary Functions

You can check how many key-value pairs are currently in a dictionary with `len`:

```python
next_int = {0: 1, 1: 2, 2: 3, 3: 4}
len(next_int)  # This returns 4
```

Normally, you iterate through dictionaries in the order in which the keys were added, but you can iterate through a dictionary in reverse order with `reversed`:

```python
number_words = {"one": 1, "two": 2, "three": 3}

# This prints the lines from "three" to "one"
for word in reversed(number_words):
    print(f"The word {word} is the number {number_words[word]}")
```

Or you can loop through in sorted order of keys with `sorted`:

```python
# This prints the lines for "one", then "three", then "two"
for word in sorted(number_words):
    print(f"The word {word} is the number {number_words[word]}")
```

For strings, sorted order is alphabetical, which explains the ordering in the comment above.

### Dictionary Methods

In addition to `items` mentioned above, dictionaries have a few other methods that can be helpful to know.

If you want to iterate just through the values of a dictionary, you could do this:

```python
# The _ shows that we are not using the key here.
for _, number in number_words.items():
    print(f"I like the number {number}")
```

However, a cleaner way to do this is through the `values` method:

```python
for number in number_words.values():
    print(f"I like the number {number}")
```

Sometimes, you want to look up a key that may or may not be in the dictionary, and return a default value if the key isn't in the dictionary. You can use the `get` method to do this:

```python
birthday = {"year": 1947, "month": 1, "day": 1}
birthday.get("year", 0)  # This returns 1947
birthday.get("hour", 0)  # This returns 0
```

This can be helpful when iterating through a dictionary with a `for` loop. There a few variations of `get` that return a default value, but do additional things like set the value of the missing key to the default value. For conciseness, we will not mention them here, but you can (completely optionally) take a look at list that includes them in the [Python official documentation](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict).

The `update` method can be used to "combine" dictionaries, pulling keys and values of another dictionary into the current one:

```python
timestamp = {"year": 2038, "month": 1, "day": 19, "hour": 1}
time = {"hour": 3, "minute": 14, "second": 7}

# After this, timestamp is {"year": 2038, "month": 1, "day": 19, "hour": 3,
#                           "minute": 14, "second": 7}.
timestamp.update(time)
```

Note that when you do this, keys in the "original" dictionary (`timestamp` in the above example) will be overwritten if they also exist in the "other" dictionary (`time` in the above example).

### Allowed Types in Dictionary Keys

Finally, note that there are some restrictions on what types you can use as keys in dictionaries. Of the types you have seen so far, lists and dictionaries are the only two types that you cannot use as dictionary keys:

```python
>>> {[1, 2]: "one, two"}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

That being said, there is an alternative if you want to use something like a list as a dictionary key, which we will describe next.

## Tuples

Tuples are essentially lists that you cannot change (i.e., you cannot assign to individual items or `append` to them). They are written slightly differently from lists, using parentheses (`()`) around comma-separated items:

```python
sample_tuple = (1, 2, 3, 4, 5)
```

Their behavior is nearly identical to that of lists - you can add tuples, multiply them by integers, loop through them, find their length, etc.

One hiccup with this syntax is that declaring a tuple with just one item in it requires a comma:

```python
>>> (1)  # This is an int
1
>>> (1,)  # This is a tuple
(1,)
```

A big advantage of tuples is that they can be used as dictionary keys:

```python
tuple_dict = {(1, 2): "one, two"}
tuple_dict[(1, 2)]  # This is "one, two"
```

If you know that you are dealing with a sequence of a specific size (for example, if you know that your data represents a pair of _x_ and _y_ coordinates), it may be advantageous to use a tuple. Doing so prevents you from accidentally appending something to the coordinates.

## Data Structure Selection

Some of the types that you have seen in this and previous chapters - strings, lists, dictionaries, and tuples - are sometimes referred to as _data structures_, because they are ways of storing and organizing data for different purposes. We have covered how to use these data structures, but so far, we have not talked much about when it might make sense to use each type in a program. In this section, we'll provide a few brief tips for thinking about how to select a useful data structure in a program.

### Structure

As the term "data structure" suggests, how your data can or must be structured will affect your choice of data structure.

In Python, a common aspect of your data to consider is whether or not it needs to be in a specific order. For example, if you are doing a survey about how people discover new music and need to store the survey responses in Python, then you probably do not need to store the responses in a list, as the order in which the responses arrived will likely not affect your conclusions. You could instead store this information as a [set](https://softdes.olin.edu/docs/readings/sets/) (fully optional reading), which stores a collection of items without any explicit order.

On the other hand, if in this survey you asked people to rank their top 5 favorite music artists, then each response to this question should be stored as a list (or a similar type), since the order of the artists represents that ranking.

This is not to say that you should _always_ store unordered data in a set rather than a list (though it is good to at least consider doing so). Read on to find out why.

### Operation

What operations you need to do with the data will also affect your choice of data structure. Whether you need to iterate through a collection of values, read, write or modify the data, or do things like sort the data, those needs will likely lead you to choose a type that has those operations built in as operators, functions, or methods.

As an example, think about storing data on students' names and their ID numbers. You could store this information as a dictionary:

```python
{"Ada": 18151210, "Barbara": 19391107, "Charlie": 19470101}
```

This would be useful if we wanted to look up a student's ID number from their name, but not ideal if we wanted to look up a student's name from their ID number.

We might always have both a student's name and ID number on hand at all times, and thus not care about lookups at all. We might be keeping this information as a roster of students in a particular course. In this case, we could store this information as a list of tuples:

```python
[("Ada", 18151210), ("Barbara", 19391107), ("Charlie", 19470101)]
```

This format (which contains the exact same data as in the dictionary) might be used if you had read these values out of a spreadsheet, for example. Storing this data in this way would be more useful if you wanted to be able to form groups of students (such as into project teams), since it would be easier to get individual pairs from the list and use lists to represent each group (no dictionary lookups required).

Finally, if you frequently need to get just the names of all students, or just their ID numbers, you could store this information as two separate lists:

```python
names = ["Ada", "Barbara", "Charlie"]
id_numbers = [18151210, 19391107, 19470101]
```

This lets you easily sort all of the names in some order, though it does require you to make sure that if you rearrange one list, you rearrange the other to keep the names and ID numbers matched.

It is important to note that in each of these cases, the data stored is exactly the same - the only change is in what operations you can easily do with the data. Moreover, you can usually do any operation with any of these formats. For example, if you wanted to look up Barbara's ID number in a list of tuples, you could do this:

```python
roster = [("Ada", 18151210), ("Barbara", 19391107), ("Charlie", 19470101)]
for pair in roster:
    if pair[0] == "Barbara":
        barbara_id = pair[1]
```

But this is more complicated than doing a dictionary lookup, like `id_numbers["Barbara"]`.

### Context

The last aspect we will mention that may affect your choice of data structure is the context of your data. This is essentially how other functions or programs might use the data you are storing. As a software designer, we encourage you to consider how your program's output might be most commonly used by other functions and programs, and to make it easier for those functions and programs.

For example, you might have a program that reads in a large amount of data from a text file, some of which is numerical. It might be fine to leave this numerical data as strings, particularly if your program needs to do some text processing with this data later. However, if you are not using this data as a string and it is likely that other functions or programs will need the data in numerical form, you should consider converting it to make this process easier. After all, if ten other functions need the data in numerical form, it is easier to convert it once in your function than to convert it from a string in each of the other functions.

If you're still not convinced that you should think about who will be using your data, consider this scenario:

![Every SoftDes grader's fear](images/3-dict-recursion-refactoring/docx.jpg)

## Recursion

_Recursion_ is a problem-solving approach and programming technique that has its roots in the mathematical foundations of computer science. Despite not being used that often in much of software development, recursion is a technique that many potential employers will expect you to have some familiarity with.

In the problem-solving context, recursion involves repeatedly breaking a problem or task down into smaller versions of itself until it can be easily solved, then using those smaller solutions to build up a solution to the original problem. In the programming context, this is implemented as a function that _calls itself_.

In this section, we will present recursion as both a way of solving problems and a way of writing functions. We will provide few worked-out examples to illustrate recursion. Since recursion is only a well-suited approach for certain types of problems, we will also describe the situations in which using recursion is likely to be helpful.

To explain how to approach a problem using recursion, we will use an example problem through the next few sections. The problem is to find the minimum value in a list of numbers. We have already seen this done using a `for` loop and the `min` function. Now we will take a look at how to solve this problem using recursion, which we hope will be a good comparison with the other approaches.

### The Base Case

The first step in using recursion is to find a set of cases where this problem can be solved more or less trivially. This is called the _base case_ in recursion, and will be used to build up a solution to the problem that can be used for all lists.

In our example problem, the trivial case is when our list has only one number in it. In this case, whatever that number is must be the minimum value by default. Usually, base cases for a problem tend to look something like this: an empty sequence or string, a sequence with only one item in it, an integer argument that is 0 or 1, etc. We would not use an empty list as the base case for this example problem, since taking the minimum of an empty list doesn't make much sense.

Problems can occasionally have multiple base cases. For example, if your function takes an integer `n`, it may have a base case that returns `True` when `n` is 1 and `False` when `n` is 0.

### The Recursive Case

Once you have identified the base case of a problem, you should think about how to break the problem down into smaller versions, called the _recursive cases_ or _recursive calls_. As you do this, you should keep two principles in mind:

1. You should break the problem into a small unit of work and a smaller version of the same problem.
2. Breaking down the problem repeatedly in this way should eventually get to the base case.

What constitutes a "small unit of work" is somewhat up to your discretion, but typically involves some post-processing of the results of the recursive calls. We will describe this work more in the next section.

In our example problem, we can consider smaller and smaller versions of the problem by splitting the list into its first item and the rest of the list. Here is a concrete example:

```python
[2, 0, 1, 3]  # The original list.
2, [0, 1, 3]  # Split the first item from the original list and consider the
              # list [0, 1, 3].
0, [1, 3]  # Repeat the process.
1, [3]  # Now we have a base case: [3].
```

We can see that the length of the list goes down by 1 in each step. Beause of this we know that we will eventually reach a list of length 1, which is a base case.

### Process the Answer of the Recursive Case

Once you hit a base case, you can solve the problem trivially. Now, you should determine how to do the "small unit of work" we mentioned earlier to build up larger solutions.

In our example, we hit a base case, which was to find the minimum of the list `[3]`. Clearly, the minimum of this list is 3. In the step before we reached this case, we split the list `[1, 3]` into the first item of the list (`1`) from the rest of the list. So what do we now do with `1`?

Because we are trying to find the overall minimum of the list, we should compare it to the solution we got for the minimum of `[3]` and reutrn whichever is smaller. In this case, we are comparing `1` and `3`, of which `1` is smaller. Thus, the minimum of the list `[1, 3]` is `1`.

If we repeat this process, we can build up the minimum of more and more of the original list until we have the full list. Thus in this case, the "small unit of work" is to compare the current "head" of the list (that was split off in this step) to the minimum of the rest of the list (that was just calculated) and return the smaller one. Here is a concrete example of this process:

```python
1, [3]  # 1 is smaller than 3, so the minimum of [1, 3] is 1.
0, [1, 3]  # 0 is smaller than 1, so the minimum of [0, 1, 3] is 0.
2, [0, 1, 3]  # 0 is smaller than 2, so the minimum of [2, 0, 1, 3] is 0.
# [2, 0, 1, 3] was the original list, so we are done and the minimum is 0.
```

### Implementation

Notice that the process we use in each step of the recursive approach is identical: split the head of the list from the rest, find the minimum of the rest, and take the smaller of the two. If the list only has one item in it, simply return that item.

Because the smaller versions of the problem have the same approach to solving them as the entire problem, we can use the same function code in each step. The way to do this in Python is to have a function _call itself_, like this:

```python
def list_min(numbers):
    # This is the base case. Simply return the number.
    if len(numbers) == 1:
        return numbers[0]
    else:
        # Split the head of the list.
        first = numbers[0]
        # Find the minimum of the rest of the list.
        min_rest = list_min(numbers[1:])  # list_min calls itself here.

        # Return the smaller of the two.
        if first < min_rest:
            return first
        else:
            return min_rest
```

It can be a bit difficult to fully understand this logic without seeing the function in action. We highly recommend you view a [step-by-step visualization of this function](http://www.pythontutor.com/visualize.html#code=def%20list_min%28numbers%29%3A%0A%20%20%20%20if%20len%28numbers%29%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20return%20numbers%5B0%5D%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20first%20%3D%20numbers%5B0%5D%0A%20%20%20%20%20%20%20%20min_rest%20%3D%20list_min%28numbers%5B1%3A%5D%29%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20Return%20the%20smaller%20of%20the%20two.%0A%20%20%20%20%20%20%20%20if%20first%20%3C%20min_rest%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20first%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20min_rest%0A%20%20%20%20%20%20%20%20%20%20%20%20%0Alist_min%28%5B2,%200,%201,%203%5D%29&cumulative=false&curInstr=1&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) to get a better sense of how this approach works in practice.

### Iteration or Recursion?

The function we used previously was used as an example to show the thought process behind recursion, but in practice the function is much better written with a `for` loop:

```python
def list_min(numbers):
    minimum = None
    for num in numbers:
        if minimum is None or num < minimum:
            minimum = num
    return num
```

(You could also just use the `min` function we introduced earlier, which would be an even better approach.)

While this problem was helpful in seeing the conceptual logic behind recursion, the actual code turned out to be a bit messy in practice. We chose this problem to illustrate that while recursion can be applied to many problems, it is not always an ideal way to approach problems.

As a problem-solving approach, recursion is usually compared against _iteration_ (which uses a `for` or `while` loop to solve a problem). Any problem that can be solved with recursion can also be solved with iteration, and vice versa. But you will often find that one approach is much more intuitive than the other.

So when is recursion a better approach than iteration? In practice, we've found two helpful signs that recursion may be a well-suited approach:

1. You don't know beforehand how many iterations or steps you have to go through. If you know how many steps you have to take, then you should just write a `for` loop, with something like `for thing in sequence:` or `for i in range(len(sequence)):`.
2. You need to keep track of or combine information from previous steps. If you don't know how many iterations you need to do but it is relatively easy to keep track of the previous steps, you may consider using a `while` loop instead.

To illustrate some cases in which recursion is better suited, we will present two problems - one from a more conceptual perspective with no real code, and one from a more programming-oriented perspective.

### Folder Hierarchy

Suppose you want to list all of the regular files that are within a folder or any of its subfolders. For example, consider the following directory structure:

```
deep-sea-divers
└── photic
    └── twilight
        └── bathyal
            ├── abyssal
            │   ├── detritus.txt
            │   └── treasure.zip
            ├── angler.sh
            ├── pollutant.zip
            ├── trash.txt
            └── wreckage.py
```

The goal is to list the six files you can see in this structure.

This problem is well-suited to a recursive solution for the following reasons:

1. It isn't obvious at the start of the problem how many iterations to make. You can see from this structure that there are files that are five folders deep, but if you didn't know what was in `deep-sea-divers` to begin with, the only way to find out would be to actually open all of the folders.
2. Some folders have a mix of subfolders and files, and some folders can have multiple subfolders. Taking an iterative approach would be difficult, since you would then need to keep track of where you are in the directory structure, as well as the files and subfolders at each level.

Conceptually, though, a recursive approach is rather straightforward:

1. Look in the current folder and list all of the regular files in it.
2. If there are any subfolders in the current folder, apply the same approach to each of those subfolders.

Eventually, you will reach a folder that has no subfolders, as you cannot have an infinite cascade of folders nested in each other. This is the base case, as you simply can list the files in this folder.

### The OFAC Problem

Consider a fictional club on campus: the Olin Fried Asparagus Club, or OFAC for short. This club sells packages of fried asparagus stalks in sets of 6, 10, or 15 stalks. If you want 12 stalks, you can buy two packages of 6, but this is not possible for every number: if you want 13 stalks, for example, there is no way to buy a combination of packages that gets you exactly 13 stalks. (You could buy a package of 15 and give two away, though.)

You want to determine for any number of asparagus stalks if it is possible to buy a combination of packages to equal exactly that number. This problem is well-suited to recursion, based on our two criteria above:

1. You don't know how many iterations you need to make, because it depends on what combinations of packages you buy. For example, if you want 30 stalks, you could buy five packages of 6, three packages of 10, or two packages of 15.
2. Keeping track of all of the possible package combinations is difficult. If for example, you want to buy 42 stalks, you can start by buying a package of 6, 10, or 15. Then, you have three sub-problems: trying to buy 36, 32, or 27 stalks (42 - 6, 10, or 15, respectively). For each of _those_, you would need to keep track of the possible combinations, and this would get rather tedious.

Fortunately, recursion again turns out to be a helpful approach.

There are a number of base cases to consider here:

- If you need to buy 0 stalks, then this is easily possible - just buy nothing.
- If you need to buy 5 or fewer stalks (but not 0), this is impossible - the minimum you can buy in a single package is 6.

Otherwise, you can subtract 6, 10, or 15 from the number you want to buy, and see if any of those combinations will work.

Following this approach, your code would look like this:

```python
def asparagus(n):
    if n == 0:
        return True
    # Note the case below also includes negative numbers, which can happen in
    # some recursive calls (such as if n is 7 and you subtract 10).
    elif n < 6:
        return False
    else:
        return asparagus(n - 6) or asparagus(n - 10) or asparagus(n - 15)
```

Because each recursive call subtracts some number from the originally desired number of stalks, you are guaranteed to eventually hit one of the base cases (either the desired number is 0 or otherwise less than 6).

## Refactoring

We will end this chapter by talking about _refactoring_, which is the process of rewriting code while keeping its external behavior the same. Since most of your programming so far has been focused on functions, our examples and explanations in this section will focus on refactoring at the function level.

When we say that a function's external behavior should stay the same, we mean that it should essentially be backwards-compatible with the previous version of the function. In other words, its interface (its name, the types of its parameters, and its return type) should stay the same, and its side effects and outputs (what it does and returns) should also stay the same. You can also think of this in terms of unit testing: the versions of the function before and after refactoring should have exactly the same set of unit test results.

Refactoring does not necessarily have to be a complex rewriting of code, and there are a number of reasons why you might want to rewrite code without changing its behavior. In this section, we will present a few types of refactoring, along with why you might want to refactor code this way.

### Renaming Variables

Perhaps the smallest change you can make in refactoring is renaming a variable. You might rename a variable to make it clearer what it represents or because it is too similar to another name. Refactoring a function in this way helps improve your code's readability.

Take this function, for example (docstring omitted for brevity):

```python
G = 6.67e-11

def grav_force(m1, m2, r):
    return G * m1 * m2 / r ** 2
```

You might recognize this as a function to calculate the gravitational force between two objects, but this is hard to tell if you don't have familiarity with the specific formula the function is based on. In part, this is because this function doesn't use good [variable name style](https://softdes.olin.edu/docs/readings/1-python-basics/#variable-name-style).

You could instead rewrite this function like this:

```python
GRAVITATIONAL_CONSTANT = 6.67e-11

def grav_force(mass_1, mass_2, distance):
    return GRAVITATIONAL_CONSTANT * mass_1 * mass_2 / distance ** 2
```

While it's more typing, it's also easier to read and understand.

### Rewriting Code Blocks

Sometimes, you discover a new feature or code pattern in Python that makes it much easier to write part of a function. For example, suppose that you wanted to find the average value of a list of numbers, and you had this (again, docstring omitted for brevity):

```python
def list_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)
```

This function is completely correct. If you then learn about the [`sum` function](https://softdes.olin.edu/docs/readings/2-sequences-testing-state/#list-functions) (or remember that you could use it here), you can replace the `for` loop in the function:

```python
def list_average(numbers):
    total = sum(numbers)
    return total / len(numbers)
```

At this point you might notice that you could further refactor this function into a single line:

```python
def list_average(numbers):
    return sum(numbers) / len(numbers)
```

As you learn more in Python, we encourage you to revisit and refactor your old code.

### Splitting Functions

After you write a function, you may find that it is rather long or complicated for a single function. Splitting these functions into smaller, simpler functions can be a useful refactoring tool in this scenario. Doing so lets each function focus on a single conceptual task, makes it easier to see the major steps of your original function, and makes your code more readable overall.

For example, suppose that you have a list of lists of strings, representing a tic-tac-toe board with some squares filled in. This might look like this (formatted for readability):

```python
[["X", "O", "X"],
 [" ", "X", "O"],
 ["O", " ", "X"]]
```

To check whether a player had won, you could write this function:

```python
def player_won(board, symbol):
    """
    Check whether a player won a game of tic-tac-toe.

    Args:
        board: A list of lists of three strings, representing the game board.
        symbol: A string representing the player's symbol ("X" or "O").

    Returns:
        True if the player with this symbol has won, and false otherwise.
    """
    return (board[0][0] == board[0][1] == board[0][2] == symbol
            or board[1][0] == board[1][1] == board[1][2] == symbol
            or board[2][0] == board[2][1] == board[2][2] == symbol
            or board[0][0] == board[1][0] == board[2][0] == symbol
            or board[0][1] == board[1][1] == board[2][1] == symbol
            or board[0][2] == board[1][2] == board[2][2] == symbol
            or board[0][0] == board[1][1] == board[2][2] == symbol
            or board[0][2] == board[1][1] == board[2][0] == symbol)
```

This is correct, but it is not very easy to understand, and it is easy to make a mistake by mistyping a single character.

One way to think about this problem (checking whether someone has won a game of tic-tac-toe) is to think through the steps of how you would solve this. You might think of a strategy like this:

- First, check each row to see if the player has won on that row (i.e., three of the same symbol going across).
- Then, check each column to see if the player has won on that column (i.e., three of the same symbol going down).
- Finally, check the diagonals to see if the player has won on a diagonal.

Each of these checks could be its own function. So you might split `player_won` into smaller functions, like this (all docstrings omitted for brevity):

```python
def player_won_row(board, symbol):
    return (board[0][0] == board[0][1] == board[0][2] == symbol
            or board[1][0] == board[1][1] == board[1][2] == symbol
            or board[2][0] == board[2][1] == board[2][2] == symbol)


def player_won_column(board, symbol):
    return (board[0][0] == board[1][0] == board[2][0] == symbol
            or board[0][1] == board[1][1] == board[2][1] == symbol
            or board[0][2] == board[1][2] == board[2][2] == symbol)


def player_won_diagonal(board, symbol):
    return (board[0][0] == board[1][1] == board[2][2] == symbol
            or board[0][2] == board[1][1] == board[2][0] == symbol)


def player_won(board, symbol):
    return (player_won_row(board, symbol)
            or player_won_column(board, symbol)
            or player_won_diagonal(board, symbol)
```

Now the same code has been split over multiple functions, but each unit is easier to read.

There is still the problem that in each of the smaller functions, it is easy to mistype a character, not notice, and end up with an incorrect function. Fortunately, there is a solution: we could refactor some of _these_ functions! For checking if a player won a row, we could do this:

```python
def player_won_row(board, symbol):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == symbol:
            return True
    return False
```

By using a `for` loop, we have much less repetitive code, and it is easier to catch an error like accidentally typing `board[0][1]` instead of `board[1][0]`.

So not only is splitting up function a useful refactoring tool on its own, it can also help you identify places to further refactor your code.

### Changing Algorithms

Finally, you can refactor a function by changing your _algorithm_, the overall approach you take to solving the problem. For example, suppose that you wanted to calculate the factorial of a positive integer n (which is the product of multiplying all of the positive integers from 1 to n).

You could do this with recursion, like this:

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

But if you later felt that it would be more readable to write the function using a `for` loop, then you could refactor the function as follows:

```python
def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product
```

Each of these algorithms has its own tradeoffs in terms of conceptual hurdles, readability, likelihood of mistakes, etc., and ultimately, you are the judge of which algorithm is best suited for your requirements.

Sometimes you will find that one algorithm is more complicated to write and understand, but runs much faster than another for most inputs. If you need to write fast code for your use case, it might make sense to refactor your code to implement this algorithm.

But your use case might not call for this - for example, perhaps your code is used in a command that a user runs in the terminal, and refactoring will drop your running time from 1 millisecond to 1 microsecond. From the user's perspective, both are essentially instantaneous, and thus using the more complicated but faster algorithm would not necessarily be a good choice.

Again, the call of whether to refactor or not lies with your reasoning. But hopefully, this section has given you an idea of how you might refactor code in different situations.
