# Comment: these are here for the author/editor

"""
This is a multi line
comment
"""

#if you have () after a word, you are 'Calling it'
# fn takes built up logic and hides it for you
print(...) # built-in function

# fn adds words to our vocab that we can use
def greet():
    print('This is my first fn')

greet()

# Example of var assignment
f_name = 'Chelsey' # snake case
fName = 'Belsey' # camel case
fname= 'Chels'
name2 = 'Something' # Numbers in var allowed, just not at start
print(f_name, fname, fName)
# concatenation
print(f_name + ' ' + 'is my name.')

x = 5
y = 10
# py respects math, but not precise (gotcha)
print(x * y) # * / // ** - +
# reassignment
x = 10
print(x * x)

# ERROR: unsupported operand type(s) for +: 'int' and 'str'
# print(5 + f_name)

# can take in data and run something on it
# This is giving us data back.
usr_input = input('> ')
print(usr_input)