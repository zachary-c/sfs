# TODO: Use a for-loop to iterate through a given list of strings and produce a new list containing only those entries that start with the letter "a"
""" lst = ['apple', 'bananas', 'artichoke', "zebras", 'grapes', 'anteaters']

newlst = []
for entry in lst:
    if entry[0] == 'a':
        newlst.append(entry)   
    print("newlst: ", newlst)

print(newlst)     
 """
# TODO: Use a for-loop to iterate through a given list of numbers and produce a new list containing all the numbers doubled
lst = [1, 2, 3, 4, 5, 0, 23 , 5, 3]
newlst = []
for entry in lst:
    newEntry = entry*2
    newlst.append(newEntry)

#print(newlst)
# TODO: Use a for-loop to iterate through a given list of numbers and check if they are all in ascending order
# print True if they are; False if not

#lst1 = [1, 4, 5, 6, 9, 10] # ascending
lst1 = [-10, -5, -2, 1, 4, 5, 7, 9, 10] # not in ascending order

last = lst1[0]
isAscending = True
for entry in lst1:
    if last <= entry:
        last = entry
    else:
        isAscending = False
        break

print(isAscending)