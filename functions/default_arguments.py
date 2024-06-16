#you can assign a default value for a parameter in case a user doesnt provide an argument. This is useful for when
# You have a param utilized in the logic, but that is essentially optional.
# Optional params must come after all the required ones.

def get_greeting(email, name = "there"):
    print(f"Hello {name}, you have entered {email} as your email!")

get_greeting("layman212@gmail.com")
get_greeting("layman212@gmail.com", "Enki")