
#finds the first common letter for a string of letters

string = "ABCA" #string to test

string = list(string)
print(string)

string_set = set(string)
print(string_set)

for i in string:
    if i in string_set:
        print(i, "is the first repeated letter.")
        break
    else:
        print("None are common/")

#Better way to do this is loop left to right and add letters to a table, creating counts as a new letter is happened upon. Return a count of 2...
