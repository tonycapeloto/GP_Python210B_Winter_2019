'''
In this file, we are going to build three functions that are intended to break:
NameError, TypeError, SyntaxError, and AttributeError
'''

# 1. exception NameError
# Raised when a local or global name is not found. This applies only to unqualified names.
# The associated value is an error message that includes the name that could not be found.

def names(x):
    return x

names(x)

# 2. exception TypeError
# Raised when an operation or function is applied to an object of inappropriate type.
# The associated value is a string giving details about the type mismatch.

# This exception may be raised by user code to indicate that an attempted operation on an
# object is not supported, and is not meant to be. If an object is meant to support a given
# operation but has not yet provided an implementation, NotImplementedError is the proper
# exception to raise.
#
# Passing arguments of the wrong type (e.g. passing a list when an int is expected) should
# result in a TypeError, but passing arguments with the wrong value (e.g. a number outside
# expected boundaries) should result in a ValueError.

a = 'hello'
b = 5

def types(a, b):
    return a + b

types(a, b)

# 3. exception SyntaxError
# Raised when the parser encounters a syntax error. This may occur in an import statement,
# in a call to the built-in functions exec() or eval(), or when reading the initial script
# or standard input (also interactively).
#
# Instances of this class have attributes filename, lineno, offset and text for easier
# access to the details. str() of the exception instance returns only the message.

def synt(a):
    return a

synt(a))

# 4. exception AttributeError
# Raised when an attribute reference (see Attribute references) or assignment fails.
# (When an object does not support attribute references or attribute assignments at all,
# TypeError is raised.)

def attr(b, a):
    return b.append(a)

attr(b, a)
