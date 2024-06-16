#The convention is to have a main() function that starts out your programs and wraps all other function calls. 
#That way you can call main as the last thing in the prgram and ensure all functions are declared before theyre called 
# WIthout having to worry about the order you define your functions

"""
health = 10
armor = 5
   
def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

add_armor(health, armor)

def print_health(nh):
    print(f"The player now has {nh} health!")

"""
#entrypoint function
def main():
    health = 10
    armor = 5
    add_armor(health, armor)
   
def add_armor(h, a):
    new_health = h + a
    print_health(new_health)


def print_health(nh):
    print(f"The player now has {nh} health!")

#All functions are defined before theyre called and are then only called in the main entrypoint function, so the order
#of which functions are defined is of no concern.
#The main functions purpose is to execute the main logic of the program, this includes declaration of global variables
#execution of other functions, etc. And this allows you to define your programs functions without having to worry about the
# the order in which you define them, regardless of what functions are calling eachother. 
#The only things that should be in the global scope are the definitions of all the functions within the program, and the call
#to the entrypoint.
main()
