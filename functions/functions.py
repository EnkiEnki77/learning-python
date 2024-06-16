#Functions allow us to reuse and organize code.

#Say we wanted to write some code that calculates the area of a circle based on its radius

radius = 5
area = 3.14 * radius * radius

print(area)

#Great but say we wanted to now do the same thing, but with a circle that has a different radius

radius = 7
area = 3.14 * radius * radius

print(area)

#The above is tedious, we want to always strive to keep our code DRY (dont repeat yourself) this keeps us from having to 
# write the same code over and over, and keeps things organized and readable. To keep things DRY we have to utilize functions

#Functions in python are declared with the def keyword, followed by the variable name of the function
#The functions variable name has parentheses attached to it denoting it as a function. These parentheses may contain one
#or more input variables aka parameters. the parentheses are then followed by a colon
#The body of the function is indented, indicating that it exists inside the function.
#When a function is called all of the code within its body is executed the return keyword tells the function when to stop
#executing, the value placed after the return keyword is then output in place of wherever the function was called. 
#When a function is called you can pass it a value in its parens, this is known as the argument, and is saved in the corresponding
#parameter for the duration of the current execution of that function. The parameter values are purged when the function is
#returned. 
#Functions may have multiple returns. 

def circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

print(circle_area(10))
print(circle_area(12))

#Now we can do this operation with multiple different radius values without having to rewrite the code every time, we just
#have to call the function with a different input argument each time. 

#You can capture the return output of a function call in a variable

area = circle_area(20)

print(area)


#Functions can be given multiple parameters

def create_introduction(name, age, height, weight):
    first_part = f"My name is {name}, and i'm {age} years old."
    second_part = f"My height is {height}, and I weigh {weight}lbs"
    intro = f"{first_part} {second_part}"

    return intro

introduction = create_introduction("Enki", 25, "5'10", 158)
print(introduction)

