# bitwise operators are similar to logical operators, except instead of operating on boolean values they operate on all
# the bits of a value. The symbol for bitwise and is &

# For example if we have 5 & 7

# 5 in binary is 0101
# 7 in binary could be 0111

# The & operator converts each value to its binary form and compares the individual bits of their binary forms against 
# eachother. 0 is false and 1 is true 

# So if we have 0101 & 0111
# 0 & 0 is 0
# 1 & 1 is 1
# 0 & 1 is 0
# 1 & 1 is 1
# The result is 0101 which is 5. 

# 5 & 7 = 5 


# When writing a number in binary the 0b prefix indicates that the following number is in binary so 0b0101 is 5 0b0111 is 7

binary_five = 0b0101
binary_seven = 0b0111
print(binary_five & binary_seven)



# Sometimes applications store user permissions as binary values.

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

# if they had all permission 
user_permissions = 0b1111

# if they had none
user_permissions = 0b0111

# To check for say the can_review_guild permission, we would do a bitwise check on the users permissions with the specific
# permission we're trying to check. if the result is the same binary as the permission we know they have that permission

# The bin() function allows you to convert a value to its binary form. 
print(bin(can_review_guild), bin(user_permissions & can_review_guild))


# The bitwise or operator works similar to bitwise and except it conducts an or operation on the individual bits. | is the
# bitwise or symbol. 

