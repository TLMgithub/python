#!/usr/bin/python
# comment lines out (like this line you're reading) with "#"
#===============================================================================
# print

# Python 2:
#   the "print" statement is not a function
#   therefore it is invoked without parentheses
# Python 3:
#   "print" is a function
#    must be invoked with parentheses

print  # print an empty line to stdout

print 'This is a message with single "quotes".'  # you can place double quotes within single quotes
print "This is a message with double 'quotes'."  # you can place single quotes within double quotes
print ('This is a message with single quotes & parenthesis.')
print ("This is a message with double quotes & parenthesis.")
print'no space needed right after "print"'

print

#===============================================================================
# variables & types

# Python is completely object oriented
#   not "statically typed"
# You don't need to declare:
#   variables before using them, or
#   their type
# Every variable in Python is an object.

# python supports three types of numbers:
#   integers
#   floating point numbers
#   complex numbers

#---------------------------------------
# define strings

# define string: single quotes
stringsingle='this is a variable with single "quotes"'

# define string: double quotes
stringdouble="this is a variable with double 'quotes'"

# define string: lowercase variable name
lower='lowercase'

# define string: uppercase variable name
UPPER='uppercase'

#---------------------------------------
# define numbers

# define integer
INT1=1

# define floating point number: explicitly
FLOAT2=2.0

# define floating point number: implicitly
FLOAT3=float(3)

#---------------------------------------
# print variables

print (stringsingle)
print (stringdouble)
print (lower)
print (UPPER)
print (INT1)
print (FLOAT2)
print (FLOAT3)

# change/reset variable
FLOAT3='spam & eggs'
print (FLOAT3)

#---------------------------------------
# define variables simultaneously

# numbers
a, b = 3, 4
print(a)
print(b)
print(a,b)

# strings
a, b = 'alpha', "beta"
print (a)
print (b)
print (a,b)

print

#===============================================================================
# simple operations

# operations: numbers
one, two = 1, 2
three=one+two
print (three)

# operations: strings
hello = "hello"
world = "world"

# operations: numbers
one, two = 1, 2
three=one+two
print (three)

# operations: strings
hello = "hello"
world = "world"

helloworld = hello + " " + world  # more spacing
print (helloworld)

helloworld=hello+' '+world        # less spacing
print (helloworld)

# Mixing operators between numbers and strings is not supported:
#print(one + two + hello)  # will error out

print

#===============================================================================
# if statements

# Python uses indentation for blocks, instead of curly braces.
# Both tabs and spaces are supported
#   the standard indentation requires standard Python code to use four spaces
#   two spaces is still OK

one=1
two = 2
THREE=3

if one == 1:
  print 'one is 1'
if two == 2:
  print 'two is 2'
if THREE == 3:
  print 'THREE is 3'

print

