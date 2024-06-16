# The way scope in python works we have two kinds of scope. Global scope, and function scope.
# Global scope is created as soon as a program is run, it is the outermost scope of the program. Variables
# declared in global scope are accessible from all other scopes.
# Function scope is created whenever a function is defined. Variables scoped to that function are only accessible from within
# that function and from within functions defined within that function. 
# You cannot access variables within lower scopes, only within the scope or upper scopes.
# In python variables are not block scoped like they are in other languages, instead they are strictly scoped to their function

# in global scope, accessible in all other scopes
x = 5 

def f():
    # Function scope is created for the function f, can access the variables x and y 
    y = 10

def g():
    # Function scope is created for the function g, can access the variables x, z, and the function h 
    z = 20

    def h():
        # Function scope is created for the function h, can access the variables x, z, and a
        a = 1

def get_names():
    names = ["lane", "enki", "bat"]

    for name in names:
        x = name

    # In most languages this would result in an error, but in python block scope does not exist, so x is not scope to the
    # for loop, its scoped to the function it lives in. 
    print(x)