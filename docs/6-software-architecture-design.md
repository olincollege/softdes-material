---
title: Reading 6 - Software Architecture Design
nav_order: 10
layout: default
---

# Reading 6: Software Architecture Design 

In the previous reading, we discussed classes and how you can use them to define your own types. In this reading, we will take a step back and consider the larger picture: how you can use a set of classes to create a larger, cohesive piece of software. Up to this point, the design of classes and functions together for a specific purpose has been largely given to you. Here, you will learn how to use composition and inheritance to describe how multiple classes relate to one another. We will then describe the model-view-controller (MVC) design pattern, a commonly used paradigm in interactive software that highlights some ways of using composition and inheritance in a larger context.

## Composition 

In a nutshell, _composition_ is combining multiple types or classes within a larger class. Composition allows us to conceptually represent multiple objects or types being used together for a particular purpose.

### Complex numbers illustrate simple composition 

A _complex number_ is the sum of a real and imaginary number, such as  \\(2 + 3i\\) (where \\(i\\) is the square root of -1). Thus, a complex number has a _real part_ (in this case, 2) and an _imaginary part_ (in this case, 3). If we were to write a class `ComplexNumber` to represent a complex number, we could think of it as being composed of its real part and its imaginary part, which in a class could be `float`s.

Stated another way, `ComplexNumber` is made up of two `float`s, which represent the complex number’s real and imaginary parts. These `float`s are used in operations involving `ComplexNumber` instances, such as adding or multiplying two complex numbers. In this way, the composition of two `float`s allows us to define more complex mathematical objects (pun intended).

### Composition is a “has-a” relationship 

Composition is sometimes referred to as a “has-a” relationship because of what it conceptually represents. In our complex number example above, the `ComplexNumber` class _has a_ `float` representing its real part, and also _has a_ `float` representing its imaginary part. In a Python class, this relationship would be expressed by making the `float`s instance attributes of the `ComplexNumber` class, like this:

```python
class ComplexNumber:
    """
    Representation of a complex number.
    
    Attributes:
        real: A float representing the real part of the number.
        imag: A float representing the imaginary part of the number.
    """
    
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
```

The has-a relationship of composition also implies some degree of ownership: because `ComplexNumber` has these `float`s, it is also responsible for managing their values. This is especially true for private instance attributes, as the owning class’s methods are the only thing that can access them.

### Composition can be nested 

A class can be composed of objects that are themselves compositions. For example, consider a game of Connect Four, in which two players take turns dropping disks into a board to try and form a row, column, or diagonal of four disks of their respective colors.

![Animation of Connect Four game](https://upload.wikimedia.org/wikipedia/commons/a/ad/Connect_Four.gif)

If we were to write a program to play a game of Connect Four, we might define an overarching `ConnectFourGame` class, which contains a `ConnectFourBoard` class and two instances of the `ConnectFourPlayer` class. The classes contained in the `ConnectFourGame` class can in turn be composed of other data types, and so on. For example, the `ConnectFourBoard` class might have instance attributes to keep track of which disks are in which spaces of the board and whose turn it is.

We could instead choose to place all of the individual instance attributes in the `ConnectFourGame` class, so that we would have just one large class that contained the board, each player’s information, etc. However, this is generally not considered good design because it does not make the components of the game very clear. In particular, player information is generally only handled by functions related to each player, and similarly for the game board. Logically, it makes more sense to make those classes of their own and compose the larger game using those classes.

Whether to compose a class using many small data types or a few larger types or classes comes down to choosing the right _level of abstraction_. Learning to find the right level of abstraction partially comes down to building up intuition through practice, but stepping back to think about what each component is doing in a larger context can be helpful as well.

In our Connect Four example, you can consider that from the game’s perspective, it really does not matter how the board stores its information (e.g., whether the pieces on the board are represented as a string, list, or a custom class) - all the game cares about is being able to tell the board to drop a piece in a specific slot or to get a sense of what pieces are where in the board. Because of this, it makes sense to have the game be composed of a board class, rather than the smaller data types that make up the board.

## Inheritance 

In a nutshell, _inheritance_ is the practice of using part of a class’s definition in another class. Inheritance allows us to more cleanly define similar classes, placing their similar behavior into one class while making smaller classes that handle their unique functionality.

### Game players illustrate simple inheritance 

Returning to our Connect Four example from above, notice that a game has a `ConnectFourPlayer` class. From the game’s perspective, it does not matter how each player makes their move - all the game needs is their move itself. Because of this, whether the player is a human and makes their move by entering their choice into a prompt, or whether the player is an AI that considers the current state of the board and a host of other information to make their move, the result given to the game is just the column in which the next disk will be dropped.

We can define a class that contains the bare minimum functionality needed for the game to get the appropriate information from the player (i.e., the color of the player’s disk and a method to get the player’s moves).

```python
class ConnectFourPlayer:
    """
    Representation of a Connect Four player.
    
    Attributes:
        color: An integer representing the color of the player's disks (0 for
            red, 1 for yellow).
    """
    
    def __init__(self, color):
        self.color = color
    
    def move(self):
        """
        Make a move on the Connect Four board.
        
        Returns:
          An integer between 0 and 6 representing the column in which to make
          the next move.
        """
        pass
```

We can then define a _subclass_ of `ConnectFourPlayer` that inherits all of the attributes and methods of the class, like this:

```python
class HumanC4Player(ConnectFourPlayer):
    """
    Representation of a human-controlled Connect Four player.
    """
    
    def move(self):
        choice = -1
        while choice < 0 or choice > 6:
            # Use input to read a choice from the user.
            choice = input("Enter an integer from 0 to 6: ")
        return int(choice)
```

Defining the class as `HumanC4Player(ConnectFourPlayer)` means that all attributes and methods defined in `ConnectFourPlayer` are available to `HumanC4Player` - in other words, `HumanC4Player` _inherits_ the attributes and methods of `ConnectFourPlayer`. However, `HumanC4Player` can _override_ any of the methods of `ConnectFourPlayer` by defining a method with the same name (as it does with `move`). An AI class could similarly override `move` to define its own way of picking its next move.

The advantage of this is that the `ConnectFourGame` class knows that it can call the `move` method of the player, and no matter what kind of player it is, the method will produce a move that the game can process.

### Inheritance is an “is-a” relationship 

Inheritance is sometimes referred to as an “is-a” relationship. Because a subclass inherits its attributes and methods from its parent class, an instance of the subclass is for all practical purposes an instance of the parent class and can be used in the ways that an instance of the parent class would. In our example above, a `HumanC4Player` _is a_ `ConnectFourPlayer`.

As with composition, inheritance can be nested. We could define a class called `AIC4Player` representing an AI player, and have it store the board used for the game. From there, we could define classes called `EasyAIPlayer`, `MediumAIPlayer`, and `HardAIPlayer` that all inherit from `AIC4Player`. Because these classes all inherit from a class that stores the game board, they all have access to the game board in their methods. However, each class can define its own `move` method and use the game board in different ways.

### Be careful when overriding methods 

Note that overriding a method makes the relevant method of the parent class not execute. For example, suppose that the `move` method of `ConnectFourPlayer` was instead this:

```python
def move(self):
    print("Calling move() in ConnectFourPlayer")
    return 0
```

If you created an instance of `HumanC4Player` and called its `move` method, you would _not_ see the message `Calling move() in ConnectFourPlayer` printed. This is because overriding a method is a bit like defining an instance attribute with the same name as a class attribute: the most specific one takes precedence. So if the parent class and subclass both define methods with the same name, the subclass’s one will be used.

This can be a particular problem when defining `__init__` methods, since we often want to use the attributes defined in the `__init__` methods of the parent class. To address this problem, we can use the `super` function, as describe below.

### Use `super` to access the parent class 

The built-in function `super` allows you to access methods in the parent class. This is particularly helpful when you want to add to a parent class’s method instead of replace it entirely.

Remember the `ConnectFourPlayer` class, which contains this `__init__` method:

```python
class ConnectFourPlayer:
    # Only the relevant portions of this class are shown here.
    
    def __init__(self, color):
        self.color = color
```

Suppose that we want to define the `AIC4Player` class, which inherits from `ConnectFourPlayer` and stores the game board as part of its attributes. Overriding the method, like this, will work, but is repetitive:

```python
class AIC4Player(ConnectFourPlayer):
    
    def __init__(self, color, board):
        # There is a better way of implementing this function, shown below.
        self.color = color
        self._board = board
```

Using super, we could instead simply call the `__init__` method of the parent class like this:

```python
class AIC4Player(ConnectFourPlayer):
    
    def __init__(self, color, board):
        super().__init__(color)
        self._board = board
```

The call `super().__init__()` does the following: `super()` gets the parent class of `AIC4Player`, which is `ConnectFourPlayer`, and then we call the `__init__` method of that class. This can be useful when creating subclasses of complex classes, or when creating nested subclasses that are several levels deep.

## The Model-View-Controller Pattern 

To illustrate how composition and inheritance might be used in a larger software project, we will use the example of designing a game of chess. In this example, we will also be highlighting the use of the _model-view-controller (MVC)_ paradigm, which is commonly used as the software architecture for interactive programs. MVC is an example of a _design pattern_, which is a specific software architecture that is commonly used for a specific application.

In short, the MVC architecture consists of three main components: the model, the view, and the controller. Each of these is responsible for a core feature of the system. MVC is designed for _modularity_: each of the model, view, and controller components offer an interface that allows it to be easily switched out with other classes. This design makes it straightforward to extend or improve components as time goes on.

In this example, we will provide a fairly minimalistic example that highlights the design of the system. If you want to see a more detailed (but not implemented) example for this game, you can view more annotated code at [this SoftDes chess MVC example](https://github.com/olincollege/softdes-material/tree/main/chess-mvc-example).

### The model represents the state of the system 

The _model_ represents the state of the system (i.e., the information maintained and managed by the system) at a given point in time. In our chess example, this would include the following at a minimum:

*   The pieces currently on the board (type and position)
*   Whose turn it is

There are other pieces of information that the board could store for convenience if we wanted it to, such as the history of moves or whether or not one side is in check. Additionally, for the purposes of certain special moves such as [castling](https://en.wikipedia.org/wiki/Castling) or [_en passant_](https://en.wikipedia.org/wiki/En_passant) captures, a board should store the necessary information to determine whether these moves are allowed on a given turn.

Given that in a chess game, we often access squares by rank and file, it would make sense to store the board as a two-dimensional list. Because there are 12 types of pieces in the game, we can represent each piece with a different integer (with an additional integer to indicate an empty square). This means that the board itself can be represented as a list of lists of ints.

When creating the board, we can set the next player’s move to be White, since that is the first player to move in chess. Each time a move is made, we can switch the next player to move from White to Black or vice versa.

This means that the beginning of our class might look something like this:

```python
class ChessBoard:
    
    white = 0
    black = 1
    empty_square = -1
    white_pawn = 0
    black_pawn = 1
    # Some pieces omitted here for conciseness.
    white_king = 10
    black_king = 11
    
    def __init__(self):
        self._next_move = self.white
        self._board = [[self.empty_square for _ in range(8)] for _ in range(8)]
```

This is a prime example of composition: the `ChessBoard` class is composed of some integers that define players and pieces, as well as a two-dimensional list of integer representing the positions of these pieces on the board.

Now we can define a series of methods that define actions used in the gameplay of chess. This includes things like:

*   Listing which squares a given piece can move to.
*   Returning whether a given side’s king is in check.
*   Determining whether moving a piece to a given square is a legal move.
*   Moving a piece from one square to another (if it is a legal move), and capturing a piece if one is there.

Each of these actions can be defined as methods of the `ChessBoard` class. During gameplay, these methods can be called to represent moves in the game.

### The view represents the human-readable representation of the system 

The _view_ is what translates the information stored by the model into a format that can be processed by users. In our chess example, the view takes a `ChessBoard` instance and “draws” a representation of it in some way to the screen.

There are many ways to represent a chess board - we could draw it in a text format, like this:

```
   a b c d e f g h
  +-+-+-+-+-+-+-+-+
8 |R|N|B|Q|K|B|N|R| 8
  +-+-+-+-+-+-+-+-+
7 |P|P|P|P|P|P|P|P| 7
  +-+-+-+-+-+-+-+-+
6 | | | | | | | | | 6
  +-+-+-+-+-+-+-+-+
5 | | | | | | | | | 5
  +-+-+-+-+-+-+-+-+
4 | | | | | | | | | 4
  +-+-+-+-+-+-+-+-+
3 | | | | | | | | | 3
  +-+-+-+-+-+-+-+-+
2 |p|p|p|p|p|p|p|p| 2
  +-+-+-+-+-+-+-+-+
1 |r|n|b|q|k|b|n|r| 1
  +-+-+-+-+-+-+-+-+
   a b c d e f g h
   
White (lowercase) to move next.
```

Unfortunately, this is not the most visually appealing, but it works for the purposes of showing the state of the board.

We could also show the board graphically, by for example creating a class to illustrate the moves over time, like this:

![Animated GUI for chess game](https://upload.wikimedia.org/wikipedia/commons/c/cc/Immortal_game_animation.gif)

To allow for a modular design in which we can easily swap out these two views for each other, we can use inheritance to define a generic view class. This class simply stores the chess board and defines a `draw` method to visually represent the board:

```python
class ChessView:
    """
    A visual representation of a chess board.

    Attributes:
        board: a ChessBoard instance representing the board to view.
    """

    def __init__(self, board):
        self._board = board

    def draw(self):
        pass
```

We can then define a `TextChessView` class that inherits from `ChessView` and defines its own `draw` method to print the text representation of the board to the screen. We can also define a `GraphicalChessView` class that inherits from `ChessView` and implements its `draw` method to create a window on which it can draw the board.

### The controller represents the input interface of the system 

The _controller_ translates inputs from the players into calls to the appropriate methods in the board. For example, if the player selects a specific move by typing text into a prompt or by clicking specific squares in a graphical interface, the controller interprets these actions to determine the specific move to attempt to make on the board.

As with the view, using inheritance here allows us to select different ways of providing input to the board. We could simply define a `ChessController` class that defines an empty method called `get_move` that gets some input from the user (such as text) and translates that into a starting and ending square on the board. These coordinates can then be used in the `ChessBoard` class to attempt to move a piece. We can then have subclasses `TextController` or `GraphicalController` that translate different types of input into these coordinates.

### Tie everything together with an overarching game class 

Once we have classes implemented for each of these components, we can use an overarching `ChessGame` class to tie everything together. This simply manages the ways in which these components interact. Here is a brief sketch of what this class would look like:

```python
class ChessGame:
    
    def __init__(self, board, view, controller):
        self._board = board
        self._view = view
        self._controller = controller
        
    def run_game(self):
        while not self._board.checkmate():
            self._view.draw()
            start_rank, start_file, end_rank, end_file = \
                self._controller.get_move()
            if self._board.is_legal_move(start_rank, start_file, end_rank,
                                         end_file):
                self._board.move(start_rank, start_file, end_rank, end_file)
            else:
                # Display that the attempted move is invalid.
                self._view.invalid_move()
```

With this class, we have another example of composition: the game is composed of the three major components in the MVC architecture, along with the methods required to make them interact and run a game of chess.