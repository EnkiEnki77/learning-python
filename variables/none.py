#If you know you need to capture a value in a variable, but you dont know what that value will be until later, use the 
# None type as the value. For example, if you need to capture the input of a user in a variable use None in this instance
# Because you wont know what the value will be until the user gives the input. 

user_age = None
#Instead of 
user_age2 = 0
#Because 0 is technically a valid age. This will help with logic later on. 

#When checking for bugs it can be confusing that the type None and the string None both print as the same to the console
#So use the type function to differentiate

print(type(user_age))
