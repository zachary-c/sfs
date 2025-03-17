
# Echo program

""" print("Hello!")
msg = input("prompt>")
print(msg)
 """
# Repeatedly echo, till :exit
""" 
read = True
while read:
    msg = input(">")
    if msg == ':exit':
        #break
        read = False
    print(msg)
"""

# Record the user's messages and play them back
messages = []
while True:
    msg = input(">")
    if msg == ':exit':
        break
    if msg == ":all":
        print(messages)
    else:
        messages.append(msg)
        print(msg)
print("Take this with you!", messages)

# TODO: Extend the above to allow the user to print their list of messages mid program, instead of just at the end, with the keyword ":all"