import math
import random
import numpy

b_or_d = input("Please select one of the two options: 1 for Decimal to Binary, and 2 for Binary to Decimal.") # This prompts the user to select what number conversion they would like to perform.
num = 0 # This number here will be used to store the number that you get from converting a binary number.
largestPower = 0 # This will be used for decimal to binary, and will store the highest power in the input decimal number.
num_bi = "" # Empty string that will be used to store the number you get from converting a decimal number to binary.

# This code below activates when the second option in the prompt is chosen (Binary to Decimal)
if(float(b_or_d) == 2):
    bi_num = input ("Please enter your number in binary: ")
    powers = len(bi_num) - 1 # Sets the number of powers the program will cycle through to the length of the binary number string minus 1, as the last power is always 0.
    
    for char in (bi_num): # This loop occurs for each character in the input binary number.

        if(char == "1"): # If the character being selected is a 1,  
            num = num + (1 * 2**powers) # it will set our number to itself plus 1 times 2 to the power that we defined earlier,
            powers = powers - 1 # then it will minus 1 from that value.

        elif (char == "0"): # If the character being selected is a 0, minus one from powers
            powers = powers - 1
    
    print (num) # Prints the final result in decimal.


# The code below activates when the first option in the prompt is chosen (Decimal to Binary)
elif (float(b_or_d) == 1): 
    dec_num = input("Please enter number: ")
    
    if float(dec_num) != 2: # When the input number is not two, this code will run.
        while float(dec_num) >= 2: # This while loop keeps dividing the input number by 2 until it drops below 2, and adds 1 to the power counter, to figure out the largest power of 2 that goes into the input number..
            dec_num = float(dec_num) / 2
            largestPower = largestPower + 1    
    
    loops = largestPower # Sets the number of loops to be equal to the largest power found.
    while loops >= 0:
        if float(dec_num) >= 2**largestPower: # This code runs if the input number is equal to or greater than 2 to the largest power found.
            dec_num = float(dec_num) - (2**largestPower) # This code will take away two to the largest power found from the input number,
            largestPower = largestPower - 1 # then will take away 1 from from the counter of the largest power,
            num_bi += "1" # then will add on a string containing the number "1", and then reduce the amount of loops by one.
            loops = loops - 1
        
        elif float(dec_num) < 2**largestPower: # This code runs if input number is less than 2 to the larget power found
            largestPower = largestPower - 1 # This elif statement will then also take away 1 from the largest power count and the loop counter,
            num_bi += "0" # but will add on a string of "0" instead.
            loops = loops - 1
    
    print(num_bi) # Prints the final result in binary.