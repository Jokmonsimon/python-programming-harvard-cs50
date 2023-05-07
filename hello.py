# Ask user for their name
name = input("What is your name? ")

# Remove whitespaces from string
name = name.strip()

# Capitalize user's name
name = name.capitalize()
name = name.upper()
name = name.lower()

# Say Hello user!
print("Hello,", name)
print("Hello, " + name)
print("Hello, {}!".format(name))