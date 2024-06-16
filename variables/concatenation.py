#Most of the math operators do not work on strings in python. One of the exceptions is the + operator. THis is called
#concatenation, and essentially fuses two or more strings into a single string

f_name = "Enki"
l_name = "Layman"
full_name = f_name + " " + l_name

print(full_name)

#You should favor f strings over concatenation

full_name = f"{f_name} {l_name}"