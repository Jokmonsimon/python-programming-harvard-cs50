# Float is a number with fractional digits
# Sum two floats x and y
x = 2.4
y = 3.2
z = x + y

print(z)
print(type(z))
print("-------------------------------------------------------")

# Ask user to input float values
x = float(input("Enter the value x: "))
y = float(input("Enter the value y: "))
z = x + y

print(z)
print(type(z))
print("-------------------------------------------------------")

# Round the value of z
z = round(x + y)

print(z)
print(f"{z:,}")
print(type(z))
print("-------------------------------------------------------")

# ROund to nearest digit after Division
z = round(x / y, 3)
print(z)
print(f"{z:.3f}")