# Ask user for their name
name = input("What is your name? ")

# Remove whitespaces from string
name = name.strip()

# Capitalize user's name
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# name = name.title()

# Say Hello user!
print("Hello,", name.strip().title())
print("Hello, " + name.strip().capitalize())
print("Hello, {}!".format(name).strip().upper())
print(f"Hello, {name.strip().lower()}!")
print(f"Hello, {name.strip().title().split()}")