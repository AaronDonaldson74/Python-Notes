//Notes on Python Programming

-What is Programming?
Set of instructions to the computer

-Python Course Introduction
three types of students1)learn to program 2) web development 3) data science.

-How to Use Repl.it for Running Python in the Browser

-Basic Usage Tips and Tricks for the Python Repl

# Data types in Python--
1. Booleans
2. numbers
3. Strings
4. Bytes and byte arrays
5. None
6. Lists [] in JS are array
7. Tuples() 
8. Sets
9. Dictionaries {}

Monolithic one large application
Microservice is several smaller applications linked by APIs.

-Requirement Elicitation – A Guide for Feature Development

-Python String Basics
Use single quotes for lines with double quotes in it, and use double quotes for strings with single quotes in them. Also you can use a backslash \ to escape a single character.
# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment

sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper()

print(sentence)
print(sentence_two)

sentence = 'the quick brown fox jumped'.capitalize()
print(sentence)

sentence = 'the quick brown fox jumped'.title()
print(sentence)

sentence = 'the Quick Brown fOx jumped'
print(sentence.lower())

-How to Access Portions of Strings in Python
Use a brackets. 
# [start:stop:step]
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1 
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6  (slice position)
#    0   1   2   3   4   5    (index position)
Collapse
len function calls the length of the string.

Leaving the first or last number in the [:] takes it from the beginning, or takes it to the end automatically.e.g. [3:] goes from 3rd slice to the end.

-Guide to Heredocs in Python
multi-line comments. Use strip function to remove the new line (\n) and spaces.

-How to Build a Raw Multiline String in Python
print(repr(content)) shows the way the computer sees the text. #Useful in debugging.
long_string functions works opposite to repr function.

-Guide to Modern Python String Interpolation
start with f then {}. f is called an "f flag".

-How to Use Python's format method to Implement Index Based String Interpolation
string.format(etc.etc.etc) is an older way to do f strings, but you may see it from some older code.

-Finding a Substring in Python with: Find, Index, and In
Find, finds an object in the string, and gives you the index.
Index, finds the object in the string, but if it's not in the string, returns an error, and could break the program.
In, put at the end of the string, returns a boolean true or False to tell you if the string contains the object. 

-Using Python's replace Function to Find and Replace String Values
The original string cannot be changed, but the value can be changed with the .replace function. But the original is not changed. Just changing the reference to it.

-Guide to the Python split Function
split breaks a data type string into a list [ ]. Must have arguments, but if no arguments, then it converts the entire string into a list data type.
Partition returns a Tuple
Split returns a list.

-Using numberic values
print('Addition')
print(100 + 42)

print('Subtraction')
print(100 - 42)

print('Division')
print(100 / 42)
print(100 / 38)

print('Floor Division')
print(100 // 42)
print(100 // 38)

print('Multiplication')
print(100 * 42)

print('Modulus')
print(100 % 42)

print('Exponents')
print(100 ** 42)

-Different collections of data types:
    -Lists []
        In JS would be an array.
        .insert(index#, 'item to be added') adds a new element into a list at the index position.
        .append() adds a new element to the list at the end.
        .pop() removes the last item off the list
        .remove allows you to specify the item to be removed
        del variable[] allows you to delete an index number.
        Lists can be mixed types of objects. 
        Lists can be an object within a list.
        len() gives the number of items
        .index() gives the value of the
        .extend([]) adds an item to the end of the list.


    -Dictionary {}
        Dictionaries need "key": "Value", pair.
        .get function helps to keep a program from breaking if no dictionary is found.
        print(var.keys()) prints the keys
        -removing dictionary items.
        del only works if you know the value 100% certainty, else it will break the code. 
        Use .pop to set the removed value as a variable, and return the removed list. You can set a defined value to pop if none exhists so it doesn't break the code. 



    -Tuple ()
        works like a list, but is immutable cannot be changed so the values can be linked without worry they will break later in the program. similar to strings in python.
        adding to a tuple is possible but it will re-assign a different variable, even if it's the same variable name, it will be a different variable. 
            post = ('tuple', 'tuple', 'tuple',)
            post += ('another_tuple',)

        Removing from tuples. Reassignment
        1. removing from the end of the tuple
            post = post[:-1]
        
        2. removing from the beginning of the tuple.
            post = post[1:]
        
        3. removing specific element (messy/not recommended)
            post = list(post)
            post.remove('item')
            post = tuple(post)

Loops
    2 types for/in loops and While loops.

    for/in loops only loop once for each item in the variable.
    while loops will cycle indefinately until the condition is met, so you must specify a clear ending of the loop, or you'll just enter an infinite loop.

    While loop:


Conditionals, Yes or no questions. What does the program do if yes or no. 

Ternary operators in Conditionals
    Can add complexity to the code that makes it difficult to read uncessarily. 

comparison operators
    # List of comparison operators
# == Equality-any data set
# != Inequality-any data set
# <> Inequality (deprecated)-don't use per python rules etc.
# >  Greater than -numbers only
# >= Greater than or equal to -numbers only
# <= Less than -numbers only
# <= Less than or equal to -numbers only


Methods and functions.

Basic syntax for creating functions.
    def function_name_in_snake_case():
        print('Hi')

        #two lines of space after the definition of the function.
    function_name_in_snake_case()

Unpacking args (*args) leads to a tuple.
Unpacking kwargs (**kwargs) leads to a dictionary.
