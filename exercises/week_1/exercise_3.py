

# Exercise 03: for-loops #3
# For each comment (#) write an explanation of what the following line is doing. 
# For the comment "Output: " write what the print statement will print
# When you are finished, run the program to see if you are correct.
# Then, fill out the last comment with what the program does.
# The first comment is completed as an example.

# Declare a list of words
lst = ["apple", "goat", "card", "banana", "cheese", "rock", "ice"]

#
desired_length = 4

#
output_lst = []

#
for word in lst:
    #
    if len(word) == desired_length:
        #
        output_lst.append(word)

# Output: 
print(output_lst)

"""
Replace this with 1-2 sentences explaining what the program does.
"""

# Once you understand what the program does, try to predict what will happen 
# if you change the value of desired_length. Try it and see if you are correct!