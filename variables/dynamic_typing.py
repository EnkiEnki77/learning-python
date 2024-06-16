#Python is a dynamically typed language meaning you can assign a variable as a specific type, and then reassign it as
# a different one later
my_age = 5
print(type(my_age))

my_age = "5"
print(type(my_age))

#In almost all instances though, its bad to change the type of a variable. Instead you should just make a new one
speed = 5
speed_description = "5"

#Languages that arent dynamically typed such as Python or Javascript are statically typed such as GO or Typescript. This 
#means a type error occurs when a variable is attempted to be assigned a new type. 