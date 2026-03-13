
# Explicit Type Casting = converting one data type to another by user.

a = "1"
# a1 = 1
b = "6"
# b1 = 6
# print(a+b) 
print("Before Type Casting : ", a + b)  # Concatenation of strings
print("After  Type Casting ",int(a)+int(b))  # Addition after type casting to integers


#implicit Type Casting = automatic conversion of one data type to another by python interpreter.
x = 5       # int
y = 2.5     # float 
z = x + y   # implicit type casting from int to float
print("The value of z is :", z)

 