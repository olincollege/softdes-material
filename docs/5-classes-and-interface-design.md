---
title: Reading 5 - Classes and Interface Design
nav_order: 9
layout: default
---

# Reading 5: Classes and Interface Design

Every object in Python has a type, such as `int` or `list`, that determines what you can do with that object. The types that you have learned so far in this course have been useful for a variety of programming tasks - you can store text as a `str`, count the frequency of each character in the text using a `dict`, or find the unique characters used in the text using a `set`.

In this reading, we will discuss how you can define your own types through _classes_. By using classes, you can create objects that are well-suited to the programming task at hand. These objects essentially bundle data along with functions to read, process, or modify this data for a particular purpose. We will also discuss how to design a good _interface_ for a class, that is, the set of functions that the class provides.

## Classes

A _class_ is essentially a collection of data and functions designed to be used for a specific purpose. Classes are used to define new types, and once you have declared a class, you can create new objects of that class called _instances_ in your code.

Because the distinction between a class and an instance can be confusing, we will start by discussing this in more detail before covering how to define a class.

### A class is a type, and an instance is an object 

Suppose you create an empty set object like this:

```python
words = set()
```

After this line executes, `words` is a set, and specifically, it is an _instance_ of a set. Its type is `set`, but `words` is not equal to the `set` type itself (`words == set` is `False`). If you want to check that `words` is of the set type, you use `isinstance(words, set)`, checking that `words` is an instance of the `set` type.

In the context of classes, this distinction is important, because some data can belong to the class as a whole while other data can belong to a specific instance of that class.

### Classes have their own syntax and style

Here is an (incomplete) example class that we will use throughout this section to illustrate the various features of classes:

```python
class PlayerSpaceship:
    
    model = "Anscombe 4X"
    mass = 1000  # kg
    engine_span = 10  # m
    
    def __init__(self, pilot):
        self.pilot = pilot
        self.fuel = 100  # Liters
        self.angle = 0  # Radians
        self._left_engine_thrust = 0  # Newtons
        self._right_engine_thrust = 0  # Newtons
        
    def __repr__(self):
        return f"({self.pilot}, {self.fuel}, {self.angle}, " \
               f"{self._left_engine_thrust}, {self._right_engine_thrust})"
        
    def set_left_thrust(self, thrust):
        self._left_engine_thrust = thrust
        
    def set_right_thrust(self, thrust):
        self._right_engine_thrust = thrust
        
    def total_thrust(self):
        return self._left_engine_thrust + self._right_engine_thrust
    
    def rotational_velocity(self):
        clockwise_thrust = self._right_engine_thrust - self._left_engine_thrust
        return clockwise_thrust * engine_span / 2
```

You declare a class using the `class` keyword, followed by the name of the class. The body of the class, like the body of a function, is indented by four spaces. A class can contain variables and functions.

Unlike most variable names, class names should begin with a capital letter, and if the name consists of multiple words, it should be written in camel case (`PlayerSpaceship`) rather than snake case (`Player_spaceship`).

Within classes, function definitions are separated by one blank line instead of two. Class definitions should be separated from one another by two blank lines. Automated style checkers such as `pycodestyle` will check for this spacing.

### `self` refers to an instance of a class [#](#self-refers-to-an-instance-of-a-class)

Except in a few rare cases that we will not discuss here, a function defined within a class is designed to be used by an instance of that class. This kind of function is called a _method_. Every method has to take `self` as its first parameter, which refers to the specific instance of the class. Data belonging to an instance of a class can be set or read using `self` as well. You can see this in the `PlayerSpaceship` class:

```python
class PlayerSpaceship:
    
    # Only the relevant part ot this class is shown for this example.

    def set_right_thrust(self, thrust):
        self._right_engine_thrust = thrust
        
    def total_thrust(self):
        return self._left_engine_thrust + self._right_engine_thrust
```

In this class, each `PlayerSpaceship` instance has its own name. The `set_right_thrust` method takes `self` as its first parameter, and the reference to `self._right_engine_thrust` in this method represents a variable called `_right_engine_thrust` that belongs to the class instance. This kind of variable is called an _attribute_ of the instance.

The `self` parameter does not appear when actually calling the function, though. If `spaceship` was a `PlayerSpaceship` instance, you would set its name like this:

```python
spaceship.set_right_thrust(50)
```

You can access a variable set in this way like `spaceship.pilot`, so for example, if you wanted to print the pilot’s name for this spaceship, you could call `print(spaceship.pilot)`. Variables like this that belong to a class instance are called _attributes_ of the instance.

Note that `self` is not available outside of methods, so you cannot do something like this:

```python
# WARNING: This code will not work.
class InvalidSelf:
    self.name = ""
    # Define other things here.
```

As you see from the beginning of the `PlayerSpaceship` class, you _can_ define variables without `self`:

```python
class PlayerSpaceship:
    
    # Only the relevant part of this class is shown for this example.
    
    model = "Anscombe 4X"
    mass = 1000  # kg
    engine_span = 10  # m
```

However, this has a slightly different meaning, as we will explain later.

### Use the class name to create an instance of a class [#](#use-the-class-name-to-create-an-instance-of-a-class)

Remember from Reading 2 that to create a new, empty set, you use the following syntax:

```python
empty_set = set()
```

To create a new instance of a class, you can use a similar form. For the `PlayerSpaceship` class above, you could do the following:

```python
spaceship = PlayerSpaceship("Major Tom")
```

### Use `__init__` to set up a class instance [#](#use-__init__-to-set-up-a-class-instance)

The `PlayerSpaceship` class has a special method called `__init__`:

```python
class PlayerSpaceship:
    
    # Only the relevant part of this class is shown for this example.
    
    def __init__(self, pilot):
        self.pilot = pilot
        self.fuel = 100  # Liters
        self.angle = 0  # Radians
        self._left_engine_thrust = 0  # Newtons
        self._right_engine_thrust = 0  # Newtons
```

You would still be able to create an instance of `PlayerSpaceship` without this method. But if you do so, you may be surprised to learn that trying to access `spaceship.pilot` (where `spaceship` is a `PlayerSpaceship` instance) results in an error message:

```
AttributeError: 'PlayerSpaceship' object has no attribute 'pilot'
```

This is the case even for variables such as `_left_engine_thrust` that are set in other methods of `PlayerSpaceship` - trying to access the variable will result in an error until some method sets its value.

The `__init__` method is usually not called directly, but executes automatically when creating a new class insance.

### Use `__repr__` to represent a class as a string [#](#use-__repr__-to-represent-a-class-as-a-string)

The `PlayerSpaceship` class also has a special method called `__repr__`:

```python
class PlayerSpaceship:
    
    # Only the relevant part of this class is shown for this example.

    def __repr__(self):
        return f"({self.pilot}, {self.fuel}, {self.angle}, " \
               f"{self._left_engine_thrust}, {self._right_engine_thrust})"
```

Without this method, printing a `PlayerSpaceship` instance would produce a result like this:

```
<__main__.PlayerSpaceship object at 0x7efccdd24f10>
```

The `__repr__` method allows you to define your own string representation of a class instance. It must take only `self` as a parameter and return a string. Ideally, the `__repr__` method should return the information required to build a copy of the instance - in our case, making a copy of a `PlayerSpaceship` instance requires all of its attributes.

It is especially helpful to write a `__repr__` method because it can help others as they use your code. If someone else is using your class and wants to print out an instance for debugging purposes, a well-implemented `__repr__` method will be useful indeed.

Like the `__init__` method, a class’s `__repr__` method is usually not called directly, but is automatically called as a result of calling `print` or `str` on a class instance.

### Use a leading underscore to indicate internal attributes or methods 

You may have noticed that the `PlayerSpaceship` class has attributes named `_left_engine_thrust` and `_right_engine_thrust`, with a leading underscore in the name of each. This is done to indicate that these variables should not be accessed outside of the class’s implementation.

In practice, nothing stops you from actually accessing and changing such an attribute, so the following code will execute:

```python
spaceship = PlayerSpaceship("Major Tom")
spaceship._left_engine_thrust = 50
```

Thus naming attributes or functions in this way is mostly as a reminder to you and to those using your code, much like the use of `_` as a variable name. That being said, some automated checkers in IDEs like VS Code will generate a warning if your code accesses an internal attribute or method outside of a class.

### Classes can also have attributes 

At the beginning of the `PlayerSpaceship` definition, we defined some variables like this:

```python
class PlayerSpaceship:
    
    # Only the relevant part of this class is shown for this example.
    
    model = "Anscombe 4X"
    mass = 1000  # kg
    engine_span = 10  # m
```

These are called _class attributes_ and are shared among all instances of the `PlayerSpaceship` class. You can access these attributes either through the instance or through the class name itself, so if `spaceship` is an instance of `PlayerSpaceship`, both `spaceship.mass` and `PlayerSpaceship.mass` will be 1000.

You can change `PlayerSpaceship.mass` by assigning directly to it, but this will have surprising results:

```python
PlayerSpaceship.mass = 42
print(spaceship.mass)  # This will print 42 instead of 1000
```

Perhaps even more surprisingly, this does not apply in the reverse direction: if you try to assign a new value to `mass` through `spaceship`, it does not carry through to `PlayerSpaceship` or to other instances of the class:

```python
# Assume that PlayerSpaceship is currently 1000 as originally defined.
spaceship.mass = 42
print(PlayerSpaceship.mass)  # This will still print 1000
```

This is because the statement `spaceship.mass = 42` creates a new _instance attribute_ and sets its value to 42 instead. If an instance attribute and class attribute have the same name, the more specific one (the instance attribute) takes precedence.

Be careful with class attributes! When in doubt, always change its value through the class name, but in general, you should avoid changing class attributes at all if possible.

### Classes should have docstrings 

Like functions, classes should have docstrings. The format is nearly identical to that of functions, except that you should list the attributes of the class:

```python
class PlayerSpaceship:
    """
    Player-controlled spaceship used for all levels.
    
    Attributes:
        model: A string representing the spaceship model name.
        mass: An int representing the mass of the spaceship in kilograms.
        engine_span: An int representing the distance in meters between the
            spaceship's left and right engines.
        pilot: A string represent the name of the spaceship pilot.
        fuel: An int representing the fuel level of the spaceship.
        angle: A float representing the current angle of the spaceship in
            radians, with 0 being the spaceship nose pointing right.
    """
    
    # Only the relevant part of this class is shown for this example.
```

Internal attributes do not need to be listed in the docstring, but you should still document their type and what they represent in the class implementation.

Methods, like any other function, should have a docstring with the usual formatting.

### Documenting Exceptions 

“Raises” can be used to list all exceptions relevant to the function followed by a description of the exception. Exceptions that are raised due to a violation of the conditions present in the docstring should not be included.

```python
class PlayerSpaceship:
    def set_thrust():
        """
        Sets the thrust of the PlayerSpaceship to values given by the user.

        Returns:
            None.
        Raises:
            ValueError: Inputted value is not an integer.
        """
        try: 
            left = int(input("Enter left thrust:"))
            right = int(input("Enter right thrust:"))
            self._left_engine_thrust = left
            self._right_engine_thrust = right
        except ValueError:
            print("Not a valid number.")
```

## Interface Design 

So far, we have discussed several aspects of how you _can_ design and implement classes, but we have not yet described how you _should_ design and implement classes. As you design a class, it is particularly important to consider your class’s _interface_, that is, the set of public attributes and methods it offers for other code to interact with it.

### Public & Private 

Prior to entering this section, make sure that you are at least somewhat familiar with the following terms:

*   public - when a variable or function can be accessed and modified **outside of** the class that it is part of
*   private - when a variable or function can only be accessed and modified **within** the class that it is part of
*   instance variable - a variable that is initialized on an instance by instance basis and can differ between instances
*   class variable - a variable that is the same for all instances of a single class

### Deciding on Public Versus Private 

Determining whether variables should be public or private typically should be done before any code is written in order to minimize the amount of refactoring that you have to do.

“Private” variables are those that will never be modified outside of the class that they are within. Private variables are represented by adding `_` as a prefix to the variable’s name. For example, a variable storing the name of an object would be `_name` as opposed to `name`. While this is merely a syntax change (you won’t get an error for trying to modify the variable outside of the class it was created within), it makes code easier to read both for yourself & others.

#### Use private instance attributes in almost all cases 

In general, you should make instance attributes private. By making an instance attribute private, you can have more confidence that it will be accessed and modified only in the way that you have implemented in the class methods.

As an example, suppose that you were writing a class to represent a character in a role playing game, like this:

```python
class Character:
    
    # Only the relevant part of this class is shown for this example.
    
    def __init__(self, name):
        self.name = name
        self.max_health = 10
        self.health = self.max_health
```

While this might seem like a reasonable way to implement the class, the fact that all of the instance attributes are public can cause some issues. A minor problem is that the character’s name can be changed by any other function, including those outside of the `Character` implementation. A more serious problem is that the character’s health can be changed to beyond its maximum value.

To see an example of this, suppose that you can restore a character’s health by using a potion. However, if the potion code is just the following, a character at full health would now have a value that is technically not allowed:

```python
character.health += 25  # This could result in a health greater than max_health
```

Because of this, it would be better to provide several functions that can increase, decrease, or view the character’s health, like this:

```python
class Character:
    
    # Only the relevant part of this class is shown for this example.
    
    def __init__(self, name):
        self._name = name
        self._max_health = 10
        self._health = self._max_health
        
    def heal(self, amount):
        self._health = min(self._health + amount, self._max_health)
        
    def damage(self, amount):
        self._health = max(self._health - amount, 0)
        
    def get_health(self):
        return self._health
```

By using private instance attributes in this way, you can ensure that the “state” of your class instances always remain valid. Again, you cannot stop code from changing the values of these attributes, but a private instance variable will make it a bit easier for you or a user of your code to realize that doing so is a mistake.

##### Only use public instance attributes for data containers 

If your class is simply designed to “hold data” and not do anything with it, or if your class has no “invalid” set of instance attributes, it is fine to make the instance attributes public. For example, if you have a class designed to represent an object in a physics simulator, you might define it like this:

```python
class Object2D:
    
    def __init__(self, x, y, velocity, label=""):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.label = label
```

This class is essentially equivalent to a tuple of four elements, except that rather than accessing its elements like `obj[0]`, you can do so using `obj.x`. This type of class is sometimes referred to as a “named tuple” for that reason. In this case, it is appropriate to define the instance attributes as public, since changing the attributes does not really affect the validity of the object.

If you want to use a class like this, you may find it useful to use the [`collections.namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple) class in the Python standard library.

### Methods should access private instance attributes or methods 

#### Avoid exposing implementation details 

Finally, you should avoid exposing the internal details of a class’s private instance attributes in the interface of the class. Suppose that you create a class that keeps a list of integers, like this:

```python
class AccountChecker:
    
    # Only the relevant part of this class is shown for this example.

    def __init__(self):
        self.accounts_to_check = []
```

Now suppose that `accounts_to_check` contains a series of integers representing the ID numbers of the accounts to check, and that accounts need to be checked in order of increasing ID.

If `accounts_to_check` is not kept in sorted order, then you would have to repeatedly find the minimum element of `accounts_to_check`, check it, and then remove it. If you did not make this a part of the `AccountChecker` class, you would have to write this code in a function external to the class.

However, this also means that if later you decided to change `accounts_to_check` to a different class that you had designed, you would likely have to change every program that accesses it. A better design would be to make `accounts_to_check` a private attribute and create a method to calculate the next account to check, like this:

```python
class AccountChecker:

    # Only the relevant part of this class is shown for this example.

    def __init__(self):
        self._accounts_to_check = []
        
    def next_account(self):
        return min(self._accounts_to_check)
```

In this way, if you ever change the type of `_accounts_to_check`, you can simply change the implementation of `next_account` and existing code that uses `AccountChecker` will continue to operate as is.

### Properties 

Properties are a feature of python that allows for creating “getters” in classes by adding the `@property` decorator tag prior to a function.

While making variables private prevents modification of attributes from outside of the class, it also makes them inaccessible since you should never be calling a private variable outside of a class. As a result, properties can be used to generate a getter that allows you to access a copy of that attribute which contains the same value as the private attribute.

For example with the character class example above, the `get_health()` function can be replaced with a health property:

```python
class Character:
    
    # Only the relevant part of this class is shown for this example.
    
    def __init__(self, name):
        self._name = name
        self._max_health = 10
        self._health = self._max_health

    @property
    def health(self):
        return self._health
```

The usage of the `health` property can be seen below:

```python
character_a = Character("A")
print(character_a.health)
```

Note that attempting to set `character_a.health` to another value will not change the the `_health` instance variable of `character_a`.