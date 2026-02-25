import random
import math


# This code creates two random numbers between 1 and 50

first = random.randint(1,50)
second = random.randint(1,50)

print(f"My random numbers are: {first} and {second}.") # This code prints two random numbers and states what those numbers are in a sentence.

# The code below compares the first and second number, than states which one is bigger, or if they are equal.
if(first > second):
    larger = first
    smaller = second
    print(f"{first} is the larger number.")
elif(first < second):
    smaller = first
    larger = second
    print(f"{second} is the larger number.")
else:
    smaller = larger = first = second
    print(f"{first} and {second} are equal") 

# The two small blocks of code below divide both numbers by two using remainder division, and if the remainder is zero, then state that the number is even.
if(first%2 == 0):
    print(f"{first} is an even number.")

if(second%2 == 0): 
    print(f"{second} is an even number.")

#  This code states whether or not the larger number is exactly divisible by the smaller number by performing remainder division - dividing the larger number by the smaller number. 
# If it isn't exactly divisible, state the remainder.
if(larger%smaller == 0):
    print(f"{larger} is perfectly divisible by {smaller}.")
else:
    remainder = larger%smaller
    print(f"The remainder is {remainder}.")

# This code assigns the larger number to the hypotenuse, 
# and the smaller number to "side A", then in the variable "side_B", performs the pythagoras theorum: B = square root of c squared minus a squared, where c is the hypotenuse.
hypotenuse = larger
side_A = smaller
side_B = math.sqrt(larger**2 - smaller**2)

# This code prints a statement that explains how side B is calculated using the pythagoras theorum.
print(f"By using {larger}m as the hypotenuse, and {smaller}m as Side A, after using Pythagoras Theorum, Side B equals to {round(side_B)}m when rounded to the nearest number.")