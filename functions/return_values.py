#When a function is not given a return value it returns None by default

def my_func():
    print("I do nothing")
    return None

def my_func2():
    print("I do nothing")
    return

#You can also leave out the return keyword, and it will be added implicitly after all the code in the body is executed.

def my_func3():
    print("I do nothing")


# Just as you can assign multiple variables on line you can return multiple values from one function, and then capture those
# Those values in multiple variables.

def ice_blast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana

print("Cast ice blast!")

dmg, mana = ice_blast(5, 100)
print(f"Damage: {dmg}, Remaining Mana: {mana}")