

# Exercise 04: while-loops #1
# For each comment (#) write an explanation of what the following line is doing. 
# When you are finished, run the program to see if you are correct.
# Then, fill out the last comment with what the program does.

#
my_number = 4

# 
guessed_number = -1

#
print("Try to guess the number I am thinking of!")
#
while my_number != guessed_number:
    #
    print("Enter your guess:")
    #
    guessed_number = int(input("> "))
    #
    if guessed_number != my_number:
        # 
        print("Sorry, guess again.")

#
print("Congrats! You got it right. The number was " + str(my_number) + ".")

"""
Replace this with 1-2 sentences explaining what the program does.
"""

