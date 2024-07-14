thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[0] = "Pear" # Change list items at index 0
print(thislist)

# Add  item to list
thislist.append("Mango")
print(thislist)

#Duplicate item in list

thislist.append("cherry")
print(thislist)
print("len:", len(thislist))  # check for the length in a list

# Checking for the datatype 

print(type(thislist))

print(list(("apple", "banana", "cherry")))  # using the list constructor


#Changing a range of items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist) 


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # Inserting at a specific index


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # To concatenate a two list items.


thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

thislist.remove("apple") # Removing items  from this list.
print(thislist)

thislist.pop(1) # Removing at a specific Index

print(thislist)

thislist = ["apple", "banana", "cherry"]  # Clearing a list
# thislist.clear()
# print(thislist)

# for x in thislist:  # looping through a list
#     print(x)

# for x in range(len(thislist)):
#     print(x)

[print(x) for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [i for i in fruits if "a" in i]
print(newlist) 